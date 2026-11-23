# Quiz Application

A full-stack quiz web application built with Django and SQLite. Users can register, log in, take category-based quizzes, and track their performance over time.

## Features

- User authentication (register, login, logout) with user profiles
- Category-based quizzes — Maths, Physics, Chemistry, Biology, Geography, Aptitude, Personality, Current Affairs, Computer Science and Space
- Automated scoring with instant results
- Global leaderboard with top scores
- Performance tracking by category using Django ORM

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** SQLite
- **Frontend:** HTML, Bootstrap (dark mode supported)

## Getting Started

```bash
git clone https://github.com/Anuskapattanaik/QuizApplication.git
cd QuizApplication
python -m venv venv
venv\Scripts\activate        # on Windows
pip install django djangorestframework pillow
python manage.py migrate
python seed_db.py
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser and register an account to start quizzing.

## Developer

**Anushka Pattanaik**
- Email: pattanaikanuska1@gmail.com
- GitHub: [@Anuskapattanaik](https://github.com/Anuskapattanaik)
