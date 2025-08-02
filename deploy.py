#!/usr/bin/env python
"""
Deployment script for PythonAnywhere
"""

import os
import subprocess
import sys

def run_command(command):
    """Run a command and print output"""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")
    return result.returncode == 0

def main():
    print("🚀 Starting deployment...")
    
    # Collect static files
    print("\n📦 Collecting static files...")
    if not run_command("python manage.py collectstatic --noinput"):
        print("❌ Failed to collect static files")
        return False
    
    # Run migrations
    print("\n🗄️ Running migrations...")
    if not run_command("python manage.py migrate"):
        print("❌ Failed to run migrations")
        return False
    
    # Create superuser if needed
    print("\n👤 Creating superuser...")
    print("You'll be prompted to create a superuser account.")
    if not run_command("python manage.py createsuperuser"):
        print("❌ Failed to create superuser")
        return False
    
    print("\n✅ Deployment completed successfully!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 