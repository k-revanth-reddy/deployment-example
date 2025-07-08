#!/usr/bin/env python3
"""
Sample data script to populate BlogHub with demo content
Run this after setting up the admin user
"""

from pymongo import MongoClient
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

def create_sample_data():
    # Connect to MongoDB
    client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
    db = client['blogging_platform']
    users_collection = db['users']
    blogs_collection = db['blogs']
    
    print("=== BlogHub Sample Data Generator ===")
    print("This script will create sample users and blogs for demonstration")
    print()
    
    # Check if sample data already exists
    if blogs_collection.count_documents({}) > 0:
        print("Sample data already exists! Skipping...")
        return
    
    # Create sample users
    sample_users = [
        {
            'username': 'tech_writer',
            'email': 'tech@example.com',
            'password': 'hashed_password_placeholder',
            'is_admin': False,
            'created_at': datetime.utcnow() - timedelta(days=30)
        },
        {
            'username': 'travel_blogger',
            'email': 'travel@example.com',
            'password': 'hashed_password_placeholder',
            'is_admin': False,
            'created_at': datetime.utcnow() - timedelta(days=25)
        },
        {
            'username': 'food_lover',
            'email': 'food@example.com',
            'password': 'hashed_password_placeholder',
            'is_admin': False,
            'created_at': datetime.utcnow() - timedelta(days=20)
        }
    ]
    
    # Insert sample users
    user_ids = []
    for user in sample_users:
        result = users_collection.insert_one(user)
        user_ids.append(str(result.inserted_id))
        print(f"✅ Created user: {user['username']}")
    
    # Sample blog content
    sample_blogs = [
        {
            'title': 'The Future of Artificial Intelligence in 2024',
            'content': '''Artificial Intelligence has come a long way in recent years, and 2024 promises to be a groundbreaking year for the technology. From advanced language models to autonomous vehicles, AI is reshaping how we live and work.

The most significant developments this year include:

1. **Advanced Language Models**: New models are becoming more sophisticated, understanding context better than ever before.

2. **AI in Healthcare**: Machine learning algorithms are helping doctors diagnose diseases more accurately and quickly.

3. **Autonomous Systems**: Self-driving cars and drones are becoming more reliable and widespread.

4. **AI Ethics**: There's growing focus on responsible AI development and ethical considerations.

As we move forward, it's crucial to balance innovation with responsibility. The future of AI depends not just on technological advancement, but on how we choose to implement and regulate these powerful tools.

What are your thoughts on the AI revolution? Are you excited about the possibilities, or concerned about the implications?''',
            'category': 'Technology',
            'author_id': user_ids[0],
            'author_username': 'tech_writer',
            'status': 'published',
            'created_at': datetime.utcnow() - timedelta(days=15),
            'updated_at': datetime.utcnow() - timedelta(days=15)
        },
        {
            'title': 'My Journey Through Southeast Asia: A Traveler\'s Tale',
            'content': '''Last month, I embarked on an unforgettable journey through Southeast Asia, visiting Thailand, Vietnam, and Cambodia. The experience was nothing short of magical, filled with incredible food, friendly people, and breathtaking landscapes.

**Thailand - The Land of Smiles**
My adventure began in Bangkok, where the bustling streets and aromatic street food immediately captured my heart. The Grand Palace was a sight to behold, with its intricate architecture and golden spires reaching toward the sky.

**Vietnam - A Country of Contrasts**
From the modern energy of Ho Chi Minh City to the peaceful beauty of Ha Long Bay, Vietnam offered an incredible range of experiences. The food was absolutely incredible - pho, banh mi, and fresh spring rolls became my daily staples.

**Cambodia - Ancient Wonders**
Angkor Wat was the highlight of my trip. Watching the sunrise over the ancient temple complex was a spiritual experience I'll never forget. The local people were incredibly warm and welcoming.

**Travel Tips:**
- Always carry cash for street vendors
- Learn a few basic phrases in the local language
- Be respectful of local customs and traditions
- Try the street food - it's often the best!

This journey taught me that travel is not just about seeing new places, but about opening your mind to new cultures and perspectives.''',
            'category': 'Travel',
            'author_id': user_ids[1],
            'author_username': 'travel_blogger',
            'status': 'published',
            'created_at': datetime.utcnow() - timedelta(days=10),
            'updated_at': datetime.utcnow() - timedelta(days=10)
        },
        {
            'title': 'The Perfect Homemade Pizza: A Complete Guide',
            'content': '''Making pizza at home can be intimidating, but with the right techniques, you can create restaurant-quality pizza in your own kitchen. After years of experimentation, I've perfected my recipe and I'm excited to share it with you.

**The Dough:**
The secret to great pizza is in the dough. You'll need:
- 3 cups all-purpose flour
- 1 cup warm water
- 2 1/4 tsp active dry yeast
- 1 tsp salt
- 1 tbsp olive oil

Mix the ingredients and let the dough rise for at least 2 hours. The longer it rises, the better the flavor.

**The Sauce:**
A simple tomato sauce works best:
- 1 can crushed tomatoes
- 2 cloves garlic, minced
- 1 tbsp olive oil
- Salt and pepper to taste
- Fresh basil

**Toppings:**
Less is more! Choose 2-3 quality toppings. My favorites:
- Fresh mozzarella
- Basil leaves
- Prosciutto
- Mushrooms

**Baking:**
Preheat your oven to the highest temperature (usually 500°F). Use a pizza stone if you have one. Bake for 10-12 minutes until the crust is golden and the cheese is bubbly.

The key to success is patience and practice. Don't get discouraged if your first attempt isn't perfect - every pizza is a learning experience!''',
            'category': 'Food',
            'author_id': user_ids[2],
            'author_username': 'food_lover',
            'status': 'published',
            'created_at': datetime.utcnow() - timedelta(days=5),
            'updated_at': datetime.utcnow() - timedelta(days=5)
        },
        {
            'title': 'Building a Morning Routine That Actually Works',
            'content': '''We've all heard about the benefits of a morning routine, but creating one that actually sticks can be challenging. After trying countless approaches, I've finally found a routine that works for me and has transformed my productivity.

**My Current Routine:**
1. **5:30 AM - Wake up** (no snooze button!)
2. **5:35 AM - Drink water** (16 oz with lemon)
3. **5:40 AM - Light stretching** (10 minutes)
4. **5:50 AM - Meditation** (15 minutes)
5. **6:05 AM - Journal** (5 minutes)
6. **6:10 AM - Coffee and planning** (10 minutes)
7. **6:20 AM - Start work**

**Key Principles:**
- **Start small**: Don't try to change everything at once
- **Be consistent**: Do it every day, even on weekends
- **Track progress**: Use a habit tracker to stay motivated
- **Adjust as needed**: Your routine should evolve with your life

**Common Mistakes to Avoid:**
- Setting unrealistic goals
- Not preparing the night before
- Trying to do too much too soon
- Not having a backup plan

Remember, the best morning routine is the one you'll actually do. Start with just one or two habits and build from there.''',
            'category': 'Lifestyle',
            'author_id': user_ids[0],
            'author_username': 'tech_writer',
            'status': 'pending',
            'created_at': datetime.utcnow() - timedelta(days=2),
            'updated_at': datetime.utcnow() - timedelta(days=2)
        }
    ]
    
    # Insert sample blogs
    for blog in sample_blogs:
        result = blogs_collection.insert_one(blog)
        print(f"✅ Created blog: {blog['title']} (Status: {blog['status']})")
    
    print()
    print("🎉 Sample data created successfully!")
    print(f"📊 Created {len(sample_users)} users and {len(sample_blogs)} blogs")
    print("🌐 Visit http://localhost:5000 to see the platform in action")
    print("📚 Use the admin panel to approve pending blogs")

if __name__ == '__main__':
    create_sample_data() 