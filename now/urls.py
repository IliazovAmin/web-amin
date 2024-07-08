# speedcubing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('save_time/', views.save_time, name='save_time'),
    path('best_results/', views.best_results, name='best_results'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('timer/', views.timer, name='timer'),
    path('time/', views.time, name='time'),
    path('logout/', views.logout_view, name='logout'),
    path('algor/', views.algor, name='algor'),
    path('', views.glav, name='glav'),
    path('we/', views.we, name='we'),
    path('up/', views.up, name='up'),
    path('best-results/delete/<int:result_id>/', views.delete_result, name='delete_result'),
]
