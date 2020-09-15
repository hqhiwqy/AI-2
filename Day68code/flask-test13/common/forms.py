# 表单验证
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed


# 管理员表单验证
class UserForm(FlaskForm):
    username = StringField("管理员账号",
                           validators=[DataRequired(message="请输入管理员账号！"),
                                       Length(5, 12, message="账号长度要求5~12字符！")],
                           render_kw={"class": "form-control",
                                      "placeholder": "请输入管理员账号"})

    password = PasswordField("管理员密码",
                             validators=[DataRequired(message="请输入管理员密码！"),
                                         Length(6, 8, message="密码长度要求6~8字符！")],
                             render_kw={"class": "form-control",
                                        "placeholder": "请输入管理员密码"})

    repassword = PasswordField("确认密码",
                               validators=[DataRequired(message="请再次输入密码！"),
                                           EqualTo("password", message="两次密码不一致！")],
                               render_kw={"class": "form-control",
                                          "placeholder": "请再次输入密码"})




    is_valid = BooleanField("是否启用")

    submit = SubmitField("提交", render_kw={"class": "btn btn-primary"})


# 新闻表单验证
class ArticleForm(FlaskForm):
    title = StringField("新闻标题",
                        validators=[DataRequired(message="请输入新闻标题！"),
                                    Length(1, 50, message="标题长度要求1~50字符！")],
                        render_kw={"class": "form-control",
                                   "placeholder": "请输入新闻标题"})
    content = TextAreaField('新闻详情',
                            validators=[DataRequired(message='请输入新闻详情')],
                            render_kw={"class": "form-control", "style": "resize:none"})
    types = SelectField('新闻类型',
                        choices=[('国内', '国内'), ('娱乐', '娱乐'), ('军事', '军事'), ('体育', '体育')],
                        render_kw={"class": "form-control"})

    img_url = FileField('新闻封面图片', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])

    # img_url = StringField('新闻封面图片',
    #                       validators=[DataRequired(message='请输入新闻图片路径')],
    #                       render_kw={"class": "form-control"})
    author = StringField('新闻来源',
                         validators=[DataRequired(message='请输入新闻来源')],
                         render_kw={"class": "form-control"})

    is_recommend = BooleanField('是否推荐')

    is_valid = BooleanField("是否启用")

    submit = SubmitField("提交", render_kw={"class": "btn btn-primary"})


# 修改管理员密码
class ChangeFrom(FlaskForm):

    username = StringField("管理员账号",
                           validators=[DataRequired(message="请输入管理员账号！"),
                                       Length(5, 12, message="账号长度要求5~12字符！")],
                           render_kw={"class": "form-control",
                                      "placeholder": "请输入管理员账号"})

    password = PasswordField("旧管理员密码",
                             validators=[DataRequired(message="请输入旧管理员密码！"),
                                         Length(6, 8, message="密码长度要求6~8字符！")],
                             render_kw={"class": "form-control",
                                        "placeholder": "请输入旧管理员密码"})

    newpassword = PasswordField("新管理员密码",
                                validators=[DataRequired(message="请输入新管理员密码！"),
                                            Length(6, 8, message="密码长度要求6~8字符！")],
                                render_kw={"class": "form-control",
                                           "placeholder": "请输入新管理员密码"})

    renewpassword = PasswordField("确认新密码",
                                  validators=[DataRequired(message="请再次输入新密码！"),
                                              EqualTo("newpassword", message="两次密码不一致!")],
                                  render_kw={"class": "form-control",
                                             "placeholder": "请再次输入新密码！"})

    submit = SubmitField("提交", render_kw={"class": "btn btn-primary"})