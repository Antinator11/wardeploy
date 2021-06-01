from flask import Flask

app = Flask(__name__)



@app.route('/fun/command')
def DisplayData(command):
    import subprocess
    test = subprocess.Popen([command], stdout=subprocess.PIPE)
    output = test.communicate()[0]
    return output



if __name__ == '__main__':
    app.run()
