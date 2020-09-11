# 测试开发环境
import datetime

DEBUG = True

DIALECT = 'mysql'  # 数据库类型

DRIVER = 'pymysql'  # 数据库驱动

USERNAME = 'root'  # 用户名

PASSWORD = 'hao7883370'  # 密码

HOST = '192.168.81.130'  # 服务器

PORT = 3306  # 端口

DATABASE = 'news2'  # 数据库名

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT,
                                                                          DRIVER,
                                                                          USERNAME,
                                                                          PASSWORD,
                                                                          HOST,
                                                                          PORT,
                                                                          DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

SEND_FILE_MAX_AGE_DEFAULT = datetime.timedelta(seconds=1)

PER_PAGE = 5