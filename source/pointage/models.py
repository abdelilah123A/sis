from django.db import models
#from lms_teacher import Teacher
#from lms_student import Course,Student

# Create your models here.
class Class_session(models.Model):
    session_id=models.PrimaryKey(
        max_length=50,
        null=False,
        on_delete=models.SET_NULL,
       
       )
    session_date = models.DateField(
          max_length=50
    
        )
    start_time= models.TimeField(
          max_length=50
    
        )
    end_time = models.TimeField(
          max_length=50
    
        )
    status= models.CharField(
              
        max_length=50,
        null=True,
        default='planned',
        verbose_name='Status',
       
        
    
        )
    comment= models.CharField(
          max_length=50
    

        )
    teacher_id=models.ForeignKey(
        "lms_teacher.Teacher",
        max_length=50,
        null=True,
        verbose_name='teacherId',
        on_delete=models.SET_NULL,
        
    )
    course_id=models.ForeignKey(
        "lms_student.Course",
        max_length=50,
        null=True,
       
        verbose_name='courseId',
        on_delete=models.SET_NULL,
       
    )
class Attendance(models.Model):
    session_id = models.ForeignKey(
        Class_session,
    )
    student_id = models.ForeignKey(
        "lms_student.Student",
       )
   
    class Meta:
       primary_key = ('session_id','student_id')
        
   
    
   