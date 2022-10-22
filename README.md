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
  * Add environment in config.py
  * Setting env. by environment variable
  * Ref.
    * https://chinese.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds/

---

<h3>V0.3.2</h3>

* Note:
  * API:
    * /user/register
    * /user/<int: user_id> (GET, PUT, DELETE) 
  * Users model add func
    * Set password
    * Check password

---

<h3>V0.3.3</h3>

* Note:
  * Refactor DB
  * UsersModel adds 3 functions.
    * get_by_id
    * get_by_username
    * get_user_list
  * Login error handle
  * Login user verification before using /user/<int: id> API
  * Add resource/users
  * API:
    * /users: Get user list
    * Update /user/<int: user_id>
      * PUT
        * Need jwt verify, Only can update your account info
        * Only can change name, email
          * Known issue:
            * Need to enter both name, email, otherwise return 500
      * DELETE
        * Need jwt verify, Only can delete your account info
    * Update /user/register
      * email required.

---

<h3>V0.4.0</h3>

* Note:
  * Add util/mail
  * Add mail function
  * Update /user/register
    * Add send welcome mail function
  * Installed:
    * pip install Flask-Mail
  * Ref.
    * Gmail settings
      * https://ithelp.ithome.com.tw/articles/10270981?sc=iThomeR
    * Flask_Mail:
      * https://hackmd.io/@shaoeChen/BytvGKs4M?type=view

---

<h3>V0.4.1</h3>

* Note:
  * Add model: Data
  * Model: Base add 1 function.
    * set_updated_at

---

<h3>V0.4.2</h3>

* Note:
  * Add route/data
  * API:
    * /user/<int: user_id>/data (POST)
    * /user/<int: user_id>/data/<int: data_id> (GET, PUT, DELETE)
    * /user/<int: user_id>/alldata (GET)
    * Update:
      * /users -> /allusers
  * DB:
    * Update:
      * Data
        * title, info: unique==False
        * Adds 2 functions.
          * get_by_user_id_data_id
          * get_data_list_by_user_id