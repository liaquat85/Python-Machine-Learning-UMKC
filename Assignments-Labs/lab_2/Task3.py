
class Airport:

    def __init__(self,dp, dt):
        self.dp = dp
        self.dt = dt

    def set(self,dept,dest):
        self.dp = dept
        self.dt = dest

    def get(self):
        return (str("The dp airport is ")+self.dp+str(" The dt airport is ")+self.dt)

#K = Airport("Karachi","Lahore")
#print(K.get())

class Person:

    def __init__(self,n,p):
        self.n = n

        self.p = p

    def set(self,n,p):
        self.n = n

        self.p = p

    def get(self):
        return (str("Name ")+self.n+str(" Phone number: ")+self.p)

#P1 = Person("Ali",23,9133257638)
#print(P1.get())

class Employee:

    def __init__(self,n,p,dept,ID):
        Person.__init__(self,n,p)
        self.dept = dept
        self.ID = ID

    def set(self,ID,dept):
        self.ID = ID
        self.dept = dept

    def get(self):
        return ("\n"+
                str("Name: ")+self.n+"\n" +
                str("Phone number: ")+self.p+"\n" +
                str("ID: ")+self.ID+"\n" +
                str("Department: ")+self.dept+"\n")

#E1= Employee("Hassan",23,9144354567,"Aviation",5216)

class Passenger:

    def __init__(self,n,p,dp,dt,pn):
        Person.__init__(self,n,p)
        Airport.__init__(self,dp,dt)
        self.pn = pn

    def set(self,pn):
        self.pn=pn

    def get(self):
        return ("\n"+
                str("Name: ")+self.n+ "\n" +
                str("Phone number: ")+self.p+ "\n" +
                str("Passenger number: ")+self.pn+ "\n" +
                str("Destination: ")+self.dt+ "\n" +
                str("Departure: ")+self.dp+
                "\n")



#Pa1 = Passenger("Hassan", 23, 9144354567, "Karachi","Lahore",123)
#print(Pa1.get())

class Flight:
    
    def __init__(self,dt,dp,fn):
        Airport.__init__(self,dp,dt)
        self.fn=fn

    def set(self, fn):
        self.fn = fn

    def get(self):
        return (str("The flight number is ")+self.fn+str(" destination is ")+self.dt+str(" departuring from ")+self.dp)

#f1= Flight("Karachi","Lahore","PK103")
#print(f1.get())


while True:

    print("Welcome to Airline Booking System")
    print("1. Enter passenger detail")

    print("2. Retrieve passenger detail and flight")
    print("3. Enter employee detail")
    print("4. Retrieve employee detail")
    print("5. Exit")
    sel = input("Please select from the menu? ")

    if sel == "1":
        n = input("Enter passenger name? ")
        ph = input("Enter passenger phone number? ")
        pn = input("Enter passenger number? ")
        dt = input("Enter destination airport? ")
        dp = input("Enter departure airpot? ")
        P1 = Passenger(n,ph,pn,dt,dp)
        print(P1.get())

    if sel == "2":
        n = input("Enter passenger name? ")
        if n == P1.n:
            print(P1.get())
        else:
            print("No passenger with that name")

    if sel == "3":
        n = input("Enter employee name? ")
        ph = input("Enter employee phone number? ")
        id = input("Enter employee ID? ")
        dept = input("Enter employee department? ")
        E1 = Employee(n, ph, id,dept)
        print(E1.get())

    if sel == "4":
        n = input("Enter employee name? ")
        if n == E1.n:
            print(E1.get())
        else:
            print("No employee with that name")


    if sel == "5":
        quit()
        










