#This is a zigzag program.

i=0 ; steps=8
descending=True

while True:

    whitesp = ""
    for j in range (i,steps):
            whitesp += " "

    print(whitesp+'******')

    if descending: i+=1
    else: i-=1

    #Reverse direction when reaching an edge.
    if i==steps: descending=False
    elif i==0: descending=True
