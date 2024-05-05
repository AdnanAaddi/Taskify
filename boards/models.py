from django.db import models
from projects.models import Project , User

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100, default="Testing Board")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name
    
    

    def add_list(self, list_name):
        new_list = List.objects.create(name=list_name, board=self)
        return new_list 

class List(models.Model):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board, related_name='lists', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    opened_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='opened_cards')
    assigned_to = models.ManyToManyField(User, related_name='assigned_cards')
    labels = models.CharField(max_length=100)
    is_open = models.BooleanField(default=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f"  {self.user.username} comments  on the {self.card.title} "