from django.db import models

choices = (
    ('男', '男性'),
    ('女', '女性'),
)


# 轮播图
class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图', max_length=200)
    url = models.URLField(max_length=200, verbose_name='访问地址')
    sort = models.IntegerField(default=1, verbose_name='顺序')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
    
# 留言
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    message = models.CharField(max_length=500, verbose_name='留言')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='留言时间')
    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name