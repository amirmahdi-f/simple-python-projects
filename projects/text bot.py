text = input('enter the text : ')

def count_word(text):
    count = 0
    return len(text.split())
    
def count_sentence(text):
    count = 0
    for sentence in text:
        if sentence == '.' or sentence == '?' or sentence == '!':
            count += 1
            
    return count

print(f'words : {count_word(text)} | sentence : {count_sentence(text)}')