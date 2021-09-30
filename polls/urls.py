from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/question_details/', views.get_details, name='details'),
    path('storten_path/<path:url>', views.shorten_path, name='bitly'),
    path('redirect/<str:token>/', views.redirect_url, name='redirect_url')
]
