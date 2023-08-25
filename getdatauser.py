import csv
import os 

class UserData:
    # object
    def __init__(self, name, age, phone, email, password):
        self.name  = name
        self.age   = age
        self.phone = phone
        self.email = email
        self.password = password

    # get data from user in class methot 
    @classmethod
    def DataUser(cls):
        name        = input('input your name :')
        age         = input('input your age  :')
        phone       = input('input your phone number :')
        email       = input('input your email :')
        password    = input('input your password :')


        while not (name  and email  and password and  age and phone):
            print("You forgot to input some data. Please provide the missing information.")
            if not  name  :
                name  = input('input your name : ')
            if not age :
                age  = input('input your age: ')
            if not phone :
                phone  = input('input your phone: ')
            if not email :
                email  = input('input your email : ')   
            if not password :
                password  = input('input your password: ')
        
        return cls(name,  age, phone, email, password)
    
    def to_list(self):
        return [self.name, self.age, self.phone, self.email, self.password]

class Usermanage:
    def __init__(self, filename='dataofuser.csv'):
        self.filename = filename
        self.user_data = None

    #save dara to csv file 
    def save_to_csv(self,data):
        file_exists = os.path.isfile(self.filename)
        header = ['name','age','phone','email','password ']
        with open(self.filename,'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            if not file_exists:
                writer.writerow(header)
            
            writer.writerow(data)
            
    def add_user(self, user_data):
        user_data =user_data.to_list()
        self.save_to_csv(user_data)
        print("User data saved successfully!")

    def main(self):
        self.user_data = UserData.DataUser()
        self.add_user(self.user_data)

    def show_user_data(self):
        if self.user_data:
            print("User Data:")
            print("Name:", self.user_data.name)
            print("Age:", self.user_data.age)
            print("Phone:", self.user_data.phone)
            print("Email:", self.user_data.email)
            print("Password:", self.user_data.password)
        else:
            print("No user data available.")

    def show_csv_contents(self):
        with open(self.filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)

if __name__== "__main__":
    user_manager = Usermanage() # Create an instance of Usermanage class
    user_manager.main()         # Call the main method of Usermanage
    user_manager.show_user_data()   # Show user data
    user_manager.show_csv_contents() # Show CSV file contents  

