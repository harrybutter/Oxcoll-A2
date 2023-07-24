import datetime # we will use this for date objects

class Person:  # by convention starts with an initial capital letter

    # define your CLASS attributes here
    species = "homo sapiens"
    
    # the CONSTRUCTOR method - has to have the name __init__
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name  # an instance ATTRIBUTE
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        print("created a new Person object:",self.name," ",self.surname)
    
    # another METHOD - like all methods must have "self" as the first argument
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

# endclass Person



    
def main():
    # creating an INSTANCE of a class - an OBJECT called Jane
    # this is called INSTANTIATION of a class
    Jane = Person( "Jane","Smith",datetime.date(1992, 3, 12), "12 Short Street","01867 45678", "jane.smith@example.com")
    
    # creating a second Person object
    Jack = Person("Jack","Smith",datetime.date(1990, 6, 5), "12 Short Street","01867 45678", "jack.smith@example.com")

    family=[Jane,Jack] # a list of objects
   
    for person in family:
        print("Name: ",person.name) # display the name attribute
        print("Email:",person.email) # display the email address attribute
        print("Age:",person.age())  # display the value returned by the age() method
        print("Species:",Person.species) # use the class name to refer to class attributes
        

if __name__ == "__main__":
    main()