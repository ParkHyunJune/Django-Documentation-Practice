"""
Post 모델
    author = User와 연결
    title
    content
    created_date
        DateTimeField 사용
    modfied_date
        DateTimeField 사용
Comment 모델
    post = Post와 연결
    author = User와 연결
    content
    created_date
    modified_date

User 모델
    name
    created_date
    modified_date
"""

from django.db import models
from utils.models.mixins import TimeStampedMixin


class Post(TimeStampedMixin):
    author = models.ForeignKey('User')
    title = models.CharField(max_length=50)
    content = models.TextField()
    # created_date = models.DateField(auto_now_add=True)
    # modified_date = models.DateField(auto_now=True)


class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post)
    author = models.ForeignKey('User')
    content = models.TextField()
    # created_date = models.DateField(auto_now_add=True)
    # modified_date = models.DateField(auto_now=True)


class User(TimeStampedMixin):
    name = models.CharField(max_length=50)
    # created_date = models.DateField(auto_now_add=True)
    # modified_date = models.DateField(auto_now=True)
