from routes.api_routes import make_app
from tornado.ioloop import IOLoop
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Servidor iniciado en http://localhost:8888")
    IOLoop.current().start()