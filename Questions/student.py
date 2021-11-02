"""
#
# @File         : student.py
# @Created      : 2021-11-02 19:27
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  :
#
"""

from person import Person


class Student(Person):
    """ class: Student - inherits from Person """

    def __init__(self, fn="", ln="", major=""):
        Person.__init__(self, fn, ln)
        self.major = major

    def attendCollege(self):
        print(self.firstName + " " + self.lastName + "'s Major is " + self.major)

    def sitExams(self):
        print(self.firstName + " " + self.lastName + " did exams on " + self.major)

