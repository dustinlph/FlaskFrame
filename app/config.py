# coding=utf-8
"""
@Project: FlaskFrame
@File: app/config.py
@Author: Dustin Lin
@Created on: 2022/10/22 16:55:56
"""
import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
env = os.environ.get('Demo_app_config')
api_version = '0.4.0'


class Config(object):
    JWT_SECRET_KEY = "super-secret"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_TOKEN_LOCATION = ['headers', 'query_string']
    DEBUG = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PROT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "serversitehandler@gmail.com"
    MAIL_PASSWORD = "your-email-password"
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)


config_options = {
    'dev': DevConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevConfig
}