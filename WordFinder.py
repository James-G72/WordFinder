def indent_print(line):
    indent = "   "
    word = line.split("::")[0]
    print(word)
    defs = line.replace(word+"::","").split("__")[1:]
    for line in defs:
        print(indent+line.replace("\n",""))

# Asking for parameters
order = input("Use hyphens and letters to describe known letter locations. Example: letter would be --t-e-")
length = len(order)
known_letters = order.replace("-","")
keys = input("Keyword(s): ")

def containsAll(str, set):
    str = str.lower()
    set = set.lower()
    if str == "eat":
        t = 1
    for c in set:
        num = str.count(c)
        if num == 0:
            return False
        else:
            str = str.replace(c,"")
            for x in range(0,num-1):
                str += c
    return True

if order == known_letters:
    if keys != "-jumble-":
        with open("MeaningsOneLine.txt","r") as f:
            for line in f:
                word = line.split("::")[0]
                if word.lower() == order.lower():
                    indent_print(line)
                    quit()

word_list = []
with open("MeaningsOneLine.txt","r") as f:
    for line in f:
        word = line.split("::")[0]
        if len(word) == length:
            if containsAll(word, known_letters):
                word_list.append(line)

if keys == "-jumble-":
    for line in word_list:
        indent_print(line)
        print("\n")

order_count = 0
check_possition = 0
for char in order:
    if char != "-":
        check_possition = 0
        while check_possition < len(word_list):
            if word_list[check_possition].split("::")[0][order_count].lower() != char:
                word_list.remove(word_list[check_possition])
            else:
                check_possition += 1
    order_count += 1

if keys != "":
    if keys.split(" ") == keys:
        keys = [keys]
    else:
        keys = keys.split(" ")
    for key in keys:
        for line in word_list:
            if key in line:
                indent_print(line)
                print("\n")
else:
    for line in word_list:
        indent_print(line)
        print("\n")



