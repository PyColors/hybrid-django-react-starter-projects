from django.db import models


class Employee(models.Model):
    DEPARTMENT_CHOICES = (
        ('hr', 'Human Resources'),
        ('finance', 'Finance'),
        ('engineering', 'Engineering'),
        ('marketing', 'Marketing'),
        ('sales', 'Sales'),
    )
    title = models.CharField(max_length=120)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    content = models.TextField()

    def __str__(self):
        return self.title
