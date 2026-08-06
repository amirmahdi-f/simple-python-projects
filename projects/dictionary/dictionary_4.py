import json

word_dict = {"hello" : "سلام", "add" : "اضافه کردن"}

def write_json (word_dict):
    with open("dictionary.txt", "w") as file:
        file.write(json.dumps(word_dict, sort_keys=True, ensure_ascii=False, encoding="utf-8"))

def add_word (word , translated_word , word_dict):
    word_dict[word] = translated_word

def persian(old_text):
    text_list = []
    new_text = ""
    for word in old_text:
        text_list.append(word)
    text_list.reverse()
    for word in text_list:
        new_text += word
        
    return new_text

def translate (word_dict , user_word):
    try:
        print(f'meaning of {user_word} is : {persian(word_dict[user_word])}')
    except Exception as error :
        question = input(f'did you know {user_word} meaning ? ')
        if (question.lower()) == "y" or (question.lower()) == "yes":
            translated_word = input(f'enter the {user_word} meaning : ')
            add_word(user_word , translated_word , word_dict)
        else :
            print(f'Error : {error}')
    write_json(word_dict)

while True :
    user_word = input('enter your word : ')
    if user_word == 'quit':
        write_json(word_dict)
        exit(0)
    translate(word_dict , user_word)