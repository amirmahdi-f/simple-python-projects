main_library = {}

class Library :
    def __init__ (self , library):
        self.library = library
        
    def show_book (self , name):
        print(f"{name} : {self.library[name]}")
        
    def show_all (self):
        for book in self.library :
            print(f'{book} => year : {self.library[book]["year"]} | status : {self.library[book]["status"]}')
            
    def check_status (self , name):
        try:
            print(f'{name} : {self.library[name]['status']}')
        except Exception as error :
            print(f'Error : {error}')
        

my_library = Library(main_library)

class books :
    def __init__ (self , name , year , status):
        self.name = name
        self.year = year
        self.status = status

    def add_to_library(self , library):
        library[self.name] = {"year" : self.year , "status" : self.status}
        
    def remove_from_library (self , library , name):
        library.pop(name)
        