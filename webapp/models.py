from django.db import models

choices = (
    ('男', '男性'),
    ('女', '女性'),
)


# 创建一个模型类
# 保存

#     'Date': 'date',
#     'Open': 'open',
#     'High': 'high',
#     'Low': 'low',
#     'Close': 'close',
#     'Adj Close': 'adj_close',
#     'Volume': 'volume',

# class Stock(models.Model):
#     id = models.AutoField(primary_key=True)
#     company_name = models.CharField(max_length=100, default='TSLA', verbose_name="公司名")
#     date = models.DateField(verbose_name='日期')
#     open = models.FloatField(verbose_name='开盘价')
#     high = models.FloatField(verbose_name='最高价')
#     low = models.FloatField(verbose_name='最低价')
#     close = models.FloatField(verbose_name='收盘价')
#     adj_close = models.FloatField(verbose_name='调整后的收盘价')
#     volume = models.FloatField(verbose_name='成交量')

#     def __str__(self):
#         return self.company_name

#     class Meta:
#         db_table = 'stock'
#         verbose_name = '股票列表'
#         verbose_name_plural = verbose_name

#     #         添加数据
#     def add_data(self, company_name, date, open, high, low, close, adj_close, volume):
#         #  先根据时间和公司名查询是否有数据，如果有则更新，没有则添加
#         stock = Stock.objects.filter(company_name=company_name, date=date)
#         if stock:
#             stock.update(company_name=company_name, date=date, open=open, high=high, low=low, close=close,
#                          adj_close=adj_close, volume=volume)
#         else:
#             stock = Stock.objects.create(company_name=company_name, date=date, open=open, high=high,
#                                          low=low,
#                                          close=close, adj_close=adj_close, volume=volume)
#             stock.save()
#         return self

#     def get_data(self, company_name):
#         # 返回公司名为company_name的所有数据
#         self.company_name = company_name
#         return Stock.objects.filter(company_name=company_name)


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