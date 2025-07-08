#!/usr/bin/env python3
"""
Setup script for Vercel deployment
This script helps initialize the application after deployment
"""

import os
from app import app, init_categories, users_collection
import bcrypt
from datetime import datetime

def setup_vercel():
    """Initialize the application for Vercel deployment"""
    print("🚀 Setting up BlogHub for Vercel deployment...")
    
    # Initialize categories
    print("📝 Initializing categories...")
    init_categories()
    
    # Check if admin user exists
    admin_user = users_collection.find_one({'is_admin': True})
    
    if not admin_user:
        print("👤 Creating admin user...")
        # Create admin user
        admin_data = {
            'username': 'admin',
            'email': 'admin@bloghub.com',
            'password': bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt()),
            'is_admin': True,
            'created_at': datetime.utcnow()
        }
        users_collection.insert_one(admin_data)
        print("✅ Admin user created!")
        print("   Username: admin")
        print("   Password: admin123")
        print("   ⚠️  Please change the password after first login!")
    else:
        print("✅ Admin user already exists")
    
    print("🎉 Setup complete!")
    print("📚 Your blogging platform is ready to use!")

if __name__ == '__main__':
    with app.app_context():
        setup_vercel() 