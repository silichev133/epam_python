import string
import random

class Student:
    def __init__(self, name, lastname, birthdate, gender, grade, spec, course_number):
        if len(name) < 25:
            self.__name = name
        else:
            raise ValueError('Length more than 25')

        if len(lastname) < 50:
            self.__lastname = lastname
        else:
            raise ValueError('Length more than 50')

        self.__birthdate = birthdate

        if gender == 'M' or gender == 'F':
            self.__gender = gender
        else:
            raise ValueError('Gender not M or F')

        if grade > 0 and grade < 11:
            self.__grade = grade
        else:
            raise ValueError('Grade more than 10 or less than 0')
        
        if len(spec) < 50:
            self.__spec = spec
        else:
            raise ValueError('Length more than 50')

        self.__course_number = course_number


    @property
    def name(self):
        return self.__name

    @property
    def lastname(self):
        return self.__lastname

    @property
    def birthdate(self):
        return self.__birthdate
    
    @property
    def gender(self):
        return self.__gender

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, gr):
        if gr > 0 and gr < 11:
            self.__grade = gr
        else:
            raise ValueError('Grade more than 10 or less than 0')

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, sp):
        if len(self.__spec) < 50:
            self.__spec = sp
        else:
            raise ValueError('Length more than 50')

    @property
    def course_number(self):
        return self.__course_number

    @course_number.setter
    def course_number(self, cn):
        self.__course_number  = cn

students = []

with open("students.dat", "r", encoding="utf-8-sig") as f:
    lines = f.readlines()
    for line in lines:
        new_line = line.strip().split(':::')
        new_line[4] = int(new_line[4])
        new_line[6] = int(new_line[6])
        students.append(new_line)

class Student_login_pwd(Student):
    def __init__(self, name, lastname, birthdate, gender, grade, spec, course_number):
        super().__init__(name, lastname, birthdate, gender, grade, spec, course_number)
        
        #self.__login = self.name[0][0].lower() + self.lastname[1].lower()

    @property
    def pwd(self):
        random_string = string.ascii_lowercase + string.ascii_uppercase + string.digits
        rand_int = random.randint(6, 9)
        pwd = ''

        for i in range(rand_int):
            pwd += random.choice(random_string)

        return pwd
    @property
    def login(self):
        return self.name[0][0].lower() + self.lastname.lower()

#loop to create multiple instances
ext_students = []
for i in range(len(students)):
    ext_students.append(Student_login_pwd(*students[i]))

#create ext_students.dat file with new information 
with open("ext_students.dat", 'a') as f:
    for i in range(len(ext_students)):
        f.write(ext_students[i].name + '::' + ext_students[i].lastname + '::' + ext_students[i].birthdate + '::' + ext_students[i].gender
                + '::' + str(ext_students[i].grade) + '::' + ext_students[i].spec + '::' + str(ext_students[i].course_number)
                + '::' + ext_students[i].login + '::' + ext_students[i].pwd + '\n')
