from django.contrib import admin
from .models import Departments ,Employees
# Register your models here.
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['DepartmentId', 'DepartmentName']
    list_filter = ['DepartmentName']
    search_fields = ['DepartmentId', 'DepartmentName']

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName']
    list_filter = ['EmployeeName']
    search_fields = ['EmployeeId', 'EmployeeName']





admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Employees, EmployeesAdmin)





