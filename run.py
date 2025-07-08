#!/usr/bin/env python3
"""
Simple script to run the BlogHub application
"""

from app import app

if __name__ == '__main__':
    print("🚀 Starting BlogHub...")
    print("📝 A Multi-User Blogging Platform")
    print("🌐 Access the application at: http://localhost:5000")
    print("📚 Admin panel: http://localhost:5000/admin")
    print("=" * 50)
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    ) 