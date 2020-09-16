import time


class UrlManager:

    @staticmethod  # 静态方法 类或实例均可调用
    def build_url(path):
        return path

    @staticmethod
    def build_static_url(path):
        version = "%s" % (int(time.time()))  # "%s"一种字符串格式化的语法， 基本用法是将值插入到%s占位符的字符串中。
        path = '/static/' + path + "?v=" + version
        return UrlManager.build_url(path)

