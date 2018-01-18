from flask import Flask
from app.main import main as main_blueprint


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.run(debug=True)
