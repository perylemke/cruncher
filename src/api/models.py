from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=300, unique=True)
    profile_page = models.CharField(max_length=2048)
    twitter_page = models.CharField(max_length=2048, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    url = models.CharField(max_length=2048)
    published_date = models.DateTimeField()
    thumbnail_url = models.TextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
