"""
#
# @File         : lecturer.py
# @Created      : 2021-11-02 19:44
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    :
#
# @Description  :
#
"""

from person import Person


class Lecturer(Person):

    def __init__(self, fn="", ln=""):
        Person.__init__(self, fn, ln)

    def markCA(self):
        print("Mark CA")

    def lecturer(self):
        print(self.firstName + self.lastName)
