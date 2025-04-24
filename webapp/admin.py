from django.contrib import admin

from webapp.models import Banner, Message

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'url', 'sort','add_time']
    list_per_page = 5
    list_max_show_all = 200
    list_filter = ['title', 'sort']
    list_display_links = ['title']
    pass
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message','add_time']
    list_per_page = 5
    list_max_show_all = 200
    list_filter = ['name','email']
    list_display_links = ['name']
    pass

# 设置app的标题
admin.site.site_header = '我的Django项目'
admin.site.site_title = '我的Django项目'


