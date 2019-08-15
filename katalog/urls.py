from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/',views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetail_View.as_view(),name='book-detail'),
    path('book/',views.AuthorListView.as_view(), name='author'),
    path('book/<int:pk>', views.AuthorDetailView.as_view(),name='author-detail'),
]