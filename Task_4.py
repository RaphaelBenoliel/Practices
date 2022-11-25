################################################################################
################################ Task__4 #######################################
################################################################################
class Student:
    def __init__(self, firstName, lastName):
        self.first = firstName
        self.last = lastName
        self.g = []

    def __add__(self, x):
        s = Student(self.first, self.last)
        s.g = list(self.g)
        if isinstance(x, int):
            s.g += [x, ]
            print('grade was succesfully added...')
            return s
        else:
            print('Cannot add this value, Grade should be integer...')
            return s

    def __str__(self):
        return f'Student name: {self.first} {self.last} Grade:{self.g}'

    def __lt__(self, other):
        if other.first < self.first:
            if other.last < self.last:
                return True
        return False

    def __le__(self, other):
        return (self.first, self.last) <= (other.first, other.last)

    def __eq__(self, other):
        return (self.first, self.last) == (other.first, other.last)

    def __ne__(self, other):
        return (self.first, self.last) != (other.first, other.last)

    def __ge__(self, other):
        return (self.first, self.last) >= (other.first, other.last)

    def __gt__(self, other):
        return (self.first, self.last) > (other.first, other.last)

    def gpa(self):
        gpa = 0
        for i in self.g:
            gpa += i
        if gpa != 0:
            return 'GPA: ' + str(gpa / len(self.g))
        return gpa

    def __len__(self):
        return len(self.g)

    def set_first(self, first):
        self.first = first

    def set_last(self, last):
        self.last = last

    def set_grade(self, grade):
        self.g = grade

    def get_first(self, first):
        return self.first

    def get_last(self, last):
        return self.last

    def get_grade(self, grade):
        return self.g


v = Student('Raphael', 'Benoliel')
r = Student('a', 'a')
y = Student('a', 'a')
print(v < r)
print(v != y)
v += 90
v += 92
v += 95
v += 100
print(v.gpa())
print(len(v))
