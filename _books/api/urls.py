from django.urls import path
from _books.api import views as api_views

urlpatterns = [
    path('books/',api_views.BookListCreateApiView.as_view(), name='Book-List'),
    path('comments/',api_views.CommentListCreateApiView.as_view(), name='Comment-List'),
]
