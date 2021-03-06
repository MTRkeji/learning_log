#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        return self.text
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50]+"..."
class Software(models.Model):
    """软件"""
    name = models.CharField(max_length=200)
    links = models.CharField(max_length=200)
    pwd = models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Tip(models.Model):
    """首页条目"""
    name = models.CharField(max_length=200)
    links = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
