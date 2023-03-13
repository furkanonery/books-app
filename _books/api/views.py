from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from _books.api.serializers import BookSerializer, CommentSerializer
from _books.models import Book, Comment

# from rest_framework import permissions
from _books.api import permissions

class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]

class BookDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]

class CommentCreateApiView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        #  path('books/<int:book_pk>/comment',api_views.CommentCreateApiView.as_view(), name='Create-Comment'),
        commenter = self.request.user
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        if Comment.objects.filter(book=book, commenter=commenter).exists() == False:
            serializer.save(book=book,commenter=commenter)
        else:
            raise ValidationError('Bir kitaba sadece bir yorum yapabilirsiniz.')

class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsCommenterOrReadOnly]


    


# class CommentListCreateApiView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# class BookListCreateApiView(ListModelMixin, CreateModelMixin, GenericAPIView):

#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self,request,*args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class CommentListCreateApiView(ListModelMixin, CreateModelMixin, GenericAPIView):

#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     def get(self,request,*args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    



