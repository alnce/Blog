import logging
from django.shortcuts import render
from django.conf import settings
from django.db.models import Count
import json

logger = logging.getLogger('blog.views')


# Create your views here.
# Create your views here.
def global_setting(request):
    # 站点基本信息
    SITE_URL = settings.SITE_URL
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    # 分类信息获取（导航数据）
    #category_list = Category.objects.all()[:6]
    # 文章归档数据
    #archive_list = Article.objects.distinct_date()
    # 广告数据（同学们自己完成）
    # 标签云数据（同学们自己完成）
    # 友情链接数据（同学们自己完成）
    # 文章排行榜数据（按浏览量和站长推荐的功能同学们自己完成）
    # 评论排行
    #comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    #article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]
    return locals()

def index(request):
    try:
        open('1.txt','r')
    except Exception as e:
        logger.error(e)
    return render(request, 'base.html', locals())
