#
#
#

from django.urls import path
from . import views

app_name='kakeibo'

urlpatterns = [
   path('kakeibo_list/', views.KakeiboListView.as_view(), name='kakeibo_list'),
   path('kakeibo_create/', views.KakeiboCreatView.as_view(), name='kakeibo_create'),
   path('kakeibo_done/', views.create_done, name='create_done'),
   path('update/<int:pk>/', views.KakeiboUpdateView.as_view(), name='kakeibo_update'),
   path('update_done/', views.update_done, name='update_done'),
   path('delete/<int:pk>/', views.KakeiboDeleteView.as_view(), name='kakeibo_delete'),
   path('delete_done/', views.delete_done, name='delete_done'),
   path('circle/', views.show_circle_grahp, name='kakeibo_circle'),
   path('line/', views.show_line_graph, name='kakeibo_line'),
   path('', views.index, name='index'),

]
