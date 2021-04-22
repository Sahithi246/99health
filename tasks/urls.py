from django.urls import path
from . import views

urlpatterns = [
    path('',views.create,name='create'),
    #path('',views.posts,name='posts')
    path('all',views.all,name='all'),
    path('update/<id>/',views.update,name='update'),
    path('deleteid/<id>/',views.deleteid,name='deleteid'),
    path('show/<id>/',views.show,name='show')

]
