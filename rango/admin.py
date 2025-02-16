from django.contrib import admin
from rango.models import Category,Page

#註冊category and page 讓他們出現在admin
class PageAdmin(admin.ModelAdmin):
    list_display=('Title','category','url')

admin.site.register(Category)
admin.site.register(Page)
# Register your models here.
