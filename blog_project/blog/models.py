# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#用户
#采用继承方式扩展用户信息（本系统采用）
#扩展：关联的方式去扩展用户信息
class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d",default="avatar/default.png",max_length=200,verbose_name="头像")
    qq = models.CharField(max_length=20,blank=True,null=True,verbose_name="QQ号码")
    mobile = models.CharField(max_length=11,blank=True,null=True,unique=True,verbose_name="手机号码")

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ["-id"]

    def __unicode__(self):
        return self.username

#tag(标签)
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name="标签名称")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name


#分类
class Catagory(models.Model):
    name = models.CharField(max_length=50, verbose_name="分类名称")
    index = models.IntegerField(default=999,verbose_name="分类的排序")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

#文章模型
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="文章标题")
    desc = models.CharField(max_length=255,verbose_name="文章描述")
    content = models.TextField(verbose_name="文章内容")
    click_count = models.IntegerField(default=0,verbose_name="点击次数")
    is_recommend = models.BooleanField(default=False,verbose_name="是否推荐")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User,related_name='user_article',verbose_name="用户")
    catagory = models.ForeignKey(Catagory,related_name='catagory_article',blank=True,null=True,verbose_name="分类")
    tag = models.ManyToManyField(Tag,verbose_name="标签")
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ["-date_publish"]

    def __unicode__(self):
        return self.title

#评论
class Comment(models.Model):
    content = models.TextField(verbose_name="评论内容")
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    user = models.ForeignKey(User,related_name='user_comment',blank=True,verbose_name="用户")
    article = models.ForeignKey(Article,related_name='article_comment',blank=True,null=True,verbose_name="文章")
    pid = models.ForeignKey('self',blank=True,null=True,verbose_name="父级评论")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ["-date_publish"]

    def __unicode__(self):
        return str(self.id)

#友情链接
class Links(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题")
    description = models.CharField(max_length=255,verbose_name="友情链接描述")
    callback_url = models.URLField(verbose_name="url地址")
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    index = models.IntegerField(default=999,verbose_name="排列顺序(从小到大)")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name
        ordering = ["index","id"]

    def __unicode__(self):
        return self.title

#广告
class Ad(models.Model):
    title = models.CharField(max_length=50,verbose_name="广告标题")
    description = models.CharField(max_length=255,verbose_name="广告描述")
    image_url = models.ImageField(null=True,blank=True,verbose_name="回调url")
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    index = models.IntegerField(default=999,verbose_name="排列顺序(从小到大)")

    class Meta:
        verbose_name = "广告"
        verbose_name_plural = verbose_name
        ordering = ["index","id"]

    def __unicode__(self):
        return self.title
























