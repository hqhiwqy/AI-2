import os

DEBUG = False

SERVER_PORT = 5050

PROJECT_TITLE = "后台管理系统"

SUPPORT = "hqhiwqy"

SECRET_KEY = 'this is a random string'

PAGE_SIZE = 10

# 登录后需要忽视的URL
IGNORE_URLS = [
    "^/user/login"
]

# 登录前需要忽视的URL
IGNORE_CHECK_LOGIN_URLS = [
    "^/static"
]