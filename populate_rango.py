import os
import django

# 設置 Django 環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')#ensure that our script can access the ORM and models.py
django.setup()

# 導入 Rango 應用的模型
from rango.models import Category, Page

def populate():
    """
    這個函數負責向數據庫中填充初始數據
    """
    # 定義 Python 相關網頁
    python_pages = [
        {'title': 'Official Python Tutorial', 'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist', 'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes', 'url':'http://www.korokithakis.net/tutorials/python/'}
    ]

    # 定義 Django 相關網頁
    django_pages = [
        {'title':'Official Django Tutorial', 'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks', 'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django', 'url':'http://www.tangowithdjango.com/'}
    ]

    # 其他框架相關網頁
    other_pages = [
        {'title':'Bottle', 'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask', 'url':'http://flask.pocoo.org'}
    ]

    # 定義類別 (Categories)
    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
    }

    # 遍歷 cats 字典，創建類別和網頁
    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data['views'], cat_data['likes'])  # 創建類別
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])  # 創建對應網頁

    # 確認數據已經添加成功
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    """
    添加頁面
    """
    p = Page.objects.get_or_create(category=cat, title=title)[0] #use get_or_create() method , if object exist-return object otherwise create new object and return
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name,views=0,likes=0):
    """
    添加類別
    """
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# 執行腳本
if __name__ == '__main__':#to ensure populate() only execute when this script running rather than other python models
    print('Starting Rango population script...')
    populate()