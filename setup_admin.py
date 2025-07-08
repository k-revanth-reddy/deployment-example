#!/usr/bin/env python3
"""
Setup script to create the first admin user for BlogHub
Run this script once to create an admin account
"""

from pymongo import MongoClient
import bcrypt
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def setup_admin():
    # Connect to MongoDB
    client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
    db = client['blogging_platform']
    users_collection = db['users']
    
    print("=== BlogHub Admin Setup ===")
    print("This script will create the first admin user for BlogHub")
    print()
    
    # Check if admin already exists
    existing_admin = users_collection.find_one({'is_admin': True})
    if existing_admin:
        print("An admin user already exists!")
        print(f"Username: {existing_admin['username']}")
        print("If you need to create another admin, please do it manually.")
        return
    
    # Get admin details
    username = input("Enter admin username: ").strip()
    email = input("Enter admin email: ").strip()
    password = input("Enter admin password: ").strip()
    
    if not username or not email or not password:
        print("All fields are required!")
        return
    
    # Check if user already exists
    if users_collection.find_one({'$or': [{'username': username}, {'email': email}]}):
        print("A user with this username or email already exists!")
        return
    
    # Hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Create admin user
    admin_data = {
        'username': username,
        'email': email,
        'password': hashed_password,
        'is_admin': True,
        'created_at': datetime.utcnow()
    }
    
    result = users_collection.insert_one(admin_data)
    
    if result.inserted_id:
        print()
        print("✅ Admin user created successfully!")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print("Role: Administrator")
        print()
        print("You can now log in to the admin panel at /admin")
    else:
        print("❌ Failed to create admin user!")

if __name__ == '__main__':
    setup_admin() 