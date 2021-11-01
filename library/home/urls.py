from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.main,name="main"),
    path('addstudent', views.addstudent,name="addstudent"),
    path('addbook', views.addbook,name="addbook"),
    path('borrowbook/<int:myid>', views.borrowbook,name="borrowbook"),
    path('studentinfo', views.studentinfo,name="studentinfo"),
    path('updatebook/<int:myid>', views.updatebook,name="updatebook"),
    path('deletebook', views.deletebook,name="deletebook"),
    path('info/<int:myid>', views.info,name="info"),
    path('delstudent/<int:myid>', views.delstudent,name="delstudent"),
]