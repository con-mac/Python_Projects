# File for class and methods
class diet:

    length = 0
    count = 0
    # The central class that objects will derive from.
    # There are 6 properties belonging to the class.
    def __init__(self, time, meal_type, des_of_m, serv, cal, sats ):

        self.time = time
        self.meal_type = meal_type
        self.des_of_m = des_of_m
        self.serv = serv
        self.cal = cal
        self.sats = sats
        diet.count += 1
        self.count += diet.count
        diet.length = 22


    # Print details method will print a description next to each
    # property in each object created.
    def printDetails(self):
        print("Time: ", self.time)
        print("Meal Type: ", self.meal_type)
        print("Descrption of Meal: ", self.des_of_m)
        print("Serving (in grammes): ", self.serv)
        print("cal: ", self.cal)
        print("Saturated Fat (in grammes): ", self.sats)




    # A 'classmethod' is then used to incrementaly count each
    # object and print the record number.
    @classmethod
    def record(cls):
        diet.count +=1
        var = diet.count - diet.length
        return "\nRecord {}".format(var)









































