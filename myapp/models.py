from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Signup(models.Model):
    ROLE = (
    ('faculty','faculty'),
    ('student', 'student'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=10,null=True)
    branch = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=20,choices=ROLE,null=True)
    profile_photo = models.FileField(null=True)

    def __str__(self):
        return self.user.username

class Notes(models.Model):
    BRANCHES = (
                ('Aerospace Engineering','Aerospace Engineering'),
                ('Chemical Engineering','Chemical Engineering'),
                ('Civil Engineering','Civil Engineering'),
                ('Computer Science & Engineering','Computer Science & Engineering'),
                ('Electrical Engineering','Electrical Engineering'),
                ('Mechanical Engineering','Mechanical Engineering'),
                ('Metallurgical Engineering & Materials Science','Metallurgical Engineering & Materials Science'),
    )    
    SUBJECTS = (
                ('Fundamentals of Computer Programming','Fundamentals of Computer Programming'),
                ('Data Structures','Data Structures'),
                ('Computer Networks','Computer Networks'),
                ('Object Oriented Programming','Object Oriented Programming'),
                ('Design and Analysis of Algorithms','Design and Analysis of Algorithms'),
                ('Mineral Processing','Mineral Processing'),
                ('Iron and Steel Making','Iron and Steel Making'),
                                                           
    )                   
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.DateTimeField(auto_now_add=True)
    branch = models.CharField(max_length=50, choices=BRANCHES)
    subject = models.CharField(max_length=50, choices=SUBJECTS)
    notesfile = models.FileField(null=True)
    filetype = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=15)
    likes = models.ManyToManyField(Signup, related_name="liked", null=True, blank=True)
    dislikes = models.ManyToManyField(Signup, related_name="disliked", null=True, blank=True)

    def __str__(self):
        return self.user.username+" "+self.status

# Model for OTP
class OTPModel(models.Model):
    user = models.EmailField(max_length=127)
    timestamp = models.DateTimeField(auto_now_add=True)
    otp = models.IntegerField()

    class Meta:
        verbose_name = 'OTP'