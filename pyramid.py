import time
def pyramid():
    row = int(input("Enter level number : "))
    sb = input("Enter symbol : ")
    sc = input("1. Up \n"
               "2. Down \n"
               "Enter a direction : ")
    if sc == '1':
        if row == 0:
            print("Must be greater than 0")
            pass
        for i in range(1,row+1):
            print(f"{sb}" * i)
            time.sleep(1)
    elif sc == '2':
        if row == 0:
            print("Must be greater than 0")
            pass
        for i in range(row,0,-1):
            print(f"{sb}" * i)
            time.sleep(1)
    else:
        print("Please select menu again")
pyramid()
while True:
    q = input("q to exit any key to continue... ")
    if q == 'q':
        break
    else:
        pyramid()