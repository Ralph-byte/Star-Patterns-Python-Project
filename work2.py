num = int(input("Enter number of rows: "))

rows=1
for i in range(0, num):
    for j in range(num,i,-1):
        print("*", end="")
    # rows=rows+3
    print()    