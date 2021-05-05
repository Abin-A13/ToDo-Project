
from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name='display'),
    # path('details',views.details, name='details'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:fid>/', views.update, name='update'),
    path('cbvlist/', views.Tasklist.as_view(), name='listview'),
    path('cbvdetail/<int:pk>/', views.Taskdetails.as_view(), name='detail'),
    path('cbvupdate/<int:pk>/', views.Taskupate.as_view(), name='updateto'),
    path('cbvdelete/<int:pk>/', views.Taskdelete.as_view(), name='deleteto')
]