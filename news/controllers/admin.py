# 后台控制器

from datetime import datetime
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from common.forms import UserForm, ArticleForm

# 引入functools.wraps装饰器
from functools import wraps

from models.User import User
from models.Article import Article
from application import db

# 定义一个实现后台访问控制的装饰器函数 admin_login_require()

# 实例化一个蓝图

admin_route = Blueprint('admin', __name__)


def admin_login_require(f):
    # 使用functools.wraps装饰器装饰内函数wrapper，从而可以保留被修饰的函数属性
    @wraps(f)
    def wrapper(*args, **kwargs):
        # 判断是否登录
        if 'isLogged' not in session or session['isLogged'] != 1:
            # 如果session中没有isLogged的键名，则重定向到登录页
            return redirect(url_for('.login'))
        return f(*args, **kwargs)
    return wrapper


# 后台首页
@admin_route.route('/')
@admin_login_require
def index():
    return render_template("admin/index.html")


# 登录
@admin_route.route('/login', methods=["GET", "POST"])
def login():
    # 如果是POST请求，进行登录处理
    if request.method == "POST":
        # 实现登录功能
        # 1、接收表单提交过来的数据
        username = request.form['username']  # 接收的用户名
        password = request.form['password']  # 接收的用户密码

        # 2、根据接收用户名到user数据表进行查询
        user = User.query.filter_by(username=username, is_valid=1).first()

        # 查询一个不存在的用户名返回None
        # 3、判断用户是否存在，如果存在，则进一步需要检测密码是否正确，如果密码检测通过，则登录成功
        # if user and user.passwd == password:
        if user and check_password_hash(user.passwd, password):

            # 登录成功，使用session保存id，同时重定向到首页
            session['isLogged'] = 1
            session['userid'] = user.id
            session['username'] = user.username
            return redirect(url_for(".index"))
        else:
            # 登录失败，通过flash进行消息提示
            flash("账户或密码不对！")
            # return redirect(url_for("login"))

    return render_template("admin/login.html")


# 退出
@admin_route.route('/logout')
def logout():
    session.pop('userid', None)
    session.pop('username', None)
    return redirect(url_for(".login"))


# 新闻列表
@admin_route.route('/article/')
@admin_route.route('/article/<int:page>')
@admin_login_require
def article_index(page=None):

    # 带分页查询
    if page is None:
        page = 1

    # 根据 ?search=搜索内容 来接收搜索的内容
    keyword = request.args.get('search')
    # print(keyword)

    # 按搜索条件进行查询
    if keyword:
        articles = Article.query\
            .filter(Article.title.contains(keyword))\
            .order_by(Article.id)\
            .paginate(page=page, per_page=2)

        condition = "?search=" + keyword

        return render_template("admin/article/index.html", articles=articles, condition=condition)

    else:
        articles = Article.query.order_by(Article.title).paginate(page=page, per_page=5)
        return render_template("admin/article/index.html", articles=articles)


# 新增新闻
@admin_route.route('/article/add', methods=['GET', 'POST'])
@admin_login_require
def article_add():
    form = ArticleForm()
    # 判断表单是否验证通过
    if form.validate_on_submit():
        try:
            # 获取表单提交的数据
            article = Article(
                title=form.title.data,
                content=form.content.data,
                types=form.types.data,
                img_url=form.img_url.data,
                author=form.author.data,
                is_recommend=form.is_recommend.data,
                is_valid=form.is_valid.data,
                created_at=datetime.now())
            db.session.add(article)
            db.session.commit()
            flash("添加新闻成功！")
            return redirect(url_for(".article_index"))
        except:
            flash("添加新闻失败！", category="error")

    return render_template("admin/article/add.html", form=form)

# 编辑新闻
@admin_route.route('/article/edit/<int:pk>', methods=['GET', 'POST'])
@admin_login_require
def article_edit(pk):
    # print(pk)
    article = Article.query.get(pk)

    if article is None:
        return redirect(url_for('.article_index'))

    form = ArticleForm(obj=article)

    if form.validate_on_submit():
        try:
            article.title = form.title.data
            article.content = form.content.data
            article.types = form.types.data
            article.img_url = form.img_url.data
            article.author = form.author.data
            article.is_recommend = form.is_recommend.data
            article.is_valid = form.is_valid.data
            article.created_at = datetime.now()

            db.session.add(article)
            db.session.commit()
            flash("新闻编辑成功！")
            return redirect(url_for(".article_index"))
        except:
            flash("新闻编辑失败！", category="error")

    return render_template("admin/article/edit.html", form=form)


# 删除单个新闻
@admin_route.route('/article/delete/<int:pk>')
@admin_login_require
def article_delete(pk):
    article = Article.query.get(pk)
    if article is None:
        return redirect(url_for('.article'))
    try:
        db.session.delete(article)
        db.session.commit()
        flash("新闻删除成功！")
    except:
        flash("新闻删除失败！", category="error")

    return redirect(url_for('.article_index'))


# 管理员列表
@admin_route.route('/user')
@admin_route.route('/user/<int:page>')
@admin_login_require
def user_index(page=None):

    # 带分页查询
    if page is None:
        page = 1

    # 根据 ?search=搜索内容 来接收搜索的内容
    keyword = request.args.get('search')
    # print(keyword)

    # 按搜索条件进行查询
    if keyword:
        users = User.query\
            .filter(User.username.contains(keyword)).\
            order_by(User.id).\
            paginate(page=page, per_page=2)

        condition = "?search=" + keyword
        return render_template("admin/user/index.html", users=users, condition=condition)

    else:
        users = User.query.order_by(User.username).paginate(page=page, per_page=5)
        return render_template("admin/user/index.html", users=users)


# 新增管理员
@admin_route.route('/user/add', methods=['GET', 'POST'])
@admin_login_require
def user_add():
    form = UserForm()

    # 美化版打印 pprint
    # pprint.pprint(form.username.__dict__)

    # 判断表单验证是否通过
    if form.validate_on_submit():
        # print(form.username.data)
        try:
            user = User(form.username.data,
                        form.password.data,
                        form.is_valid.data)

            # print(form.is_valid.data)
            db.session.add(user)
            db.session.commit()
            flash("成功添加管理员！")
            return redirect(url_for(".user_index"))
        except:
            flash("添加管理员失败！", category="error")
    return render_template("admin/user/add.html", form=form)


# 编辑管理员
@admin_route.route('/user/edit/<int:pk>', methods=['GET', 'POST'])
@admin_login_require
def user_edit(pk):
    # print(pk)
    user = User.query.get(pk)
    if user is None:
        return redirect(url_for('.user_index'))
    form = UserForm(obj=user)

    # 判断表单验证是否通过
    if form.validate_on_submit():
        try:
            user.username = form.username.data
            user.passwd = generate_password_hash(form.password.data)
            user.is_valid = form.is_valid.data

            db.session.add(user)
            db.session.commit()

            flash("管理员编辑成功！")
        except:
            flash("管理员编辑失败！", category="error")

    return render_template("admin/user/edit.html", form=form)


# 删除单个管理员
@admin_route.route('/user/delete/<int:pk>')
@admin_login_require
def user_delete(pk):
    user = User.query.get(pk)
    if user is None:
        return redirect(url_for('.user_index'))
    try:
        db.session.delete(user)
        db.session.commit()
        flash("管理员删除成功！")
    except:
        flash("管理员删除失败！", category="error")

    return redirect(url_for('.user_index'))
