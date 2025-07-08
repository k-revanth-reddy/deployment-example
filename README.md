# BlogHub - Multi-User Blogging Platform

A beautiful and modern multi-user blogging platform built with Flask, MongoDB, and Tailwind CSS. Users can write blogs, select categories, and have their content reviewed by admins before publication.

## 🚀 Features

### For Users
- **User Registration & Authentication**: Secure user registration and login system
- **Blog Creation**: Write and submit blogs with rich text content
- **Category Selection**: Choose from predefined categories for your blog
- **Blog Management**: View all your submitted blogs and their approval status
- **Beautiful UI**: Modern, responsive design with Tailwind CSS

### For Admins
- **Admin Panel**: Comprehensive dashboard to manage all blog submissions
- **Admin Login**: Dedicated admin login page with enhanced security
- **Blog Approval System**: Review, approve, or reject submitted blogs
- **Content Management**: View all blogs with detailed statistics
- **User Management**: Monitor user activity and blog submissions

### Platform Features
- **Category System**: 8 predefined categories (Technology, Travel, Food, Lifestyle, Business, Health, Entertainment, Education)
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Real-time Status Updates**: Track your blog approval status in real-time
- **Search & Filter**: Browse blogs by categories
- **Modern UI/UX**: Beautiful gradients, animations, and intuitive navigation

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: MongoDB
- **Frontend**: HTML + Tailwind CSS
- **Authentication**: Flask-Login with bcrypt password hashing
- **Icons**: Font Awesome
- **Styling**: Custom CSS with responsive design

## 📋 Prerequisites

Before running this application, make sure you have:

1. **Python 3.7+** installed on your system
2. **MongoDB** installed and running locally
3. **pip** (Python package manager)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd blogging-platform
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-super-secret-key-change-this-in-production
MONGODB_URI=mongodb://localhost:27017/
```

### 4. Start MongoDB
Make sure MongoDB is running on your system:
```bash
# On Windows
mongod

# On macOS/Linux
sudo systemctl start mongod
```

### 5. Create Admin User
Run the admin setup script to create your first admin account:
```bash
python setup_admin.py
```

### 6. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📁 Project Structure

```
blogging-platform/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── setup_admin.py        # Admin user setup script
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── templates/           # HTML templates
    ├── base.html        # Base template with navigation
    ├── home.html        # Home page with featured blogs
    ├── register.html    # User registration page
    ├── login.html       # User login page
    ├── admin_login.html # Admin login page
    ├── create_blog.html # Blog creation form
    ├── my_blogs.html    # User's blog management
    ├── view_blog.html   # Individual blog view
    ├── admin.html       # Admin panel
    └── category.html    # Category-specific blog listing
```

## 🎯 How It Works

### User Flow
1. **Registration**: Users create an account with username, email, and password
2. **Login**: Users authenticate to access the platform
3. **Blog Creation**: Users write blogs, select categories, and submit for review
4. **Status Tracking**: Users can view their blog approval status
5. **Reading**: Users can browse and read published blogs

### Admin Flow
1. **Admin Login**: Admins use the dedicated admin login page at `/admin-login`
2. **Review Process**: Admins review pending blog submissions
3. **Approval/Rejection**: Admins can approve or reject blogs
4. **Content Management**: Admins can view all blogs and manage content

### Blog Approval Process
1. User submits a blog → Status: **Pending**
2. Admin reviews the blog
3. Admin approves → Status: **Published** (visible to all users)
4. Admin rejects → Status: **Rejected** (not visible to public)

## 🎨 UI/UX Features

- **Modern Design**: Clean, professional interface with gradients and shadows
- **Responsive Layout**: Mobile-first design that works on all devices
- **Interactive Elements**: Hover effects, transitions, and smooth animations
- **Color-coded Status**: Visual indicators for blog approval status
- **Intuitive Navigation**: Easy-to-use navigation with clear call-to-actions
- **Loading States**: Proper feedback for user actions
- **Error Handling**: User-friendly error messages and validation

## 🔧 Configuration

### Database Configuration
The application uses MongoDB. You can configure the connection in the `.env` file:
```env
MONGODB_URI=mongodb://localhost:27017/
```

### Categories
The platform comes with 8 predefined categories:
- Technology
- Travel
- Food
- Lifestyle
- Business
- Health
- Entertainment
- Education

You can modify these in the `init_categories()` function in `app.py`.

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Vercel Deployment (Recommended)

For easy deployment to Vercel, follow these steps:

1. **Push your code to GitHub**
2. **Set up MongoDB Atlas** (cloud database)
3. **Deploy to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Add environment variables:
     - `SECRET_KEY`: Your Flask secret key
     - `MONGODB_URI`: Your MongoDB Atlas connection string
   - Deploy!

📖 **Detailed deployment guide**: See [DEPLOYMENT.md](DEPLOYMENT.md) for complete step-by-step instructions.

### Traditional Production Deployment
1. Set `DEBUG = False` in `config.py`
2. Use a production WSGI server like Gunicorn
3. Set up a production MongoDB instance
4. Configure environment variables for production
5. Set up a reverse proxy (nginx) if needed

## 🔒 Security Features

- **Password Hashing**: All passwords are hashed using bcrypt
- **Session Management**: Secure session handling with Flask-Login
- **Input Validation**: Form validation and sanitization
- **CSRF Protection**: Built-in CSRF protection
- **Secure Headers**: Proper security headers configuration

## 📊 Database Schema

### Users Collection
```json
{
  "_id": ObjectId,
  "username": "string",
  "email": "string",
  "password": "hashed_string",
  "is_admin": boolean,
  "created_at": datetime
}
```

### Blogs Collection
```json
{
  "_id": ObjectId,
  "title": "string",
  "content": "string",
  "category": "string",
  "author_id": "string",
  "author_username": "string",
  "status": "pending|published|rejected",
  "created_at": datetime,
  "updated_at": datetime
}
```

### Categories Collection
```json
{
  "_id": ObjectId,
  "name": "string",
  "description": "string"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:

1. Check the documentation
2. Review the error logs
3. Ensure MongoDB is running
4. Verify all dependencies are installed
5. Check environment variables are set correctly

## 🎉 Getting Started

1. **Start the application**: `python app.py`
2. **Create admin account**: `python setup_admin.py`
3. **Register as a user**: Visit `/register`
4. **Write your first blog**: Click "Write Blog" after login
5. **Access admin panel**: Use admin login at `/admin-login` or click "Admin Login" on home page
6. **Approve blogs**: Use admin panel at `/admin`

Enjoy blogging with BlogHub! 🚀 #   m u l t i b l o g g i n g - p l a t f o r m  
 # deployment-example
