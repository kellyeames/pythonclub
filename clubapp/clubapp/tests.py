from django.test import TestCase
from django.urls import reverse
from .models import Meeting, Resource, Event
from django.contrib.auth.models import User
import datetime
from .forms import ResourceForm

# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        type=Meeting(meetingtitle="meetingtitle")
        self.assertEqual(str(type), type.meetingtitle)
    
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class Resource(TestCase):
    def test_string(self):
        type=Resource(resourcename="resourcename")
        self.assertEqual(str(type), type.resourcename)
    
    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class ResourceForm_Test(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='user1', password='dog')
    
    def test_resourceForm(self):
        data={
            'resourcename' : 'computer',
            'resourcetype' : 'hardware',
            'resourceentrydate' : datetime.date(2019,5,28),
            'user' : self.user,
            'resourcedescription' : 'anything',
        }
        form = ResourceForm(data=data)
        self.assertTrue(form._is_valid())



