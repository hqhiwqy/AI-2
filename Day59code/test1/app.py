from flask import Flask
from flask import render_template
from test1 import default_config

app = Flask(__name__)
app.config.from_object(default_config)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(port=5002)
