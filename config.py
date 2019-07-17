"""
    配置文件
    BaseConfig,DevConfig,ProductConfig
"""
import os


class BaseConfig(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or "KEY"
    WTF_I18N_ENABLED = False
    BABEL_DEFAULT_LOCALE = 'zh_cn'


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:////data.db"
    DEVELOPMENT_ENV = "development"


class ProductConfig(BaseConfig):
    DRIVER = "pymysql"
    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = "BankDataBase"

    SQLALCHEMY_DATABASE_URI = 'mysql+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
        DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
    )
