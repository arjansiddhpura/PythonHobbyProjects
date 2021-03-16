#class IntSet(object):
#    """An intSet is a set of integers"""
#    #Information about the implementation (not the abstraction)
#    #Value of the set is represented by a list of ints, self.vals.
#    #Each int in the set occurs in self.vals exactly once.
#
#    def __init__(self):
#        """Create an empty set of integers"""
#        self.vals = []
#
#    def insert(self, e):
#        """Assumes e is an integer and inserts e into self"""
#        if e not in self.vals:
#            self.vals.append(e)
#
#    def member(self, e):
#        """Assumes e is an integer
#        Returns True if e is in self, and False otherwise"""
#        return e in self.vals
#
#    def remove(self, e):
#        """Assumes e is an integer and removes e from self
#        Raises ValueError if e is not in self"""
#        try:
#            self.vals.remove(e)
#        except:
#            raise ValueError(str(e) + ' not found')
#
#    def getMembers(self):
#        """Returns a list containing the elements of self.
#        Nothing can be assumed about the order of the elements"""
#        return self.vals[:]
#
#    def __str__(self):
#        """Returns a string representation of self"""
#        self.vals.sort()
#        result = ''
#        for e in self.vals:
#            result = result + str(e) + ','
#        return '{' + result[:-1] + '}' #-1 omits trailing comma
#
#s = IntSet()
#s.insert(6)
#s.insert(4)
#print(s)


#Class Person
import datetime

class Person(object):

    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """Returns self's full name"""
        return self.name

    def getLastName(self):
        """Returns self's last name"""
        return self.lastName

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate"""
        self.birthday = birthdate

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are
        compared."""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
       
    
    def __str__(self):
        """Returns self's name"""
        return self.name

#Class MIT Person
class MITPerson(Person):

    nextIdNum = 0 #identification number

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def isStudent(self):
        return isinstance(self, Student)

    def __lt__(self, other):
        try:
            return self.idNum < other.idNum
        except AttributeError:
            print(MITPerson.getName(self) + ' has no ID Number. Get him one!')  

#Class Student 
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

class Grad(Student):
    pass

#me = Person('Arjan Siddhpura')
#him = Person('Barack Obama')
#her = Person('Madonna')
#print(him.getLastName())
#him.setBirthday(datetime.date(1961, 8, 4))
#her.setBirthday(datetime.date(1958, 8, 16))
#print(him.getName(), 'is', him.getAge(), 'days old.')
#people = [me, him, her]
#people.sort()
#people.reverse()
#for p in people:
#    print(p)

p1 = MITPerson('Mark Guttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')
p5 =    ('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)

#print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
#print('And ' + str(p2) + '\'s id number is ' + str(p2.getIdNum()))
print(p5, 'is a graduate student is', type(p5) == Grad)
print(p5, 'is an undergraduate student is', type(p5) == UG)
print(p5, 'is a student is', p5.isStudent())
print(p3, 'is a student is', p3.isStudent())
#print('p4 < p1 = ', p4 < p1)
#print('p1 < p4 = ', p1 < p4)