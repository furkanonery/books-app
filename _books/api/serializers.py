from rest_framework import serializers
from _books.models import Book, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['book']

class BookSerializer(serializers.ModelSerializer):
    Comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'