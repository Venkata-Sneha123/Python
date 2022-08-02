rows=int(input("Enter the number of rows: "))
print(rows,end="\n\n")

print("The pattern is :")
for i in range(rows,0,-1):
    for j in range(rows,i-1,-1):
        ch=96+i
        print(chr(ch),end=" ") 
    print("\n") 

#output:
#Enter the number of rows: 5
#5

#The pattern is :
#e 

#d d 

#c c c 

#b b b b 

#a a a a a     

