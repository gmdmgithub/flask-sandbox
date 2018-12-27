
from flask_sandbox import create_app

app = create_app()

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p','--port',default=5000)
    args = parser.parse_args()
    port = args.port
    app.run(debug=True, port=port) # delfault is left but can be change to any other (ofcourse can be change on Apache, Ngnix...)
