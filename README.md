# 🚀 Dev Sprint Orchestrator

A comprehensive Django web application for managing daily team activities, leave tracking, and standup responses.

## ✨ Features

### 🔐 Authentication System
- **Custom User Model** with additional fields (employee_id, department, designation)
- **User Registration & Login** with beautiful Bootstrap UI
- **Profile Management** with detailed user information
- **Permission-based Access** for different features

### 📊 Daily Tracker
- **Leave Management** - Record full day, first half, or second half leaves
- **Standup Tracking** - Monitor daily standup responses
- **Smart Logic** - Users on leave (full day/first half) automatically excluded from standup records
- **Bulk Operations** - Efficient database operations with conflict handling

### 🎯 Admin Interface
- **Comprehensive User Management** with custom fields
- **Leave Records** with filtering and search capabilities
- **Standup Records** with response tracking and notes
- **Advanced Filtering** - Date hierarchies, search, and multiple filter options

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5, Font Awesome
- **Database**: SQLite (can be upgraded to PostgreSQL/MySQL)
- **Authentication**: Django's built-in auth system
- **Deployment**: PythonAnywhere ready

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/dev-sprint-orchestrator.git
   cd dev-sprint-orchestrator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv dev-sprint-env
   source dev-sprint-env/bin/activate  # On Windows: dev-sprint-env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
devsprintorchestrator/
├── custom_auth/                 # Authentication app
│   ├── models.py               # Custom User model
│   ├── views.py                # Auth views (login, logout, register)
│   ├── urls.py                 # Auth URL patterns
│   ├── admin.py                # Admin configuration
│   └── templates/custom_auth/  # Auth templates
├── daily_tracker/              # Daily tracking app
│   ├── models.py               # Leave and StandupRecord models
│   ├── views.py                # Tracker and recording views
│   ├── urls.py                 # Tracker URL patterns
│   ├── admin.py                # Admin configuration
│   └── templates/daily_tracker/ # Tracker templates
├── devsprintorchestrator/      # Main project
│   ├── settings.py             # Development settings
│   ├── settings_production.py  # Production settings
│   ├── urls.py                 # Main URL configuration
│   ├── views.py                # Home dashboard view
│   └── templates/              # Project templates
├── requirements.txt            # Python dependencies
├── manage.py                   # Django management script
└── README.md                  # This file
```

## 🔐 Usage

### Authentication
1. **Register** a new account or **Login** with existing credentials
2. **Access Dashboard** to see overview and quick actions
3. **Manage Profile** to view and update user information

### Daily Recording (Permission Required)
1. **Navigate** to "Record Daily" in the menu
2. **Set Date** (optional, defaults to today)
3. **Add Leave Entries**:
   - Type username for autocomplete search
   - Select leave type (Full Day/First Half/Second Half)
   - Click on user from dropdown to add
4. **Add Standup Defaulters**:
   - Type username for autocomplete search
   - Click on user from dropdown to mark as defaulter
5. **Submit Records** to save everything to database

### Admin Panel
- **User Management**: Add, edit, and manage users with custom fields
- **Leave Records**: Track and filter leave entries
- **Standup Records**: Monitor daily responses with notes

## 🚀 Deployment

### PythonAnywhere Deployment
See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed deployment instructions.

### Quick Deployment Steps:
1. Upload code to PythonAnywhere
2. Set up virtual environment and install requirements
3. Configure production settings
4. Run migrations and create superuser
5. Collect static files
6. Configure web app and WSGI file
7. Reload and test

## 🔧 Configuration

### Development Settings
- `DEBUG = True`
- SQLite database
- Development secret key

### Production Settings
- `DEBUG = False`
- Secure secret key
- Proper ALLOWED_HOSTS
- Static files configuration
- Logging setup

## 🛡️ Security Features

- **CSRF Protection** on all forms
- **Password Validation** with Django's built-in validators
- **Session Management** with secure settings
- **Permission-based Access** for sensitive features
- **Input Validation** and sanitization

## 📊 Database Models

### User Model (custom_auth.User)
- Extends Django's AbstractUser
- Additional fields: employee_id, department, designation
- Full admin integration

### Leave Model
- User (ForeignKey)
- Date (DateField)
- Half (IntegerField with choices: Full Day/First Half/Second Half)
- Timestamps (created_at, updated_at)

### StandupRecord Model
- User (ForeignKey)
- Date (DateField)
- Responded (BooleanField)
- Notes (TextField)
- Timestamps (created_at, updated_at)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues:
1. Check the [Django documentation](https://docs.djangoproject.com/)
2. Review the deployment guide
3. Check error logs
4. Create an issue in the repository

## 🎯 Roadmap

- [ ] Google OAuth integration
- [ ] Email notifications
- [ ] Advanced reporting
- [ ] Mobile app
- [ ] API endpoints
- [ ] Multi-tenant support

---

**Built with ❤️ using Django and Bootstrap** 