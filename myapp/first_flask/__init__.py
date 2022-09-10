# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from config import app_config
#
# db = SQLAlchemy()
#
#
# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(app_config[config_name])
#     from first_flask.vendor.view1 import mod as user_modul1
#     db.init_app(app)
#
#     app.register_blueprint(user_modul1)
#     return app
### ------------------this code for vendor directory -----------------------
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from config import app_config
#
# db = SQLAlchemy()
#
#
# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(app_config[config_name])
#     from first_flask.vendor.view1 import mod as users_module
#     db.init_app(app)
#     app.register_blueprint(users_module)
#     return app

#####----------------------------------------------------------------------------##




############-------------------------------- this code for employee info direcoty relationship-------------------------------------##

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from empconfig1 import app_config
# db=SQLAlchemy()
#
# def create_app(config_name):
#     app=Flask(__name__)
#     app.config.from_object(app_config[config_name])
#     from first_flask.employee_info_relation.view_emp import mod as emp_module
#     db.init_app(app)
#
#     app.register_blueprint(emp_module)
#     return app




############------------------------------- this code for student info relationship-------------------------##

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from stuinfoconfig2  import app_config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    from first_flask.student_info_relation.stu_views import mod as user_module
    db.init_app(app)

    app.register_blueprint(user_module)
    return app


