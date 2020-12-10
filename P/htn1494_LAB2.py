##NAME: HUNG NGUYEN
#ID:    1001721494
#DATE   NOVEMBER 6
#OS     window / BUT compiled code on UBUNTU 20 VM with python3.8.5

f = open('input_RPN.txt','r')

def compare(c):
    box = ['+','-','/','*']
    if c in box:
        return 0
def result(c1,c2,ops):
    if ops == '+':
        return int(c1) + int(c2)
    elif ops == '-':
        return int(c1) - int(c2)
    elif ops == '/':
        return int(c1) / int(c2)
    elif ops == '*':
        return int(c1) * int(c2)

stack = [] # create an empty stack
for line in f:
    # iterate thru every single line and execute the code below
    list = line.split()
    for i in list:
        #iterate thru the list
        if compare(i) != 0: #if its a number then append to an empty stack
            stack.append(i)
        elif compare(i) == 0: # check if the character is an operator
            operator = i
            x1 = stack.pop() # pop out the number from the stack
            x2 = stack.pop() # pop out the second number from the stack to do the math
            stack.append(result(x2,x1,operator)) # put the result back onto the stack so every time we take out 2 number we put back 1

    print(stack) # print out the resutl
    stack = [] # reset the stack for a new line

f.close()
