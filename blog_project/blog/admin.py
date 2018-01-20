from django.contrib import admin
from blog.models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # 显示哪些列
    fields = ('title','desc','content',)
    # 除了哪些列，其他都显示
    #exclude = ('title','desc','content',)

    #fieldsets =
    #list_display =
    #list_display_links =
    #list_editable =
    #list_filter =
    #inlines =

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

#admindocs

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article,admin_class=ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Ad)
admin.site.register(Catagory)
admin.site.register(Links)