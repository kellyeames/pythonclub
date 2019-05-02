from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    resourceid=models.CharField(max_length=255)
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    location=models.CharField(max_length=255)
    agenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meeting_id=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    meetingtext=models.TextField()

    def __str__(self):
        return self.meetingtext
    
    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    resourceentrydate=models.DateField()
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField(max_length=255)

    def __str__(self):
        return self.resourcename
    
    class Meta: 
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventid=models.CharField(max_length=255)
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'
