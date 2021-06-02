from flask import Flask
import subprocess
app = Flask(__name__)



@app.route('/fun/<command>')
def DisplayData(command):
    listcom = list(eval(command))
    test = subprocess.run(listcom, capture_output=True)
    return str(test)

@app.route('/')
def Hello():
    return 'Hello World'




if __name__ == '__main__':
    app.run(host='0.0.0.0')
