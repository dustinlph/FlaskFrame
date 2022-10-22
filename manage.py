# coding=utf-8
"""
@Project: FlaskFrame
@File: /manage.py
@Author: Dustin Lin
@Created on: 2022/10/22 16:39:09
"""
from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from app import create_app

app = create_app()
manager = Manager(app)
manager.add_command('run', Server(host='127.0.0.1', port=8090, use_reloader=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
