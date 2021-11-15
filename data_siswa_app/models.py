from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.
class CustemUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Staff"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)


class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustemUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    update_ad=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustemUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Subjects(models.Model):
    id=models.AutoField(primary_key=255)
    subject_name=models.CharField(max_length=255)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    staff_id=models.ForeignKey(Staff, on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustemUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    profile_pic=models.CharField(max_length=255)
    address=models.TextField()
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateTimeField(auto_now_add=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class LeaveReportStudents(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_masage=models.TextField()
    leave_status=models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class LeaveReportStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_masage=models.TextField()
    leave_status=models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class FeedbackStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_replay=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class FeedbackStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_replay=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class NotificationStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students, on_delete=models.CASCADE)
    message=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class NotificationStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff, on_delete=models.CASCADE)
    message=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
