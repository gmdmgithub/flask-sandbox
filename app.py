
from flask_sandbox import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000) # delfault is left but can be change to any other (ofcourse can be change on Apache, Ngnix...)
