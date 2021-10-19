def indent_print(list):
    indent = "   "
    
    for line in list:
        try:
            list = meaning_list[type]
            print(indent+type+":")
            for defs in list:
                print(indent+indent+defs)

        except:
            pass

# Asking for parameters
order = input("Use hyphens and letters to describe known letter locations. Example: letter would be --t-e-")
length = len(order)
known_letters = order.replace("-","")

if order == known_letters:
    blockPrint()
    definition = dictionary.meaning(order)
    enablePrint()
    print(order)
    if definition == None:
        print("No definition known")
    else:
        indent_print(definition)
    print("\n")
    exit()

def containsAll(str, set):
    for c in set:
        if c not in str and c.upper() not in str:
            return False
    return True

word_list = []
with open("every_word.txt","r") as f:
    for line in f:
        if len(line) == length + 1:
            if containsAll(line, known_letters):
                word_list.append(line)

order_count = 0
check_possition = 0
for char in order:
    if char != "-":
        check_possition = 0
        while check_possition < len(word_list):
            if word_list[check_possition][order_count] != char:
                word_list.remove(word_list[check_possition])
            else:
                check_possition += 1
    order_count += 1

for printer in word_list:
    blockPrint()
    definition = dictionary.meaning(printer.replace("\n",""))
    enablePrint()
    print(printer.replace("\n",""))
    if definition == None:
        print("No definition known")
    else:
        indent_print(definition)
    print("\n")



