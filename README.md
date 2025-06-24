# Mireldar Babayev Blog Website

Welcome to the Mireldar Blog Website, a comprehensive platform powered by Python Django! This website offers a seamless blogging experience alongside additional features such as appointment scheduling and FAQs to enhance user engagement.

# Table of Contents

1. Features
2. Installation
3. Usage
4. Deployment
5. CI/CD
6. Technologies Used


# 🚀 Features

## General Pages

- Homepage: Welcoming users with featured blogs and services.
- Contact Page: Reach out for inquiries or feedback.
- About Us: Learn more about Mireldar Babayev’s blog journey.
- Services: Explore a range of services with detailed descriptions.
- Service Detail Page: Download related files directly.

## Blog Functionality

- Blog List Page: Browse an extensive collection of blogs.
    - Search and Tag Filters: Quickly find specific blogs by keywords or tags.
    - Category Filters: Narrow down blogs by categories.
    - Most Popular Blogs: Discover the most popular posts.
- Blog Detail Page: View blog content and engage via comments.

## Comments

- Add, edit, or delete comments (by the original author).
- Interactive discussions under blog posts.

## Appointment with Doctor

- Book Appointments: Users can schedule appointments with doctor.

## User Authentication

- Login/Registration: Secure account creation and authentication.

## FAQ Functionality

- FAQ Page: View frequently asked questions with answers.


# 🛠️ Installation

Follow these steps to set up the project locally:

1. Clone the Repository

    git clone https://github.com/shabnamadil/MireldarBabayev.git

2. Create a Virtual Environment (Recommended)

| **Platform** | **Command**                                        |
| ------------ | -------------------------------------------------- |
| Windows      | `python -m venv env`<br>`.\env\Scripts\activate`   |
| macOS/Linux  | `python3 -m venv env`<br>`source env/bin/activate` |


3. Setup project

    make dev-setup

4. Run Migrations

    make migrate-all

5. Start the Development Server

    make dev-run

# 🚀 Deployment

This project is containerized and deployed to production using Docker and AWS EC2. Below are the key deployment features.

- Dockerized Application for consistent environments across dev and production.

- Uwsgi as the WSGI server.

- NGINX as a reverse proxy and static file server.

- AWS EC2 as the cloud host.

- Environment Variables managed securely.

🔄 Continuous Integration & Deployment (CI/CD)

This project includes a basic CI/CD pipeline using GitHub Actions, configured to:

- Lint the code using flake8, black, and isort.

- Run tests on every push to main.

- Build and push Docker image to Docker Hub if tests pass.

# 📖 Usage

## General Usage

- Navigate to the homepage to explore featured content.
- Use the Blog List Page to browse blogs by search, tags, or categories.
- Access the Services Page for details and file downloads.
- Engage with blog posts by adding or editing comments.
- Register and log in for a personalized experience.

## Booking an Appointment

- Navigate to the Appointment Page.
- Submit the form to book the appointment.


# 🖥️ Technologies Used

- Backend: Python, Django, Django REST Framework
- Frontend: HTML, CSS, JavaScript
- Database: PostgreSql


Explore, engage, and elevate your experience with Mireldar Blog Website! ✨