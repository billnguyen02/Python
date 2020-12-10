"""
    HUNG NGUYEN
    1001721494
    11/24
    PYTHON3 ON UBUNTU 20.04
"""

f = open('input_EC.txt','r+')
count = 0
inner = 0

statement = True
for line in f:
    comment = 0

    boolean = True
    line = line.rstrip('\n')
    

        #if the line is comment out then ignore the whole line
    if "/*" in line:
        statement = False
        # set the boolean equal to false so that we don't execute the bracket counting if it is false
    elif "*/" in line:
        statement  = True
        # set the boolean equal to true so that we execute the bracket counting when the statement is true only
    else:
        if ')' in line and '{' in line and statement == True and comment == 0 and '"' not in line:
           
            # this is to check if the () and {}  are in the same line and not in a ""
            first_split = line.split('{')
            #split the line to 2 half between the character {
            print(count, first_split[0] )
            print(count,"{")
            #print the first half before the character {
            second_split = first_split[1].split('}')
            #split the second half from the first split to the end of the closing bracket}
            print(count,"\t",second_split[0])
            print(count,"}")  
        else:      
            if "//" in line:
                comment = 100
                # this is to make sure the line is comment out
                string = line.partition("//")
                print("string 0" , string[0])
                if '{'  not in string[0] or '}' not in string[0]:
                    print("pass")
                    boolean = False
                    pass        
                    # partition to cut the string into smaller string at the character.
                    # here i split up the string and check if the first half of the string contain { or } if it does not then pass do not increment or decrement count
            word = line.split()
            # split the line by a space delimiter
            for i in word:
                #for everysingle word in the line

                if id(i) == id("{") and statement == True :
                    count += 1
                    # if we character { is in the line then}
                elif id(i) == id("}") and statement == True :
                    if inner == 0:
                        inner += 1
                        #increment the inner so that next line comes in the inner wont be 0 anymore
                        #since we do not want to decrement count at the first closing bracket its finds
                        #none comment to make sure it is not a comment out sentence
                    else:
                        count -= 1
    #here is what we want it to do at the end of each line                  
    if len(line.strip()) == 0:
        pass
        # this is to get rid of empty lines and don't print em
    elif '}' in line and count == 1 :
        # check if it is the last closing brackets then print that line and make everything after that count = 0
        print(count,line)
        count = 0
    elif ')' in line and '{' in line and statement == True and comment == 0 and '"' not in line :
        pass
    else:   
        print(count,line)
    