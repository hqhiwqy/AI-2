
打造一个高可用的Flask MVC框架



|——application.py  定义和创建Flask应用实例

|——common
        |——libs    公共函数、公共类
        |——models  模型        
        
|——config
        |——base_setting.py   基础配置文件
        |——local_setting.py  本地环境配置文件
        
|——manager.py  命令行脚本文件

|——README.md   项目说明文档

|——requirements.txt   Python环境依赖包

|——web
       |——controlles  控制器（蓝图文件）
       |——static      静态资源
       |——templates   模板   
       
|——www.py  统一注册蓝图的文件


* 创建初始管理员账号
from application import db, app
from common.models.User import User

admin = User('admin', '123456', 1)
db.session.add(admin)
db.session.commit()