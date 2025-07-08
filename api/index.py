from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from pymongo import MongoClient
from bson import ObjectId
import bcrypt
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI', 'mongodb+srv://shaikabdulrahiman0718:9MVMzzvlOH9C2dh3@cluster0.axirwvd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
db = client['blogging_platform']
users_collection = db['users']
blogs_collection = db['blogs']
categories_collection = db['categories']

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # type: ignore

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.username = user_data['username']
        self.email = user_data['email']
        self.is_admin = user_data.get('is_admin', False)

@login_manager.user_loader
def load_user(user_id):
    user_data = users_collection.find_one({'_id': ObjectId(user_id)})
    if user_data:
        return User(user_data)
    return None

# Initialize categories
def init_categories():
    if categories_collection.count_documents({}) == 0:
        categories = [
            {'name': 'Technology', 'description': 'Tech news and tutorials'},
            {'name': 'Travel', 'description': 'Travel experiences and tips'},
            {'name': 'Food', 'description': 'Recipes and food reviews'},
            {'name': 'Lifestyle', 'description': 'Personal development and lifestyle'},
            {'name': 'Business', 'description': 'Business insights and strategies'},
            {'name': 'Health', 'description': 'Health and wellness tips'},
            {'name': 'Entertainment', 'description': 'Movies, music, and entertainment'},
            {'name': 'Education', 'description': 'Learning and educational content'}
        ]
        categories_collection.insert_many(categories)

# Routes
@app.route('/health')
def health_check():
    """Health check endpoint for deployment verification"""
    return {
        'status': 'healthy',
        'message': 'BlogHub is running successfully!',
        'database': 'connected' if client.admin.command('ping') else 'disconnected'
    }

@app.route('/')
def home():
    # Get published blogs
    published_blogs = list(blogs_collection.find({'status': 'published'}).sort('created_at', -1))
    categories = list(categories_collection.find())
    return render_template('home.html', blogs=published_blogs, categories=categories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if user already exists
        if users_collection.find_one({'$or': [{'username': username}, {'email': email}]}):
            flash('Username or email already exists!', 'error')
            return redirect(url_for('register'))
        
        # Hash password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Create user
        user_data = {
            'username': username,
            'email': email,
            'password': hashed_password,
            'is_admin': False,
            'created_at': datetime.utcnow()
        }
        users_collection.insert_one(user_data)
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_data = users_collection.find_one({'username': username})
        if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data['password']):
            user = User(user_data)
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'error')
    
    return render_template('login.html')

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_data = users_collection.find_one({'username': username})
        if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data['password']):
            if user_data.get('is_admin', False):
                user = User(user_data)
                login_user(user)
                flash('Admin login successful!', 'success')
                return redirect(url_for('admin_panel'))
            else:
                flash('Access denied! This account does not have admin privileges.', 'error')
        else:
            flash('Invalid username or password!', 'error')
    
    return render_template('admin_login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/create-blog', methods=['GET', 'POST'])
@login_required
def create_blog():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        
        blog_data = {
            'title': title,
            'content': content,
            'category': category,
            'author_id': current_user.id,
            'author_username': current_user.username,
            'status': 'pending',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }
        
        blogs_collection.insert_one(blog_data)
        flash('Blog submitted for approval!', 'success')
        return redirect(url_for('my_blogs'))
    
    categories = list(categories_collection.find())
    return render_template('create_blog.html', categories=categories)

@app.route('/my-blogs')
@login_required
def my_blogs():
    user_blogs = list(blogs_collection.find({'author_id': current_user.id}).sort('created_at', -1))
    return render_template('my_blogs.html', blogs=user_blogs)

@app.route('/blog/<blog_id>')
def view_blog(blog_id):
    blog = blogs_collection.find_one({'_id': ObjectId(blog_id)})
    if not blog:
        flash('Blog not found!', 'error')
        return redirect(url_for('home'))
    return render_template('view_blog.html', blog=blog)

@app.route('/admin')
@login_required
def admin_panel():
    if not current_user.is_admin:
        flash('Access denied!', 'error')
        return redirect(url_for('home'))
    
    pending_blogs = list(blogs_collection.find({'status': 'pending'}).sort('created_at', -1))
    all_blogs = list(blogs_collection.find().sort('created_at', -1))
    return render_template('admin.html', pending_blogs=pending_blogs, all_blogs=all_blogs)

@app.route('/admin/approve/<blog_id>')
@login_required
def approve_blog(blog_id):
    if not current_user.is_admin:
        flash('Access denied!', 'error')
        return redirect(url_for('home'))
    
    blogs_collection.update_one(
        {'_id': ObjectId(blog_id)},
        {'$set': {'status': 'published', 'updated_at': datetime.utcnow()}}
    )
    flash('Blog approved!', 'success')
    return redirect(url_for('admin_panel'))

@app.route('/admin/reject/<blog_id>')
@login_required
def reject_blog(blog_id):
    if not current_user.is_admin:
        flash('Access denied!', 'error')
        return redirect(url_for('home'))
    
    blogs_collection.update_one(
        {'_id': ObjectId(blog_id)},
        {'$set': {'status': 'rejected', 'updated_at': datetime.utcnow()}}
    )
    flash('Blog rejected!', 'success')
    return redirect(url_for('admin_panel'))

@app.route('/category/<category_name>')
def category_blogs(category_name):
    blogs = list(blogs_collection.find({
        'category': category_name,
        'status': 'published'
    }).sort('created_at', -1))
    categories = list(categories_collection.find())
    return render_template('category.html', blogs=blogs, category_name=category_name, categories=categories)

init_categories()
# For Vercel Python serverless
def handler(request):
    return app(request)