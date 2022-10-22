# FlaskFrame
<h2>Envorinment: Python 3.7.9</h2>

---
<h3>V0.1.0</h3>
* Note:
  * Installed:
    * pip install Flask==2.1.2
    * pip install Flask-Script
      * BUG: from flask_script._compat import text_type
  * Add app package
  * Add manage.py
  * Add requirements.txt
  * Run app with script successful.
---
<h3>V0.2.0</h3>
* Note:
  * Installed: 
    * pip install Flask-SQLAlchemy==2.5.1
    * pip install Flask-Migrate==2.7.0
      * ImportError: cannot import name 'MigrateCommand' from 'flask_migrate' (C:\Users\Dustin\git\FlaskFrame\venv\lib\site-packages\flask_migrate\__init__.py)
  * Add DB, Migrate
    * manage.py add command
      * python manage.py db init
      * python manage.py db migrate -m "add users"
      * python manage.py db upgrade
  * Add model/users
  * Add config.py
