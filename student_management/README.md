# Student Management System

This is a Django-based Student Management System for managing student records, including features like student creation, editing, viewing, and searching. The system also includes user authentication to restrict access to certain features.

## Features

- Add, view, edit, and delete student records
- User authentication for secured access
- Search functionality to find students by name
- Pagination for viewing student lists
- Form validation for inputs like email and grade

## Prerequisites

Before setting up the project locally, ensure you have the following installed on your system:

- Python 3.x
- Virtualenv
- Git

## Installation

### Step 1: Clone the repository

Start by cloning the repository from GitHub using the following link in command line:
https://github.com/IanYuan00/GNG5300_FullStackDevelopment/tree/68c7c9aee52c56f0a801d2e60c82a09c199c1318/student_management

### Step 2: Set up a virtual environment

Create and avtivate a virtual environment using the following code:

python -m venv venv
#### On windows:
venv\Scripts\activate
#### On MacOS or Linux:
source venv/bin/activate

### Step 3: Setup the database
Run the migrations to set up theb database schema:

python manage.py makemigrations

python manage.py migrate

### Step 4: Create a superuser
Create an admin user to access the Django admin panel:
python manage.py createsuperuser

Follow the prompts to create a superuser account

### Step 5: Run the development server
Run the following command:
python manage.py runserver

Visit http://127.0.0.1:8000 in your browser to view the application.