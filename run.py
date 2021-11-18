from api import application

app = application()

if __name__ == '__main__':
    app.run(port=5000, debug=False)