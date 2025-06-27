from django.db import models
from accounts.models import MemberProfile

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=10, unique=True, primary_key=True)
    quantity = models.IntegerField()
    available_count = models.IntegerField()


    class Meta:
        ordering = ['title']

        
    def __str__(self):
        return self.title

class IssueRecord(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    is_returned = models.BooleanField(default=False)
    fine = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.member.user.username} - {self.book.title}"




