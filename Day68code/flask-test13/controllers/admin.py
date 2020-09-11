from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from common.forms import UserForm, ArticleForm
# 引入functools.wraps装饰器
from functools import wraps
from models.Article import Article
from models.User import User
from app import db
from config.default_setting import PER_PAGE
from datetime import datetime


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
@admin_route.route("/login", methods=['POST', 'GET'])
def login():
    """登录"""
    # 判断 如果是POST请求，就进行登录处理
    if request.method == 'POST':
        # 实现登录功能
        # 1.接收表单提交的数据
        username = request.form['username']  # 接收用户名
        password = request.form['password']  # 接收密码

        # 2.根据接收的用户名与user表中的数据进行查询
        user = User.query.filter_by(username=username, is_valid=1).first()

        # 3.查询用户名是否存在，如果存在，则进一步查询密码是否匹配，如果密码验证成功，就进行登录
        if user and check_password_hash(user.passwd, password):

            # 登录成功,使用session保存id，同时重定向到首页
            session['isLogged'] = 1
            session['userid'] = user.id
            session['username'] = user.username
            return redirect(url_for('.index'))
        else:
            # 登陆失败，通过flash提示错误
            flash("用户名或密码错误！")

    return render_template('/admin/login.html')


# 退出
@admin_route.route('/logout')
def logout():
    session.pop('userid', None)
    session.pop('username', None)
    return redirect(url_for(".login"))


# 管理员列表
@admin_route.route('/user')
@admin_route.route('/user/<int:page>')
@admin_login_require
def user_index(page=None):
    # 带分页查询
    if page is None:
        page = 1

    # 根据 ?search=搜索内容 来接受搜索的内容
    keyword = request.args.get('search')

    # 根据搜索条件进行查询
    if keyword:
        users = User.query \
            .filter(User.username.contains(keyword)). \
            order_by(User.id). \
            paginate(page=page, per_page=PER_PAGE)

        # 把搜索条件带到分页
        condition = "?search=" + keyword
        return render_template("admin/user/index.html", users=users, condition=condition)
    else:
        users = User.query.paginate(page, per_page=PER_PAGE)
        return render_template('/admin/user/index.html', users=users)


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

            flash("管理员创建成功！")
        except:
            flash("管理员创建失败！", category="error")

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


# 新闻列表
@admin_route.route('/article/')
@admin_route.route('/article/<int:page>')
@admin_login_require
def article_index(page=None):

    # 带分页查询
    if page is None:
        page = 1

    # 根据 ?search= 搜索内容 来接收内容
    keyword = request.args.get('search')

    # 按搜索条件来进行查询
    if keyword:
        articles = Article.query\
            .filter(Article.title.contains(keyword))\
            .order_by(Article.id)\
            .paginate(page=page, per_page=PER_PAGE)

        condition = "?search=" + keyword

        return render_template("admin/article/index.html", articles=articles, condition=condition)

    else:
        articles = Article.query.order_by(Article.title).paginate(page=page, per_page=PER_PAGE)
        return render_template("admin/article/index.html", articles=articles)


# 新增新闻
@admin_route.route('/article/add', methods=['GET', 'POST'])
@admin_login_require
def article_add():
    form = ArticleForm()

    # 判断表单验证是否通过
    if form.validate_on_submit():
        try:
            # 获取表单提交的数据
            articles = Article(
                title = form.title.data,
                content = form.content.data,
                types = form.types.data,
                img_url=form.img_url.data,
                author=form.author.data,
                is_recommend=form.is_recommend.data,
                is_valid=form.is_valid.data,
                created_at=datetime.now())
            db.session.add(articles)
            db.session.commit()
            flash("新闻添加成功！")
            return redirect(url_for('.article_index'))
        except:
            flash("新闻添加失败！", category="error")

    return render_template("admin/article/add.html", form=form)


# 编辑新闻
@admin_route.route('/article/edit/<int:pk>', methods=['GET', 'POST'])
@admin_login_require
def article_edit(pk):
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

