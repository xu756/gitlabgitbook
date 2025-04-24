from django.http import JsonResponse
from django.shortcuts import render
import gitlab
from webapp.models import Banner, Message
from django.views.decorators.csrf import csrf_exempt


gl = gitlab.Gitlab(url='http://192.168.190.129:8090/', private_token='glpat-hbSBsALhCR52ooe1syUh')
project = gl.projects.get(2, lazy=True)



def index(request):
    # posts = Post.objects.all()
    release = project.releases.list()
    banners = Banner.objects.order_by('sort')
    
    
    # 轮播图
    return render(request, 'index.html', {
        'release': release,
       'banners': banners,
    })



def gitlab_view(request):

    release = project.releases.list()
    print(release)

@csrf_exempt
def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        message = Message(name=name, email=email, message=message)
        message.save()
        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message':'error'})




# def stock_data_view(request, company_name):
#     # 公司名和年份
#     # company_name = request.GET.get('company_name', 'TSLA')

#     # 使用函数获取股票价格和移动平均线数据
#     stock_prices = get_stock_prices(company_name, years)

#     stock_prices.index = stock_prices.index.strftime('%Y-%m-%d')
#     stock_prices = stock_prices.reset_index()
#     stock_prices.rename(columns={
#         'Date': 'date',
#         'Open': 'open',
#         'High': 'high',
#         'Low': 'low',
#         'Close': 'close',
#         'Adj Close': 'adj_close',
#         'Volume': 'volume',
#     }, inplace=True)
#     stock_prices = stock_prices.dropna()
#     data = stock_prices.to_dict('records')
#     return JsonResponse(data, safe=False)


# def get_moving_average_view(request, company_name):
#     # 公司名和年份
#     # company_name = request.GET.get('company_name', 'TSLA')

#     # 使用函数获取股票价格和移动平均线数据
#     stock_prices = get_moving_average(company_name, years)

#     stock_prices.index = stock_prices.index.strftime('%Y-%m-%d')
#     stock_prices = stock_prices.reset_index()
#     stock_prices.rename(columns={
#         'Date': 'date',
#         'Adj Close': 'ma',
#     }, inplace=True)
#     stock_prices = stock_prices.dropna()
#     data = stock_prices.to_dict('records')
#     return JsonResponse(data, safe=False)


# # 日收益率
# def daily_return_view(request, company_name):
#     # 公司名和年份

#     # 使用函数获取股票价格和移动平均线数据
#     stock_prices = get_daily_return(company_name, years)

#     stock_prices.index = stock_prices.index.strftime('%Y-%m-%d')
#     stock_prices = stock_prices.reset_index()
#     print(stock_prices.info())
#     stock_prices.rename(columns={
#         'Date': 'date',
#         'Adj Close': 'daily_return',
#     }, inplace=True)
#     #  删除 daily_return 为NaN的
#     stock_prices = stock_prices.dropna()
#     data = stock_prices.to_dict('records')
#     return JsonResponse(data, safe=False)


# def save_stock_data(request, company_name):
#     data = get_stock_prices(company_name, years)
#     data.index = data.index.strftime('%Y-%m-%d')
#     stock_prices = data.reset_index()
#     stock_prices.rename(columns={
#         'Date': 'date',
#         'Open': 'open',
#         'High': 'high',
#         'Low': 'low',
#         'Close': 'close',
#         'Adj Close': 'adj_close',
#         'Volume': 'volume',
#     }, inplace=True)
#     #      保存数据到 Stock
#     for index, row in data.iterrows():
#         # 获取每一行数据的name
#         stock = Stock()
#         stock.add_data(company_name, index, row['Open'], row['High'], row['Low'], row['Close'],
#                        row['Adj Close'], row['Volume'])
#     return JsonResponse(data.to_dict('records'), safe=False)
