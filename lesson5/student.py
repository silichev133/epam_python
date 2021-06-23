class Student:
    def __init__(self, name, lastname, birthdate, gender, grade, speciality, course_number):
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
        
        if len(speciality) < 50:
            self.__speciality = speciality
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
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, sp):
        if len(speciality) > 50:
            self.__speciality = sp
        else:
            raise ValueError('Length more than 50')
    @property
    def course_number(self):
        return self.__course_number

    @course_number.setter
    def course_number(self, cn):
        self.__course_number = cn


