from flask import Flask

app = Flask(__name__)



@app.route('/')
def DisplayData():
    with open('data.txt', 'r') as data:
        return data.read()



if __name__ == '__main__':
    app.run()
