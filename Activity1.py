class Employee:
    #Initilizing (Contructor)
    def _init_(self):
        print('Employee created.')
    #Deleting (Destructor)
    def _del_(self):
        print('Destructor called, Employee deleted.')


obj = Employee()
del obj