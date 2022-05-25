from django.db import models

class Class_Name(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    uni_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    def __str__(self):
        return self.name
        
class Student_Number(models.Model):
    class_name = models.ForeignKey(Class_Name, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    student_name = models.CharField(max_length=100)
    student_number = models.IntegerField(default=0)
    info = models.TextField(blank=True)
    def __str__(self):
        return self.student_name
    
