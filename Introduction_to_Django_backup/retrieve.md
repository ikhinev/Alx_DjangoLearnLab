# Retrieve Operation

```python
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year
# Expected: ('1984', 'George Orwell', 1949)

