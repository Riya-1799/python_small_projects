# Create multiple inheritance on teacher,student and youtuber.
# Q. if we have created teacher and now one student joins master degree with becoming teacher then what??
#
# Ans :  just make subclass from  teacher so that student will become teacher

class teacher:
    def teacher_action(self):
        print("I can Teach")

class student:
    def student_action(self):
        print("I can code")

class youtuber:
    def youtuber_action(self):
        print("I can code and Teach")


class person(teacher,student,youtuber):
    pass

people = person()
people.student_action()
people.youtuber_action()
people.teacher_action()
