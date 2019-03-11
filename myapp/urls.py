

from django.urls import path
from . import views
app_name='myapp'
urlpatterns = [
  
    path("",views.home,name='home'),
    path("books/",views.books_list,name='books_list'),
    path("upload/",views.upload_book,name='upload_book'),
    path("login/",views.login_user,name='login_user'),
    path("logout/",views.logout_user,name='logout_user'),
    path("register/",views.register_user,name='register_user'),
    path("delete/<int:pk>",views.delete_book,name='delete_book'),
]
