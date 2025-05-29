
from django.urls import path
from . import views

app_name = 'blog'  # 必须添加这行定义应用命名空间

urlpatterns = [
    path('', views.index, name='index'),  # 处理/blog/请求
    path('article/<int:article_id>/', views.article_page, name='article_page'),
    path('edit/<int:article_id>/', views.edit_page, name="edit_page"),
    path('edit_action/', views.edit_action, name="edit_action"),
]
