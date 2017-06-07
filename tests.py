import unittest
from test import support
import peewee
import datetime
import sys
import os
import worklogdb
from worklogdb import Employee

employees = Employee.select().order_by(Employee.date_time.desc())


class DatabaseModelTests(unittest.TestCase):

    def test_class_str_method(self):
        entry = Employee(name="Chico", task_name="Sing a song", date_time=peewee.DateTimeField(default=datetime.datetime.now), notes="na")
        assert 'Chico' in str(entry)





class SearchTests(unittest.TestCase):

    def setUp(self):
        # Datetime date object
        self.chico_date = datetime.date(2017, 6, 7)

        # Temporary 'self.chico' instance with self.chico_date as the date_time of post
        self.chico = Employee(name="Chico Buarque", task_name="Sing a song", date_time=self.chico_date, minutes=30, notes="A note here")
        self.chico.save()

    def test_name_search(self):
        self.assertIn(self.chico, worklogdb.name_query('chico buarque'))

    def test_time_search(self):
        self.assertIn(self.chico, worklogdb.time_query('30'))

    def test_term_search(self):
        self.assertIn(self.chico, worklogdb.term_db_query('note'))

    def test_date_search(self):
        # Assert if a call of date_query() containing a date object reflecting today's date
        self.assertIn(self.chico, worklogdb.date_query(self.chico_date))

    def tearDown(self):
        self.chico.delete_instance()

class DisplayDatesTest(unittest.TestCase):

    def setUp(self):
        self.dates = ['06/07/2017']

    def test_display_dates(self):
        assert '06/07/2017' in worklogdb.display_dates()

class DisplayAllRecordsTest(unittest.TestCase):

    def setUp(self):
        self.chico = Employee(name="Chico Buarque", task_name="Sing a song", minutes=30, notes="A note here")
        self.chico.save()

    def test_printer(self):
        with support.captured_stdout() as stdout:
            queryset = worklogdb.name_query('chico buarque')
            worklogdb.printer(queryset, paginated=False)
            assert "Chico" in stdout.getvalue()

    def tearDown(self):
        self.chico.delete_instance()


if __name__ == '__main__':
    unittest.main()




################################################################################

    # def test_name_search(self):
    #     with support.captured_stdout() as stdout:
    #         name_results = employees.where(Employee.name.contains('adam'))
    #         worklogdb.printer(name_results)
    #         assert 'a' in stdout.getvalue()



        # with support.captured_stdin() as stdin, support.captured_stdout() as stdout:            
            # stdin.write("b\n")
            # stdin.seek(0)