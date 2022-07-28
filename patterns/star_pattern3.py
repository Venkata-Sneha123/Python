rows=int(input("Enter the number of rows: "))
print(rows,end="\n\n")
print("The pattern is :")
for i in range(0,rows):
    for k in range(0,rows-i):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",sep=" ",end=" ")
    print("\n")    


# output:
#Enter the number of rows: 5
#5

#The pattern is :
#          * 

#        * * 

#      * * * 

#    * * * * 

#  * * * * * 

