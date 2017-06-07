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
        entry = Employee(name="Jorge", task_name="Sing a song", date_time=peewee.DateTimeField(default=datetime.datetime.now), notes="na")
        assert 'Jorge' in str(entry)


# class SearchTests(unittest.TestCase):

#     def test_name_search(self):
#         with support.captured_stdin() as stdin, support.captured_stdout() as stdout:
#             stdin.write('adam cameron\n')
#             stdin.seek(0)
#             worklogdb.name_search()
#             assert 'adam' in 





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