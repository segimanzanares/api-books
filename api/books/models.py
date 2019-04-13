from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    publisher = models.CharField(max_length=100, blank=False, null=False)
    published_date = models.DateField(null=False)
    description = models.TextField(blank=True, null=True, default='')
    language = models.CharField(max_length=2, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    deleted_at = models.DateTimeField(auto_now=False, null=True)

    class Meta:
        ordering = ('created_at',)

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    deleted_at = models.DateTimeField(auto_now=False, null=True)

    class Meta:
        ordering = ('created_at',)
