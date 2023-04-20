from django.db import models


class Article(models.Model):
    article_id = models.IntegerField(default=0)
    year = models.IntegerField()
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=30)
    link = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.article_id}, {self.category}"


class Author(models.Model):
    name = models.CharField(max_length=70)
    author_id = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.author_id}, {self.name}"


class Connection(models.Model):
    article_id = models.IntegerField(default=0)
    author_id = models.IntegerField(default=0)

    def __str__(self):
        return f"Author ({self.author_id}) - Article({self.article_id})"

