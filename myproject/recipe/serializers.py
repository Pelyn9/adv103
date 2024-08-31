from rest_framework import serializers
from .models import Book, Author, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'gender']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'author', 'category', 'created_at']
