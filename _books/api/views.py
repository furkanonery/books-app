# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404

from _books.api.serializers import BookSerializer, CommentSerializer
from _books.models import Book, Comment

class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CommentCreateApiView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        #  path('books/<int:book_pk>/comment',api_views.CommentCreateApiView.as_view(), name='Create-Comment'),
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        serializer.save(book=book)

class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    


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
    



