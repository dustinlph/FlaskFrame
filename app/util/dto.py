# coding=utf-8
"""
@Project: FlaskFrame
@File: app/util/dto.py
@Author: Dustin Lin
@Created on: 2022/10/22 17:37:41
"""
from flask_restx import Namespace, fields


class AuthDto:
    auth_api = Namespace('auth', description="This is a description of authentication")
    auth_request = auth_api.model('auth_request', {
        "username": fields.String(required=True, description='enter username', example="test"),
        "password": fields.String(required=True, description="enter password", example="test")
    })
    auth_response = auth_api.model('auth_response', {
        "access_token": fields.String(example="access token"),
        "refresh_token": fields.String(example="refresh token")
    })
