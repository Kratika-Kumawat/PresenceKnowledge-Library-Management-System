from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=30)
    enroll=models.CharField(max_length=20)
    branch = models.CharField(max_length=10)
    sem=models.IntegerField()
    year = models.CharField(max_length=30)
    mob=models.CharField(max_length=11)
    def __str__(self):
        return self.name+" "+self.branch+" "+self.year
    
class Library(models.Model):
    book=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    language=models.CharField(max_length=10)
    description=models.TextField()
    publisher=models.CharField(max_length=30)
    paperback=models.CharField(max_length=10)
    sid=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.book
    
