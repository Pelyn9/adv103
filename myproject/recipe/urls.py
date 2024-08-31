from django.urls import path
from .views import BookListView, AuthorListView, CategoryListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
