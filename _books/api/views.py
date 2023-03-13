from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics

from _books.api.serializers import BookSerializer, CommentSerializer
from _books.models import Book, Comment

class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CommentListCreateApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BookDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


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
    



