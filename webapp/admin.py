from django.contrib import admin

# from webapp.models import User, Stock


# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     # 设置显示的字段
#     list_display = ['id', 'user_name', 'password', 'email', 'gender']
#     search_fields = ['user_name']
#     list_per_page = 5
#     list_max_show_all = 200
#     list_filter = ['user_name', 'gender']
#     list_display_links = ['user_name']
#     pass


# 设置app的标题
admin.site.site_header = '我的Django项目'
admin.site.site_title = '我的Django项目'


# @admin.register(Stock)
# class StockAdmin(admin.ModelAdmin):
#     # 设置显示的字段
#     list_display = ['id', 'company_name', 'date', 'open', 'high', 'low', 'close', 'adj_close', 'volume']
#     search_fields = ['company_name', ]
#     list_per_page = 30
#     list_max_show_all = 200
#     list_display_links = ['company_name']
#     # 排序
#     ordering = ['date']

    # 添加获取数据的方法
#     def get_data(self, request, queryset):
#         # 这里可以根据queryset过滤选择的公司
#         # 然后调用更新数据的函数
#         selected_companies = queryset.values_list('company_name', flat=True).distinct()
#         print(selected_companies)
#         # for company_name in selected_companies:
#         # 在这里调用更新数据的函数，这里只是一个示例
#         # self.update_data_for_company(company_name)
#
#     get_data.short_description = '获取数据'
#     actions = ['get_data']
#
#
# admin.action(StockAdmin)
