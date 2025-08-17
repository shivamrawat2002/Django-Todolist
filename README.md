# Django Todo Application

A simple and elegant Todo application built with Django that allows users to create, manage, and track their tasks efficiently.

## 🚀 Features

- **Create Todos**: Add new tasks with title and description
- **View Todo List**: See all your todos in a clean table format
- **Mark as Complete**: Mark tasks as completed with a single click
- **Delete Todos**: Remove completed or unwanted tasks
- **Responsive Design**: Bootstrap-powered UI that works on all devices
- **Real-time Updates**: Immediate reflection of changes in the interface

## 🛠️ Technologies Used

- **Backend**: Django 4.2.23
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 4.6.2
- **JavaScript**: jQuery 3.7.1 (slim), Popper.js 1.16.1
- **Python**: 3.9+
- **Template Engine**: Django Template Language (DTL)
- **Web Server**: Django Development Server

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.9 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd mytodo
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install django
```

### 5. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

### 8. Access the Application
Open your browser and navigate to:
- **Main App**: http://127.0.0.1:8000/ or http://127.0.0.1:8000/todo/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
mytodo/
├── manage.py                 # Django management script
├── mytodo/                  # Project configuration
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── todo/                    # Todo app
│   ├── __init__.py
│   ├── admin.py            # Admin interface configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── tests.py
│   └── migrations/         # Database migrations
├── templates/               # HTML templates
│   └── todo/
│       └── index.html      # Main todo interface
├── db.sqlite3              # SQLite database
└── venv/                   # Virtual environment
```

## 🎯 How to Use

### Creating a New Todo
1. Navigate to the main page (`/` or `/todo/`)
2. Fill in the title field (required)
3. Add a description (optional)
4. Click "Submit" button
5. The page refreshes and shows your new todo in the table below

### Managing Todos
- **Complete a Todo**: Click the "complete" button to mark a task as done
- **Delete a Todo**: Click the "delete" button to remove a task
- **View Status**: Completed todos show a green "completed" badge instead of the complete button
- **Real-time Updates**: All changes are immediately visible after page refresh

## 🔧 Configuration

### Database
The application uses SQLite3 by default. To change the database:

1. Update `DATABASES` in `mytodo/settings.py`
2. Run migrations: `python manage.py migrate`

### Static Files
Static files are served from the `static/` directory. Update `STATIC_URL` in settings if needed.

## 🧪 Testing

Run the test suite with:
```bash
python manage.py test
```

## 📱 API Endpoints

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | Home page with todo list |
| `/todo/` | GET | Todo list page |
| `/todo/create/` | POST | Create new todo |
| `/todo/complete/<id>/` | GET | Mark todo as complete |
| `/todo/delete/<id>/` | GET | Delete a todo |
| `/admin/` | GET | Django admin interface |

## 🎨 Customization

### Styling
- Modify `templates/todo/index.html` for UI changes
- Update Bootstrap classes for different themes
- Add custom CSS in the template
- Customize Bootstrap components (buttons, forms, tables)

### Functionality
- Extend `todo/views.py` for additional features
- Modify `todo/models.py` for database changes
- Update `mytodo/urls.py` for new routes
- Add new model fields or methods
- Implement user authentication
- Add todo categories or due dates

## 🚨 Troubleshooting

### Common Issues

1. **Template Not Found Error**
   - Ensure templates are in the correct directory
   - Check `TEMPLATES_DIR` setting in `settings.py`

2. **Database Migration Errors**
   - Delete `migrations/` folder and `db.sqlite3`
   - Run `python manage.py makemigrations` again

3. **Import Errors**
   - Activate virtual environment
   - Install required packages with `pip install -r requirements.txt`

### Debug Mode
Set `DEBUG = True` in `settings.py` for detailed error messages during development.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Shivam Rawat**
- GitHub: [@your-username]
- Email: your.email@example.com

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Python Community

## 📞 Support

If you encounter any issues or have questions:
- Create an issue on GitHub
- Contact the author directly
- Check the Django documentation

---

**Happy Coding! 🎉**
