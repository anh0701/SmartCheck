from flask import Flask
from controllers.image_controller import image_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(image_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)