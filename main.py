import os
import json
import random
import string

file_name="data.json"

class pass_manager:
    def add_pass(self):
        web=input("Enter your website name:\n")
        username=input("Enter your username:\n")
        
        print("How do you want your password?")
        print("1. Enter manually")
        print("2. Generate password")

        check=int(input("Enter your choice"))
        if check==1:
            password=input("Enter your password:\n")

        elif check==2:
            password=self.generate_password()
            print("Generated Password:", password)

        else:
            print("Invalid choice")
            return
        
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                data=json.load(file)
        else:
            data= []

        new_pass={
            "website" : web,
            "username" : username,
            "password" : password
        }
        data.append(new_pass)
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
    
    def view_pass(self):
        try:
            with open(file_name, "r") as file:
                data=json.load(file)

        except FileNotFoundError:
            print("File doesn't exists")
            return

        for item in data:
            print("Website:", item["website"])
            print("username:", item["username"])
            print("password:", item["password"])
            print()


    def search_pass(self):
        web=input("Enter your website name")
        try:
            with open(file_name, "r") as file:
                data=json.load(file)
        except FileNotFoundError:
            print("File does not exist")
            return

        found=False
        for item in data:
            if item["website"]==web:
                print(item["website"])
                print(item["username"])
                print(item["password"])
                found=True
        if not found:
            print("Your website does not exist")

    def delete_pass(self):
        web=input("Enter your website name")

        try:
            with open(file_name, "r") as file:
                data=json.load(file)
        except FileNotFoundError:
            print("File doesn't exist")
            return

        found=False
        for item in data:
            if item["website"]==web:
                data.remove(item)
                found=True
                break

        if found:
            with open(file_name, "w") as file:
                json.dump(data,file, indent=4)
            print("Your website deleted successfully")

        else:
            print("Your website doesn't exist")

    def generate_password(self):

        pass_len=8
        password=""
        CharValue=string.ascii_letters + string.punctuation + string.digits

        for i in range(pass_len):
            password += random.choice(CharValue)
        return password

    def menu(self):

        while True:
            print("1. Add Password")
            print("2. View Password")
            print("3. Search Password")
            print("4. Delete Password")
            print("5. Exit")

            try:
                choice=int(input("Enter your number according to your choice"))

            except ValueError:
                print("Enter numbers only")
                continue

            if choice==5:
                print("Goodbye")
                break

            if choice not in[1,2,3,4]:
                print("Enter Valid choice")

            elif choice==1:
                self.add_pass()

            elif choice==2:
                self.view_pass()

            elif choice==3:
                self.search_pass()

            elif choice==4:
                self.delete_pass()

            else:
                print("Invalid choice")

pm=pass_manager()
pm.menu()