from django.urls import path
from _books.api import views as api_views

urlpatterns = [
    path('books/',api_views.BookListCreateApiView.as_view(), name='Book-List'),
    path('books/<int:pk>',api_views.BookDetailApiView.as_view(), name='Book-Detail'),

    path('books/<int:book_pk>/comment',api_views.CommentCreateApiView.as_view(), name='Create-Comment'),
    path('comments/<int:pk>',api_views.CommentDetailApiView.as_view(), name='Comment-Detail'),
    
    # path('comments/',api_views.CommentListCreateApiView.as_view(), name='Comment-List'),

]
