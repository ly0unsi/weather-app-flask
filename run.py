from flask import Flask
myapp = Flask(__name__)
if __name__ == "__main__":
    myapp.config.setdefault('WTF_CSRF_METHODS', ['PUT'])

    myapp.run(debug=True)
