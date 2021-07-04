from django.urls import path
from newapp import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('new/', views.new, name='new'),
    path('del_post/<int:id>', views.delete_post, name='dele_post'),
    path('<int:id>', views.edit_post, name='edit_post'),
    

    

 
]
