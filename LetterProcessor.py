for letter in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
    line_build = []
    with open("Raw_Letters/"+letter+".txt","r") as f:
        for line in f:
            if line != "\n":
                line_build.append(line)

    with open("Processed_Letters/"+letter+".txt","w") as f:
        for string in line_build:
            f.write(string)
line_build = []
word_build = []
for letter in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
    with open("Raw_Letters/"+letter+".txt","r") as f:
        for line in f:
            if line != "\n":
                word = line.split(" ")[0]
                line_build.append(line)
                word_build.append(word)
with open("MeaningsMultiLine.txt","w") as f:
    for string in line_build:
        f.write(string)
with open("justWords.txt","w") as f:
    for string in sorted(set(word_build)):
        f.write(string)
        f.write("\n")

line_build = []
with open("MeaningsMultiLine.txt","r") as f:
    prev_word = None
    string = ""
    for line in f:
        if prev_word == None:
            prev_word = line.split(" ")[0]
            string += prev_word+"::"
        word = line.split(" ")[0]
        if word == prev_word:
            string += "__"+line.replace(word,"").replace("\n","")
            prev_word = word
        else:
            line_build.append(string)
            string = ""+word+"::"+"__"+line.replace(word,"").replace("\n","")
with open("MeaningsOneLine.txt","w") as f:
    for string in line_build:
        f.write(string)
        f.write("\n")

thing_list = []
with open("MeaningsOneLine.txt","r") as f:
    for line in f:
        first = line.split("::")[1]
        second = first.split("__")[1:]
        add = False
        for meaning in second:
            thing = ""
            for char in meaning:
                if char == "(":
                    add = True
                elif char == ")":
                    thing_list.append(thing)
                    add = False
                    break
                elif add:
                    thing += char
print(set(thing_list))


