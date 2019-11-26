
from django.urls import path,include

from django.conf.urls.static import static
from django.conf.urls import url


from Library.books import views

urlpatterns = [
    
    
    path('upload/', views.upload, name='upload'),
    
    
    
    path('notes/', views.books_list, name='books_list'),
    
    path('notes/upload/', views.upload_book, name='upload_notes'),
    
]

