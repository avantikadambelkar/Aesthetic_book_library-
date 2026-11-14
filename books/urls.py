from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('library/', views.library_view, name='library'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    
    # Auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

