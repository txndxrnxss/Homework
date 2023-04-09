from flask import Flask
from app1.views import blueprint_name

# Создание Flask приложения
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    app.register_blueprint(blueprint_name)                # Регистрация Blueprint
    return app

if __name__ == '__main__':
    create_app().run()