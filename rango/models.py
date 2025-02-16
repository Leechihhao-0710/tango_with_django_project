from django.db import models

# Create your models here.
#create category model
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)  # 分類名稱
    views = models.IntegerField(default=0)  # 訪問次數
    likes = models.IntegerField(default=0)  # 喜歡數量
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# 創建頁面（Page）模型
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 一對多關係
    title = models.CharField(max_length=128)  # 頁面標題
    url = models.URLField()  # 頁面 URL
    views = models.IntegerField(default=0)  # 頁面瀏覽數

    def __str__(self):
        return self.title
