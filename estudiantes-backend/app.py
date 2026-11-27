from flask import Flask
from config import config
from flask_mysqldb import MySQL
mysql= MySQL()

def create_app():
    #importacion va dentro de la funcion porque no se reconoce en objeto
    from controllers.controladorAlumno import controladorAlumnoBP
    app=Flask(__name__)
    app.register_blueprint(controladorAlumnoBP)
    app.config.from_object(config)
    mysql.init_app(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)