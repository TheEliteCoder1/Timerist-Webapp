from django.db import models

# Create your models here.

class Todo(models.Model):
    STATUS_TYPES = (
        ('Incomplete', 'Incomplete ❌'),
        ('Completed', 'Completed ✔️'),
        ('Overdue', 'Overdue ⌛')
    )   

    task = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=200, null=True, choices=STATUS_TYPES, default='Incomplete ❌')
    due_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task