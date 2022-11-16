# CS50W: Web Programming with Python and JavaScript

## Welcome to my CS50w final project

![main page](/screenshot/index.jpg)

### Video
The project's video: Click [here](https://youtu.be/322oe2GNMtQ)

### Course's link
Click [here](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript).

## MyPasswords
This Web App is my final project submission for the CS50w course. A password manager used to store logins/passwords and also notes.
MyPasswords is a webapp, running the backend in Python and frontend using React. The project was built using Django as the backend framework and ReactJS on the frontend with CDN. All generated information is saved in database (SQLite by default).

## Distinctiveness and Complexity

The complexity of this project can be seen in several parts. This project is different from all the others carried out so far.

One complexity I found came from the choice to integrate Django with a frontend framework like React, at first I didn't know how this would happen, there were many different approaches available, and I ended up choosing to incorporate React using CND. I was very interested in using React in a more streamlined way, taking more advantage of Django's power in frontend management.

I searched through several articles and blogs to find out how this would actually work, and if it would meet the behavior I was looking for, I came across the Django Rest Framework (DRF), but I ended up choosing not to use it, I will definitely be looking to understand more about this method later, i chose to create some routes that work as endpoints and it met my need.

Speaking of the app itself, it has all the basic requirements of a complex web app: user authentication/authorization, CRUD functionality, dynamic pages, etc. Some specific areas of complexity in this application include the search bar, where I had to study a lot about the map method to get the result I wanted.

In the same way I needed to understand about the django-cryptography library to apply it in this project. Finally, I managed to apply a lot of knowledge acquired during the course and I needed to look for other libraries/functions that met my initial purpose.

## Use and purpose
When it came time to start my final CS50w project, I thought of a few different projects (like a webapp for financial management). But in the course of planning I realized that I had a particular need that could be met with a webapp, so I changed my initial project and started developing it.

In my current job I manage many logins and accesses in different systems, which makes it difficult to memorize the passwords used in each one. Within this context, the idea of creating an application that would help me in this task arose.

The goals of the webapp are:

* Create login records that can be easily copied and a link to access the system.
* Create annotations that can be edited dynamically without reloading the page.
* Create a password generator with custom options.
* Make the application responsive to mobile devices.
* Test the application and its features.

## Most important pages

### Index page

This page is the application's Landing Page, with Login/Register options.

### Home

The page is configured to display user records after login, containing the options to edit and delete, hide and view passwords and copy information dynamically, if the user has not logged in, he will be redirected.

### Generator

Here the user can generate a strong password to be used in any application, using the upper/lower case, numbers and symbols options.

### Login, Logout, Register

The registration form is very simple and fast, leaving
the user ready to use the application's functions in less than a minute. After registering, the user is redirected to the home page, where he can create new records and view them. In Login, if something goes wrong, a feedback message is sent to the user.

## Some web design considerations

I opted for a simple design, using a predominant blue color pattern, with my own style sheet. I made use of custom fonts throughout the application (https://fonts.google.com/specimen/Fugaz+One?query=Fugaz+One, https://fonts.google.com/specimen/Fredoka+One?query=Fredoka+One, https://fonts.google.com/specimen/Fredoka?query=Fredoka, https://fonts.google.com/specimen/Roboto?query=Robot).

The entire application is responsive.

## Files and directories

### Structure
  - `mypasswords` - Main application directory.
    - `static/mypasswords` Contains all static content.
        - `img` This directory contains all the images used in the project.
        - `favicon.png` - Favicon image.
        - `styles.css` - CSS file.
    - `templates/mypasswords` Contains all application templates.
        - `_layout-index.html` - Base template for screens where the user is not logged in.
        - `_layout.html` - Base template for the screens where the user is logged in.
        - `generator.html` - Template to generate a new password.
        - `home.html` - Main template that shows all user records (only for registered users).
        - `index.html` - This template is the application's landing page.
        - `login.html` - For the user to log in.
        - `new.html` - Template for create new record.
        - `notes.html` - This template shows user annotations.
        - `passwords.html` - This template shows user passwords.
        - `register.html` - For the user to register.
    - `admin.py` - Custom django admin view.
    - `models.py` - Contains all models used in the project..
    - `urls.py` - all application URLs.
    - `views.py` respectively, contains all application views.
  - `finalproject` - project directory.

### Details

`generator.html`: On this page, using a react component, I created the functionality for the user to generate a password, which can be used in some external application, he can choose to include uppercase letters, lowercase letters, numbers and symbols, as well as the number of characters between 4 and 40. There are some validations, such as at least one of these mentioned character types.

`home.html`: Here, an authenticated user will be able to see all his records, both passwords and annotations, with CRUD methods, where there is a specific button for creating new records, and an option to edit or delete each one individually, there is Also a preview password button for added security. The biggest difficulty I found was in the search bar, where I would like the user to do a search and all related items to appear dynamically, I got the expected result using the filter and map methods.

`index.html`: This is the page seen by the user when arriving at the application, I opted for a minimalist design.

`login.html`: The user who tries to access any page that requires authentication will be redirected here in order to enter his credentials and continue browsing.

`new.html`: Page where the user creates a new record, when selecting the "type" of record, the page dynamically updates with the information that needs to be filled in by the user, without having to reload it.

`notes.html`: Similar to the "home" page, the difference is that it will only display the user's notes.

`passwords.html`: Like the previous one, it looks like the "home" page, but this one will only display the user's password records.

`register.html`: Page for registering a new user.

## Installation
  - Install project dependencies by running `pip install -r requirements.txt`.
  - Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`

