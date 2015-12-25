from webapp import create_app

app = create_app("conf/config.yml")

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
