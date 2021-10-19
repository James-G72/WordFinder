def indent_print(line):
    indent = "   "
    word = line.split("::")[0]
    meanings = line.replace(word+"::","").split("__")
    print(word)
    for type in meanings[1:]:
        print(indent+type.replace("\n",""))

# Asking for parameters
order = input("Use hyphens and letters to describe known letter locations. Example: letter would be --t-e-")
length = len(order)
known_letters = order.replace("-","")
keys = input("Keyword: ")

if order == known_letters:
    with open("MeaningsOneLine.txt","r") as f:
        for line in f:
            word = line.split("::")[0]
            if word.lower() == order.lower():
                indent_print(line)
                print("\n")
                exit()

def containsAll(str, set):
    for c in set:
        if c not in str and c.upper() not in str:
            return False
    return True

word_list = []
with open("MeaningsOneLine.txt","r") as f:
    for line in f:
        word = line.split("::")[0]
        if len(word) == length:
            if containsAll(word, known_letters):
                word_list.append(line)

order_count = 0
for char in order:
    if char != "-":
        list_possition = 0
        while list_possition < len(word_list):
            if word_list[list_possition].split("::")[0][order_count] != char:
                word_list.remove(word_list[list_possition])
            else:
                list_possition += 1
    order_count += 1

if keys != "":
    if " " in keys:
        keys = keys.split(" ")
    if isinstance(keys,list):
        for key in keys:
            for word in word_list:
                if key in word:
                    indent_print(word)
                    print("\n")
    else:
        for word in word_list:
            if keys in word:
                indent_print(word)
                print("\n")

else:
    for printer in word_list:
        indent_print(printer)
        print("\n")



