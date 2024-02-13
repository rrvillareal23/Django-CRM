# Django CRM Project

This Django CRM project is designed to manage customer records, track project statuses, and facilitate communication between staff members. It provides features such as user authentication, record management, adding notes, and updating project statuses.

## Features:

1. **User Authentication**: Users can register, login, and logout. Different user roles (e.g., Admin, Installer) are implemented to control access to certain functionalities.

2. **Customer Record Management**: Users can view, add, update, and delete customer records. Each record includes details such as customer name, contact information, and project status.

3. **Search and Filter**: Records can be searched using a keyword query. Additionally, records can be filtered based on specific project statuses.

4. **Sorting**: Records can be sorted based on various criteria such as ID, first name, last name, etc. Both ascending and descending orders are supported.

5. **Notes**: Users can add notes to customer records, documenting updates or important information. Notes are timestamped and associated with the respective record.

## Project Structure:

- **`crm/`**: Main Django application directory.
  - **`templates/`**: HTML templates for rendering views.
  - **`forms.py`**: Django forms for data validation.
  - **`models.py`**: Database models defining the structure of customer records, notes, and project updates.
  - **`views.py`**: Django views handling HTTP requests and rendering responses.
  - **`decorators.py`**: Custom decorators for controlling user access based on roles.
  - **`urls.py`**: URL patterns for routing requests to the appropriate views.
- **`static/`**: Static files such as CSS, JavaScript, and images.
- **`media/`**: User-uploaded media files (e.g., profile pictures).
- **`manage.py`**: Django's command-line utility for administrative tasks.
- **`requirements.txt`**: List of Python dependencies for the project.

## Setup Instructions:

1. Clone the repository: `git clone https://github.com/rrvillareal/django-crm.git`
2. Navigate to the project directory: `cd django-crm`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`
7. Access the application in a web browser: `http://localhost:8000`

## Usage:

1. **Home Page**: After logging in, users are redirected to the home page where they can view customer records and their project statuses.
2. **Navigation**: Use the navigation bar to access different sections such as adding records, adding notes, or logging out.
3. **Search and Filter**: Use the search box to search for specific records. Filter records by project status using the dropdown menu.
4. **Sorting**: Click on column headers to sort records based on different criteria.
5. **Record Details**: Click on a record to view its details, including associated notes and project updates.
6. **Adding Notes**: From the record details page, users can add notes to document updates or important information.
7. **Adding Records**: Admin users can add new customer records by clicking on the "Add Record" button.
8. **Updating Records**: Admin users can update existing records by clicking on the "Edit" button on the record details page.
9. **Deleting Records**: Admin users can delete records by clicking on the "Delete" button on the record details page.

## Contributing:

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests to improve the functionality or fix issues.
