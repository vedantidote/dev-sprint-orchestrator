# 🚀 PythonAnywhere Deployment Guide

## Prerequisites
- PythonAnywhere account (free or paid)
- Git repository with your code

## Step 1: Upload Your Code

### Option A: Using Git (Recommended)
```bash
# On PythonAnywhere console
git clone https://github.com/yourusername/dev-sprint-orchestrator.git
cd dev-sprint-orchestrator
```

### Option B: Using File Upload
1. Go to PythonAnywhere Files tab
2. Upload your project files
3. Extract if needed

## Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv dev-sprint-env

# Activate virtual environment
source dev-sprint-env/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Step 3: Configure Settings

1. **Update `settings_production.py`:**
   - Replace `yourusername.pythonanywhere.com` with your actual domain
   - Generate a new SECRET_KEY (use Django's `get_random_secret_key()`)

2. **Update `pythonanywhere_wsgi.py`:**
   - Replace `/home/yourusername/` with your actual PythonAnywhere path

## Step 4: Set Up Database

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

## Step 5: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

## Step 6: Configure Web App

1. Go to **Web** tab on PythonAnywhere
2. Click **Add a new web app**
3. Choose **Manual configuration**
4. Choose **Python 3.9** (or latest available)
5. Set **Source code** to your project directory
6. Set **Working directory** to your project directory

## Step 7: Configure WSGI File

1. Click on the WSGI configuration file
2. Replace the content with your `pythonanywhere_wsgi.py` content
3. Update the path to match your actual path

## Step 8: Configure Static Files

In the **Web** tab, add these static files mappings:

| URL | Directory |
|-----|-----------|
| /static/ | /home/yourusername/dev-sprint-orchestrator/staticfiles |
| /media/ | /home/yourusername/dev-sprint-orchestrator/media |

## Step 9: Reload Web App

Click **Reload** button in the Web tab.

## Step 10: Test Your Application

Visit your domain: `https://yourusername.pythonanywhere.com`

## 🔧 Troubleshooting

### Common Issues:

1. **Import Errors:**
   - Check that your virtual environment is activated
   - Verify all requirements are installed

2. **Static Files Not Loading:**
   - Ensure static files are collected: `python manage.py collectstatic`
   - Check static files configuration in Web tab

3. **Database Errors:**
   - Run migrations: `python manage.py migrate`
   - Check database permissions

4. **Permission Errors:**
   - Ensure your PythonAnywhere user has access to project files
   - Check file permissions

### Debugging:

1. **Check Error Logs:**
   - Go to Web tab → Error log
   - Look for specific error messages

2. **Test Locally:**
   - Use PythonAnywhere console to test commands
   - Run `python manage.py check` to verify settings

## 🔒 Security Checklist

- [ ] DEBUG = False in production settings
- [ ] SECRET_KEY is properly set
- [ ] ALLOWED_HOSTS includes your domain
- [ ] Static files are collected
- [ ] Database is properly configured
- [ ] Superuser account is created

## 📝 Environment Variables (Optional)

For better security, you can set environment variables:

```bash
# In PythonAnywhere console
export SECRET_KEY="your-secret-key-here"
```

## 🚀 Post-Deployment

1. **Test all functionality:**
   - User registration/login
   - Daily tracker features
   - Admin panel access

2. **Set up monitoring:**
   - Check error logs regularly
   - Monitor application performance

3. **Backup strategy:**
   - Regular database backups
   - Code version control

## 📞 Support

If you encounter issues:
1. Check PythonAnywhere documentation
2. Review Django deployment guide
3. Check error logs in Web tab
4. Test in PythonAnywhere console

Your application should now be live at `https://yourusername.pythonanywhere.com`! 