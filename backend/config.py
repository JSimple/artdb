import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class BaseConfig:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(
        basedir, "tmp", "app.db"
    )


class Development(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(
        basedir, "tmp", "app.dev.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Test(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"