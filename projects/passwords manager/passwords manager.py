import hashlib, string, random, json

# passwords = {
#     "users" : {
#         "user_1" : "password_hash",
#     },
#     "passwords" : {
#         "user_1" : [{
#             "site" : "google",
#             "username" : "related username",
#             "password" : "related password (hash)",
#             "notes" : "related notes"
#         }]
#     }
# }

password_list = {
        "users" : {
            },
        "passwords" : {
        }
        }

def hash_it (text):
    return hashlib.sha256(text.encode()).hexdigest()

def check_user (username, password_list):
    if username in password_list["users"]:
        return True
    else:
        return False

def check_user_main(username, password, password_list):
    if username in password_list["users"].keys() and password in password_list["users"].values():
        return True
    else:
        return False

def menu():
    print("1.register | 2.add password | 3.remove password | 4.show passwords | 5.quit")

def write_json():
    with open ("passwords.txt", "w") as file:
        file.write(json.dumps(password_list))

def make_strong_pass():
    password = ""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
    for number in range(8):
        password += random.choice(numbers)
    for low_letter in range (1):
        password += random.choice(lowercase)
    for up_letter in range (1):
        password += random.choice(uppercase)
    for symbol in range (3):
        password += random.choice(symbols)
        
    return password

class password_manager:
    def __init__(self ,password_list):
        self.password_list = password_list
        
    def register (self, username, password):
        if not check_user(username, self.password_list):
            if password == "strong":
                self.password_list["users"][username] = hash_it(make_strong_pass())
                self.password_list["passwords"][username] = []
                write_json()
                return "acount registered ✅"
            else:
                self.password_list["users"][username] = hash_it(password)
                self.password_list["passwords"][username] = []
                write_json()
                return "acount registered ✅"
            
        else :
            return("username/password is repetitive ❌")
    def add_pass_to_passwords (self, username, username_pass, site = "unknown", passwords_username="unknown", password="unknown", notes="clear"):
        info ={"site" : site, "username" : passwords_username, "password": hash_it(password), "notes" : notes}
        if username in self.password_list["users"].keys():
        
            for user, user_password in self.password_list["users"].items():
                if username == user and hash_it(username_pass) == user_password:
                    self.password_list["passwords"][username].append(info)
                    write_json()
                    return "password added ✅"
            else :
                return "wrong password ❌"
        else:
            return "user notfound ❌"
        
    def del_pass_form_passwords (self, username, username_pass, site):
        if username in self.password_list["users"]:
            for user, user_password in self.password_list["users"].items():
                if username == user and hash_it(username_pass) == user_password:
                    for info in self.password_list["passwords"][username] :
                        if info["site"] == site:
                            self.password_list["passwords"][username].remove(info)
                            write_json()
                            return "password removed 🗑️"
            else :
                return "wrong password ❌"
        else:
            return "user notfound ❌"
    def show_passwords (self, username, username_pass):
        if username in self.password_list["users"]:
            for user, user_password in self.password_list["users"].items():
                if username == user and hash_it(username_pass) == user_password:
                    for password in self.password_list["passwords"][username]:
                        print(f"site : {password["site"]}\nusername : {password["username"]}\npassword : {password["password"]}\nnotes : {password["notes"]}")
                        print("🌟-----------------------🌟")
                        
                else:
                    return "wrong password ❌"
            else:
                return "user notfound ❌"
            


if __name__ == "__main__":
    pass_manager = password_manager(password_list)
    while True:
        menu()
        process = input("what do you want to do : ")
        if process == "1":
            username = input("enter username : ")
            password = input("enter password : ")
            
            print(pass_manager.register(username, password))
        elif process == "2":
            username = input("enter username : ")
            username_pass = input("enter password : ")
            if check_user_main(username, username_pass, password_list):
                site = input("site : ")
                passwords_username = input(f"{site}'s username : ")
                password = input(f"{site}'s password : ")
                notes = input (f"{site}'s notes : ")
                
                print(pass_manager.add_pass_to_passwords(username, username_pass, site, passwords_username, password, notes))
            else:
                print("user notfound")
        elif process == "3":
            username = input("username : ")
            username_pass = input("username_pass : ")
            if check_user_main(username, username_pass, password_list):
                site = input("site : ")
            
                print(pass_manager.del_pass_form_passwords(username, username_pass, site))
            else:
                print("user notfound")
        elif process == "4":
            username = input("username : ")
            username_pass = input("password : ")
            if check_user_main(username, username_pass, password_list):
            
                print(pass_manager.show_passwords(username, username_pass))
            else:
                print("user notfound")
        
        elif process == "5" :
            print("thanks for your attention 🙏")
            exit(0)
        
        else:
            print("command not found")