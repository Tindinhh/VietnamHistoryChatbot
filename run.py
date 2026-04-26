#!/usr/bin/env python
"""
Vietnamese History Chatbot - Main Entry Point
Run: python run.py
"""

import os
import sys
from pathlib import Path

# Add app directory to path
app_dir = Path(__file__).parent / 'app'
sys.path.insert(0, str(app_dir))

# Change to app directory
os.chdir(app_dir)

# Import and run Flask app
if __name__ == '__main__':
    from main import app
    
    print("\n" + "="*60)
    print("🇻🇳 SỬ VIỆT TOÀN THƯ - Vietnamese History Chatbot")
    print("="*60)
    print("✅ Flask app is starting...")
    print("📍 Open your browser: http://localhost:5000")
    print("⚠️  Press CTRL+C to stop the server")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
