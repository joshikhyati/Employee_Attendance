
from django.db import models

from django.contrib.auth.models import User

class Employee(models.Model):
    blood_choices =  (
        ('type', 'AB+'),
        ('type', 'AB-'),
        ('type', 'A+'),
        ('type', 'A-'),
        ('type', 'B+'),
        ('type', 'B-'),
        ('type', 'O+'),
        ('type', 'O-'),
        )
    fullname=models.CharField(max_length=100)
    fathername=models.CharField(max_length=50)
    mothername=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    emergencynumber=models.IntegerField()
    bloodgroup=models.CharField(max_length=20,choices=blood_choices,default='AB+')
    address=models.TextField()
    position=models.CharField(max_length=100)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    image =  models.ImageField(upload_to='Image',null=True)
    code=models.IntegerField()
    # code=models.UUIDField(primary_key=True,default=str(uuid.uuid4().int)[:4], editable=False)

    def __str__(self):
        return self.user_id.username

class Attendance(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    date=models.DateField()

    class Meta:
        unique_together = ('employee', 'date')


    def __str__(self):
        return self.employee.user_id.username

class Timespend(models.Model):
    attendance=models.ForeignKey(Attendance, on_delete=models.CASCADE)
    punchin=models.DateTimeField(blank=True, null=True)
    punchout=models.DateTimeField(blank=True, null=True)
    

    class Meta:
        get_latest_by = ['attendance']
     
        
        
    def __str__(self):
        return 'attendance'
