from django.db import models

# Create your models here.
class scrapy_manage(models.Model):
    task_id = models.CharField(max_length=20,primary_key=True)
    scrapy_id = models.CharField(max_length=500,null=True,blank=True)
    scope = models.CharField(max_length=2, null=True, blank=True)
    xsort = models.CharField(max_length=2, null=True, blank=True)
    category = models.CharField(max_length=2, null=True, blank=True)
    vip = models.CharField(max_length=2, null=True, blank=True)
    keyword = models.TextField(null=True, blank=True)
    date_time_begin = models.CharField(max_length=500, null=True, blank=True)
    date_time_begin = models.CharField(max_length=500, null=True, blank=True)
    date_time_end = models.CharField(max_length=500, null=True, blank=True)
    real_time_task = models.CharField(max_length=2, null=True, blank=True)
    class Meta:
        db_table = "scrapy_manage"
class weibo_post(models.Model):
    user_id = models.CharField(max_length=100,null=True,blank=True)
    post_id = models.CharField(max_length=100,)
    post_content = models.TextField(null=True,blank=True)
    post_time = models.DateTimeField(null=True,blank=True)
    forward_num = models.IntegerField(null=True,blank=True)
    comment_num = models.IntegerField(null=True,blank=True)
    like_num = models.IntegerField(null=True,blank=True)
    repost_id = models.CharField(max_length=20,null=True,blank=True)
    task_id = models.CharField(max_length=20)
    # 接下来设置联合主键
    class Meta:
        unique_together = ("post_id","task_id")
        db_table = "weibo_post"
class weibo_user(models.Model):
    user_id = models.CharField(max_length=100)
    fans_num = models.IntegerField(null=True,blank=True)
    authentication = models.CharField(max_length=1,null=True,blank=True)
    class Meta:
        db_table = "weibo_user"
class noise_judge(models.Model):
    post_id = models.CharField(max_length=100)
    task_id = models.CharField(max_length=100)
    noise = models.CharField(max_length=2,null=True,blank=True)
    # 接下来设置联合主键
    class Meta:
        unique_together = ("post_id", "task_id")
        db_table = "noise_judge"
class category(models.Model):
    post_id = models.CharField(max_length=100)
    task_id = models.CharField(max_length=100)
    category = models.CharField(max_length=500,null=True,blank=True)
    # 接下来设置联合主键
    class Meta:
        unique_together = ("post_id", "task_id")
        db_table = "category"
class event(models.Model):
    post_id = models.CharField(max_length=100)
    task_id = models.CharField(max_length=100)
    time = models.DateTimeField(null=True, blank=True)
    province = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    area = models.TextField(null=True, blank=True)
    event = models.TextField(null=True,blank=True)
    cluster = models.CharField(max_length=500,null=True,blank=True)
    # 接下来设置联合主键
    class Meta:
        unique_together = ("post_id", "task_id")
        db_table = "event"