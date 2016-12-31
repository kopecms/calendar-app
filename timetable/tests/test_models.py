from django.test import TestCase
from timetable.models import Month, Task

from datetime import date

class MonthTest(TestCase):

    def test_default_month(self):
        month = Month()
        self.assertEqual(month.month, date.today().month)
