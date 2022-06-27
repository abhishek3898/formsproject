from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('forms/', views.form_page, name='registerd'),
    path("detail/<int:id>", views.details, name="detail_page"),
    path('edit/<int:id>',views.edit_page,name='edit_record'),
    path('delete/<int:id>',views.delete_page,name='delete_record'),
    path('js',views.new_js,name='jsfile'),
    # path("nameform/<int:id>", views.nameform_detail, name="nameformdetail_page"),
    # path('your-name/', views.MyFormView.as_view(), name='index'),
]