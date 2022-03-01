from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './uploads'

from routes import processing
app.register_blueprint(processing.bp)


if __name__ == "__main__":
    app.run()