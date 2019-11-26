from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


from Library.Notes import views





urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('',include('Library.books.urls')),
    

    path('accounts/profile/', views.Home.as_view(), name=''),
    
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    
    
  
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    url('register', views.user_register, name='user_register'),
    path( 'logout',views.logout_user,name='logout'),
    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)