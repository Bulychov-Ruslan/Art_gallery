from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.name

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)
    reply = models.ForeignKey('Comment', on_delete=models.PROTECT, null=True, related_name='replies')
    content = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Комментарии'

    # def __str__(self):
    #     return '{}-{}'.format(self.item.name, str(self.user.username))









