class Student():
    """ Student Class is used to keep the track of student information as a new
        student enters the school """

    number_of_students = 0          #static variable storing number of student admitted in school

    def __init__(self,name = "No Name Entered",age = 0,sec='A',percent=0.00):
        self.__name = name
        self.__age = age
        self.__sec = sec
        self.__percent = percent
        self.__id = Student.number_of_students
        Student.number_of_students += 1

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getSec(self):
        return self.__sec

    def getPercent(self):
        return self.__percent

    def getId(self):
        return self.__id

    def setName(self,name):
        self.__name = name
        return

    def setAge(self,age):
        self.__age = age
        return

    def setSec(self,sec):
        self.__sec = sec
        return

    def setPercent(self,percent):
        self.__percent = percent
        return

    def __del__(self):
        Student.number_of_students -= 1
        return
