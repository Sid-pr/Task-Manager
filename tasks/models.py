from django.db import models

class Task(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()

    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Completed', 'Completed')
        ]
    )

    remarks = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title