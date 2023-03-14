from flask import Flask
app = Flask(__name__)
if __name__ == "__main__":
    app.config.setdefault('WTF_CSRF_METHODS', ['PUT'])

    myapp = app.run(debug=True)
