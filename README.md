# CampusConnect (FirstDjango)

**Name:** Kimmy Swain C. Alontaga
**Section:** CSIT327 – G1

## Description
A Django app with user sign-up, login, and an editable profile page,
styled with Bootstrap 5.

## Features
- Sign-up with a success message
- Login / Logout
- Profile page (view and edit your own profile, login required)
- Bootstrap 5 styling through a shared base.html

## How to Run

1. Clone the repository
   ```
   git clone https://github.com/ykm1216/campusconnectg1.git
   cd campusconnectg1
   ```
2. Create and activate a virtual environment
   ```
   python3 -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Apply migrations
   ```
   python3 manage.py migrate
   ```
5. Run the server
   ```
   python3 manage.py runserver
   ```
6. Open http://127.0.0.1:8000/login/ in your browser.