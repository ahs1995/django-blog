# 📝 Django Blog Project

A fully functional blog web application built using Django, following the excellent [Corey Schafer's Django YouTube Tutorial Series](https://www.youtube.com/playlist?list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng).

## 🚀 Overview

This project is a classic blogging platform where users can:

- Register and log in to their accounts
- Create, edit, and delete their own posts
- View posts from all users in reverse chronological order
- Update their profile and profile picture
- Paginate posts for better user experience

It helped me grasp core Django concepts such as:

- Models, Views, and Templates (MVT pattern)
- User authentication & authorization
- Django forms and crispy forms
- Class-based and function-based views
- Django admin customization
- Media handling and static files
- URL routing and reverse resolution
- Deployment basics

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap 4
- **Database:** SQLite (default for development)
- **Authentication:** Django's built-in user system
- **Other Tools:** Crispy Forms, Pillow (for image handling)

---

## 🔧 Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ahs1995/django-blog.git
   cd corey

   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate

   ```

5. **Create a superuser (admin account):**

   ```bash
   python manage.py createsuperuser

   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver

   ```

7. **Visit the site:**

   Open http://127.0.0.1:8000/ in your browser.

## 🙏 Credits

Tutorial: Corey Schafer's Django Series on YouTube

Bootstrap: https://getbootstrap.com/

Django: https://www.djangoproject.com/

## 📜 License

This project is for educational purposes only. Feel free to use and modify it for learning.
