#progrm to display hexagons
#defining the function for printin
def hexagondisplay(rows,cols):
    if cols%2!=0:
        limit = (cols+1)//2
    else:
        limit = (cols//2)


#printing hexagons if the num of columns is odd
    if cols%2!=0:

#printing top of the hexagon
        for num in range(limit):
            print(r" ___", end="    ")
        print()

#printing midlle part
        for row in range(rows):
            
            for num in range(limit):     
                if num!=(limit-1):
                    print(r"/   \___", end="")
                else:
                    print(r"/   \ ", end="")
            print()

#printing lower part
            for num in range(0,limit):
                if num!=(limit-1):
                    print(r"\___/", end="   ")
                else:
                    print(r"\___/")


#printing hexagons in=f the num of cols is even
    else:
        #printing the top
        for num in range(limit):
            print(r" ___", end="    ")
        print()

#prrint the middle
        for row in range(rows):
            
            for num in range(limit):     
                if num!=(limit-1):
                    print(r"/   \___", end="")
                elif row!=0:
                    print(r"/   \___/")
                else:
                    print(r"/   \___")
                    

#printin the lower part
            for num in range(limit):
                if num!=(limit-1):
                    print(r"\___/", end="   ")
                elif row!=rows-1:
                    print(r"\___/   \ ")
                    
                else:
                    print(r"\___/    ")
    
#gettin input for num of rows and cols from the user
rows = int(input("Enter no of rows:"))
cols = int(input("Enter no of columns:"))

#calling the function 
hexagondisplay(rows,cols)








