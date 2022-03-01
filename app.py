import os
from flask import Flask, current_app
from flask_cors import CORS

  
app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './uploads'

from routes import processing
app.register_blueprint(processing.bp)

app.run()

#     return app

# if __name__ == "__main__":
#     app = create_app()
#     app.run()