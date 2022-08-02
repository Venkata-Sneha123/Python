rows=int(input("Enter the number of rows: "))
print(rows,end="\n\n")

print("The pattern is :")
for i in range(1,rows+1):
    ch=102
    for j in range(1,i+1):
        ch=ch-1 
        print(chr(ch),end=" ") 
    print("\n") 

#output:
#Enter the number of rows: 5
#5

#The pattern is :
#e 

#e d 

#e d c 

#e d c b 

#e d c b a    

