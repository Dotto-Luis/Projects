from flask import Flask
from views import router
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.register_blueprint(router)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
