## Mireldar Babayev Blog Website

Welcome to the Mireldar Blog Website, a comprehensive platform powered by Python Django! This website offers a seamless blogging experience alongside additional features such as appointment scheduling and FAQs to enhance user engagement.

## Table of Contents

1. Features
2. Installation
3. Usage
4. Technologies Used


🚀 Features

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

- Book Appointments: Users can schedule appointments with doctors.

## User Authentication

- Login/Registration: Secure account creation and authentication.

## FAQ Functionality

- FAQ Page: View frequently asked questions with answers.


🛠️ Installation

Follow these steps to set up the project locally:

1. Clone the Repository

    git clone https://github.com/shabnamadil/MireldarBabayev.git

2. Create a Virtual Environment (Recommended)

    python3 -m venv env
    .\env\Scripts\activate

3. Install Dependencies

    pip install -r requirements.txt

4. Run Migrations

    cd app
    python3 manage.py makemigrations
    py manage.py migrate

5. Start the Development Server

    python3 manage.py runserver


📖 Usage

## General Usage

- Navigate to the homepage to explore featured content.
- Use the Blog List Page to browse blogs by search, tags, or categories.
- Access the Services Page for details and file downloads.
- Engage with blog posts by adding or editing comments.
- Register and log in for a personalized experience.

## Booking an Appointment

- Navigate to the Appointment Page.
- Submit the form to book the appointment.


🖥️ Technologies Used

- Backend: Python, Django, Django REST Framework
- Frontend: HTML, CSS, JavaScript
- Database: SQLite


Explore, engage, and elevate your experience with Mireldar Blog Website! ✨