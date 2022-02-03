"""
a classes module
"""
import json

class Person():
    """
    a person class
    """
    def __init__(self, name, ssn, address=""):
        self.name = name
        self._ssn = ssn
        self.address = address

    def get_ssn(self):
        """
        returns the SSN
        """
        return self._ssn

    def address_return(self, address):
        """
        returns the address
        """
        self.address = address
        return self.address

    def get_name(self):
        """
        returns the name
        """
        return f"Name: {self.name}"


class Address():
    """
    adds address
    """
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

    def return_adress(self):
        """
        returns the adress
        """
        return f"Address: {self.city} {self.state} {self.country}"

class Teacher(Person):
    """
    Teacher class
    """

    def __init__(self, name, ssn, courses=None):
        """
        init method
        """
        super().__init__(name, ssn, address="")
        self.courses = courses
        if self.courses is None:
            self.courses = []

    def add_course(self, course):
        """
        adds courses to the list
        """
        self.courses.append(course)

    def remove_course(self, course):
        """
        removes a course from the list
        """
        self.courses.remove(course)

    @classmethod
    def from_json(cls, filename):
        """
        opens json file as filename and returns the data
        """
        filename = json.load(open(filename))
        return cls(filename["name"], filename["ssn"], filename["courses"])

    @staticmethod
    def to_json(filename):
        """
        opens json file as file and returns a json formatted dict
        """
        filename = json.load(open(filename))
        json_object = json.dumps(filename, indent=4)
        return json_object

    def json_to_string(self):
        """
        makes json data into a formatted string and returns it
        """

        new_str = super().get_name() + " " + "SSN: " + super().get_ssn() + " Courses: "
        for course in self.courses:
            new_str += course + ", "
        json_string = new_str[:-2]
        return json_string



    def to_string(self):
        """
        To string
        """
        new_str = super().get_name() + " " + "SSN: " + super().get_ssn() + " Courses: "
        for course in self.courses:
            new_str += course + ", "
        return new_str[:-2]

class Student(Person):
    """
    Student class
    """
    def __init__(self, name, ssn, address="", courses_grades=None):
        """
        init method
        """
        super().__init__(name, ssn, address="")
        self.courses_grades = courses_grades
        if self.courses_grades is None:
            self.courses_grades = []
        self.classes = 0
        self.points = 0

    def add_course_grade(self, course, grade):
        """
        add course grades
        """
        if grade != "-":
            tuplevar = (course, grade)
            self.courses_grades += tuplevar


    def average_grade(self):
        """
        calculates the avr grade
        """
        for ggrade in self.courses_grades:
            if isinstance(ggrade, str):
                self.classes += 1
            elif isinstance(ggrade, int):
                self.points += ggrade
        avg = self.points / self.classes
        return avg
