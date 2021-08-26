from django.db import models
from django.utils.html import format_html
# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)
    # PhotoFileName = models.FileField(upload_to='media/', null=True, blank=True)



    # def show_image(self): 
    #     if self.image:
    #         return format_html('<img src="%s" height="40px">' % self.image.url) 
    #     return ''
    # show_image.allow_tags = True 
    # show_image.short_description = 'PhotoFileName'
