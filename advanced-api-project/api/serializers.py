from rest_framework import serializers
from .models import Author, Book
<<<<<<< HEAD
from datetime import datetime
=======
>>>>>>> fa039cb (Initial commit: models and serializers)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
<<<<<<< HEAD
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
=======
        fields = ['title', 'publication_year', 'author']

    # Custom validation for the publication_year
    def validate_publication_year(self, value):
        if value > 2025:  # You can adjust this to the current year or any logic
>>>>>>> fa039cb (Initial commit: models and serializers)
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
=======
    books = BookSerializer(many=True, read_only=True)  # Nested BookSerializer

    class Meta:
        model = Author
        fields = ['name', 'books']
>>>>>>> fa039cb (Initial commit: models and serializers)
