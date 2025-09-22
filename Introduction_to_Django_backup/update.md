# Update Operation

```python
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(pk=b.pk).title
# Expected: 'Nineteen Eighty-Four'

