import os
from flask import Flask, request, url_for, send_from_directory, render_template, flash, session
from werkzeug.utils import secure_filename
# from pypinyin import lazy_pinyin
import uuid

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('./uploads_pic')  # 返回指定文件夹
# app.config['UPLOAD_FOLDER'] = os.getcwd()  # 返回当前目录
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.secret_key = os.urandom(24)


@app.route("/ping")
def ping():
    return "pong"


# 简单的文件上传
@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # 接收上传的文件
        file = request.files['headpic']
        # 保存上传的文件
        file.save('./uploads_pic/demo.png')
    return render_template('upload.html')


# 完整的文件上传
# 检查文件扩展名
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 获取上传后的文件 Url
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# 文件上传
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        # 接收上传的文件
        file = request.files['headpic']

        # 判断上传文件名
        if file and allowed_file(file.filename):
            # 导入 Werkzeug 提供的 secure_filename() 函数来检查文件名
            filename = secure_filename(file.filename)
            # filename = secure_filename(''.join(lazy_pinyin(file.filename)))
            print(filename)
            # 生成不重复的上传文件
            new_filename = uuid.uuid4().hex + '.' + filename.rsplit('.', 1)[1]
            # 保存上传的文件
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))

            # 获取上次文件的 Url
            file_url = url_for('uploaded_file', filename=file.filename)
            # print(filename)
            # 根据获取的文件 Url 显示图片
            return render_template('upload.html', url=file_url)
        else:
            flash('请上传符合类型的文件！')

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)

# https://blog.csdn.net/qq_36390239/article/details/98847888 解决文件名不是中文
