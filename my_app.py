from flask import Flask

app = Flask(__name__)

@app.route('/')

def hi_world():
    return 'Flask installation is complted.'

if __name__=='__main__':
      app.run()
