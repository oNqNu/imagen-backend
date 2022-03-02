from flask import Flask
from flask_cors import CORS

# def create_app():
    
app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './uploads'

# from routes import processing
# app.register_blueprint(processing.bp)

@app.route('/')
def index():
    return 'hello, world'


if __name__ == "__main__":
    # app = create_app()
    app.run()