from django.db import models

class Add_students(models.Model):
    name = models.CharField(max_length=100)
    roll_num = models.IntegerField()
    email =models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
class MarkAttendance(models.Model):
    student = models.ForeignKey(Add_students,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=100,choices=[('Present', 'Present'), ('Absent', 'Absent')])
    
    def __str__(self):
        return self.student