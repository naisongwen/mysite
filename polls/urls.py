from django.urls import path

from . import views

app_name="polls"

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/category
    path('<int:category_id>/category', views.category, name='category'),
    # ex: /polls/5/sub_category
    path('<int:sub_category_id>/subcategory', views.subcategory, name='subcategory'),
    # ex: /polls/5/article
    path('<int:article_id>/article', views.article_detail, name='article_detail'),
    # ex: /polls/5/product/
    path('<int:product_id>/product/', views.product_detail, name='product_detail'),

    path('consult/', views.consult, name='consult'),
    path('complete_consult', views.complete_consult, name='complete_consult'),
]
