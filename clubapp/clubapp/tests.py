from django.test import TestCase
from django.urls import reverse
from .models import Meeting, Resource, Event
from django.contrib.auth.models import User

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



