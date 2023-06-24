from jazz.app import create_app

app = create_app()

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5001
    debug = True
    app.run(host, port, debug)