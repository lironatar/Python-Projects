# url that go to the views.py in this folder ( main )

from django.urls import path
# import from this folder the views
from . import views


#paths to the views
#path('url path ', go the views.py and to the function named 'index', name 'index' )
#the path in mysite - urls.py -> / here
# for example in the mysite urls home/   and here the pattern 
urlpatterns = [
    #path('start/', views.index, name='index'),
    path("<str:name>", views.index ,name='index'),
    path("<int:id>", views.index)
    #      id / string : 
]
