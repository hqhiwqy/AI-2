from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # 接收上传的文件
        file = request.files['headpic']
        # 保存上传的文件
        file.save('demo.png')
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)