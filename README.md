# FlaskFrame
<h2>Envorinment: Python 3.7.9</h2>

---

<h3>V0.1.0</h3>

* Note:
  * Add app package
  * Add manage.py
  * Add requirements.txt
  * Run app with script successful. 
  * Installed:
    * pip install Flask==2.1.2
    * pip install Flask-Script
      * BUG: from flask_script._compat import text_type
---

<h3>V0.2.0</h3>

* Note:
  * Add DB, Migrate
    * manage.py add command
      * python manage.py db init
      * python manage.py db migrate -m "add users"
      * python manage.py db upgrade
  * Add model/users
  * Add config.py 
  * Installed: 
    * pip install Flask-SQLAlchemy==2.5.1
    * pip install Flask-Migrate==2.7.0
      * ImportError: cannot import name 'MigrateCommand' from 'flask_migrate' (C:\Users\Dustin\git\FlaskFrame\venv\lib\site-packages\flask_migrate\__init__.py)

---

<h3>V0.3.0</h3>

* Note:
  * Add resource/auth
  * API:
    * Add blueprint
      * /auth/login
      * /auth/refresh-token
    * Swagger:
      * Using Authorization: OK!
  * Installed:
    * pip install Flask-JWT-Extended
    * pip install flask-restx
  * Error
    * werkzeug:
      * ImportError: cannot import name 'parse_rule' from 'werkzeug.routing'
        * Fixed:
          * downgrade: werkzeug==2.1.2
          * Ref. https://blog.51cto.com/u_15830339/5758564

---

<h3>V0.3.1</h3>

* Note:
  * Refactor API
    * Move api settings into resource/
  * Add util/dto

---

<h3>V0.3.2</h3>

* Note:
  * Add environment in config.py
  * Setting env. by environment variable
  * Ref.
    * https://chinese.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds/