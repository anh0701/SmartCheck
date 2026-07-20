from flask import Flask
from controllers.image_controller import image_bp
from controllers.detect_controller import detect_bp
# from db import init_db
from config import Config
from database import db

def create_app():
    app = Flask(__name__)

    # init_db()
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(image_bp)
    app.register_blueprint(detect_bp)

    with app.app_context():
        db.create_all()
    
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)