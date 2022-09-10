from flask import Flask
def launch_app():
    app=Flask(__name__)
    from first_flask.product.bussines import mod as user_module1
    app.register_blueprint(user_module1)
    return app
