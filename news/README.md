# flask-news
Flask实战——新闻管理系统


## 项目需求

### 前台

* 首页：展示所有新闻列表
* 新闻分类页：点击某一个分类展示此分类下面的新闻列表
* 新闻推荐页：点击推荐展示所有推荐的新闻列表
* 新闻详情页：展示新闻详情（新闻标题、发布时间、新闻来源、新闻内容）

### 后台

管理员在后台进行登录，登录之后就可以进行新闻管理（发布、修改、删除等）。

* 登录
* 新闻列表（带分页）
* 发布新闻
* 修改新闻
* 删除新闻
* 新闻推荐


## 数据库设计

### 新闻表——articles

| 字段名称 | 字段类型 | 备注 |
| -------- | -------- | -------- |
| id     | Integer    | 主键，由系统自动生成    |
| title     | String(200)     | 新闻标题    |
| content    | Text()    | 新闻内容     |
| types    | String(10) | 新闻分类  |
| img_url    | String(300) | 新闻封面图 |
| author    | String(20) | 新闻作者  |
| view_count   | Integer | 阅读量  |
| created_at   | DateTime | 创建时间  |
| is_valid   | Boolean | 是否上架 1-上架 0-下架  默认1 |
| is_recommend   | Boolean | 是否推荐 1-推荐 0-不推荐 默认0  |

根据数据表的设计创建news模型如下：

```
class Articles(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    types = db.Column(db.String(10), nullable=False)
    img_url = db.Column(db.String(300))
    author = db.Column(db.String(20))
    view_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean, default=1)
    is_recommend = db.Column(db.Boolean, default=0)

```