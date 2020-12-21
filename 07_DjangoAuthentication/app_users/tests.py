from django.test import TestCase

# Create your tests here.
import datetime
if datetime.datetime.now().hour >= 23 or datetime.datetime.now().hour <= 5:
    print('Слишком поздно')