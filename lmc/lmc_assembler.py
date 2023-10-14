import tkinter as tk

root = tk.Tk()
root.geometry("600x700")
root.title = "LM Assembler"

commands = ["INP","STA","ADD","OUT"]

def compile():
    text = textbox.get("1.0","end-1c")

    compiled.insert(tk.END, text)
    
    #get each line as an array
    text = text.split("\n")
    

    #textbox.tag_config("start", foreground="red")
    #textbox.tag_add("start","1.2","1.4")

    #search for lables - ie words that are not commands
    labels = {} #store found labels
    for line in range(0, len(text)):
        tokens = text[line].split(" ")
        for token in tokens:
            if token not in commands:
                if not token.isdigit():
                    #it not a number or command
                    index = tokens.index(token)
                    if index == 0: #the label must be at start of the line
                        labels.update({token : line}) #so add token to the list



    #we now have labels in a dictionary
    #compile the tokens with numbers
    assembled_code = []
    for line in range(0, len(text)):
        tokens = text[line].split(" ")
        token_count = len(tokens)

        #token at the start of the line
        if tokens[0] == "INP":
            assembled_code.append("901")
            if token_count > 1:
                raise Exception ("ERROR on LINE: ", line, " - Token found after INP")
        elif tokens[0] == "OUT":
            assembled_code.append("902")
            if token_count > 1:
                raise Exception ("ERROR on LINE: ", line, " - Token found after OUT")
        elif tokens[0] == "STA":  #STA
            if token_count > 1:
                address = tokens[1] 
                if token_count > 2:
                    raise Exception ("ERROR on LINE: ", line, " - To Many Tokens")
                else:
                    assembled_code.append(("9"+address))
            else:
                raise Exception ("ERROR on LINE: ", line, " - Token found after OUT")



    print(text)

    print(assembled_code)

    print(labels)





textbox = tk.Text(root,width=20,height=20, font=("Ariel",16))
textbox.place(x=20,y = 100)

compiled = tk.Text(root,width=20,height=20, font=("Ariel",16))
compiled.place(x=300,y = 100)

assemble = tk.Button(root, text = "Assemble", font=("Ariel",16), command = compile)
assemble.place(x = 20, y = 600)




root.mainloop()
