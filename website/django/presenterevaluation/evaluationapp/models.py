from django.db import models
from django.utils import timezone

class AppAdmin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return "ID: %d Username: %s Password: %s" % (self.id, self.username, self.password)

class AppAdminLog(models.Model):
    appAdminUser = models.ForeignKey('AppAdmin', on_delete=models.CASCADE)
    last_logged_in = models.CharField(max_length=100)
    last_logged_out = models.CharField(max_length=100, blank=True, null=True)

class Professor(models.Model):
    username = models.CharField(max_length=70)
    mailId = models.CharField(max_length=70)
    accesscode = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    recovery_answer = models.CharField(max_length=20)
    created_on = models.DateTimeField(default=timezone.now)
    last_updated_on = models.DateTimeField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=70)
    middle_name = models.CharField(max_length=70, blank=True, default='')
    last_name = models.CharField(max_length=70)
    phone_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "ID: %d First Name: %s Middle Name: %s Last Name: %s Phone Number: %s" % (self.id, self.first_name, self.middle_name, self.last_name, self.phone_number)

class ProfessorVerify(models.Model):
    username = models.CharField(max_length=70)

class ProfessorLog(models.Model):
    professorUser = models.ForeignKey('Professor', on_delete=models.CASCADE)
    last_logged_in = models.CharField(max_length=100)
    last_logged_out = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.professorUser


class Student(models.Model):
    username = models.CharField(max_length=70)
    mailId = models.CharField(max_length=70)
    password = models.CharField(max_length=20)
    recovery_answer = models.CharField(max_length=20)
    created_on = models.DateTimeField(default=timezone.now)
    last_updated_on = models.DateTimeField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=70)
    middle_name = models.CharField(max_length=70, blank=True, default='')
    last_name = models.CharField(max_length=70)
    phone_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.username, self.password)

class StudentLog(models.Model):
    studentUser = models.ForeignKey('Student', on_delete=models.CASCADE)
    last_logged_in = models.CharField(max_length=100)
    last_logged_out = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.studentUser

class Presenter(models.Model):
    reviewedfor = models.CharField(max_length=70)
    evaluationType = models.CharField(max_length=70)
    comments = models.CharField(max_length=1000)
    score = models.IntegerField(blank=True, null=True)
    reviewedby = models.CharField(max_length=70)

    def __str__(self):
        return "%s %s %s %s" % (self.reviewedfor, self.evaluationType, self.comments, self.reviewedby)

class PresenterNew(models.Model):
    reviewedby = models.CharField(max_length=70)
    reviewedfor = models.CharField(max_length=20, default='')
    eva = models.CharField(max_length=70)
    com = models.CharField(max_length=500)
    score = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    last_updated_on = models.DateTimeField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "ID: %d Username: %s Password: %s" % (self.id, self.reviewedby, self.eva)

