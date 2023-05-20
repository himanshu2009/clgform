from django.db import models

import datetime


# Create your models here.


class Student(models.Model):
    id=models.IntegerField(primary_key=True)  
    name=models.CharField(max_length=200,default='')
    regno=models.IntegerField(default=0)
    # yoj=models.DateField(_("Date"), default=datetime.date.today)
    phno=models.IntegerField(default=0)
    email=models.EmailField()
    address=models.TextField(default='')
    nooftranscript=models.IntegerField()
    deptname=models.CharField(max_length=200,default='-')

class Subject(models.Model):
    id=models.IntegerField(primary_key=True)
    subname=models.CharField(max_length=200)
    subcode=models.CharField(max_length=200)
    credit=models.IntegerField()
    sem_id=models.IntegerField()


class Grade(models.Model):
    id=models.IntegerField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE ,default=0)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE,default=0)
    grade=models.CharField(max_length=200)




   





















   





