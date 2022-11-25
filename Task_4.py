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
        s.g = list(self.g) + [x, ]
        return s

    def __str__(self):
        return f'Student name: {self.first} {self.last}'

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


v = Student('Raphael', 'Benoliel')
r = Student('a', 'a')
y = Student('a', 'a')

print(v < r)
print(v != y)
