import json

from datetime import datetime

def date_now ():
    return datetime.now()

def write_json (message):
    with open ("TO_DO.txt", "w") as file:
        file.write(json.dumps(message))

class TO_DO:
    def __init__(self, To_Do_list):
        self.To_Do_list = To_Do_list
    def add_work (self, work, date, status, information):
        self.To_Do_list[work] = {"information" : information, "date" : date, "status" : status}

    def remove_work (self, work):
        self.To_Do_list.pop(work)

    def show_special_work(self, work):
        print(f'{work} : {self.To_Do_list[work]}')

    def show_work(self, status):
        for work, other in self.To_Do_list.items():
            if other['status'] == status:
                show_special_work(self.To_Do_list, work)

    def show_all (self):
        for work in self.To_Do_list:
            print(work)
            print(f'information : {self.To_Do_list[work]['information']}')
            print(f'status : {self.To_Do_list[work]['status']}')
            print(f'date : {self.To_Do_list[work]['date']}')

    def change(self, work_name, old_part , new_part):
        self.To_Do_list[work_name][old_part] = new_part

    def change_status(self, work_name, new_status):
        self.To_Do_list[work_name]['status'] = new_status


my_list = {}
user_1 = TO_DO(my_list)

while True:
    print('1.add | 2.remove | 3.show_work | 4.change | 5.change_status | 6.show_all | 7.quit')
    process = input('what do you want to do? ')
    if process == '1':
        work_name = input('enter the work name : ')
        work_date = input('enter the date : ')
        if work_date == "now":
            work_date = str(date_now())
        work_status = input('enter the status : ')
        work_information = input('enter the work information : ')
        user_1.add_work(work_name, work_date, work_status, work_information)
        print(f'{work_name} added from your list')

    if process == '2':
        work_name = input('enter the work name : ')
        user_1.remove_work(work_name)
        print(f'{work_name} removed from your list')

    if process == '3':
        works_status = input(f'enter the work / works status : ')
        user_1.show_work(works_status)

    if process == '4':
        work_name = input('enter the work_name you want to change : ')
        work_old_part = input('which part you want to change? (work_name/information/status/date)')
        work_new_part = input(f'enter the new {work_old_part} : ')
        user_1.change(work_name, work_old_part, work_new_part)

    if process == '5':
        work_name = input('enter he work_name : ')
        new_status = input(f"enter the {work_name}'s new status : ")
        user_1.show_all()

    if process == '6':
        user_1.show_all()

    if process == '7':
        print('thanks for your using')
        exit(0)
        
    write_json(my_list)