
def bmi():
    name = input("Enter your name : ")
    if not name.isalpha():
        print("Error: letter only")
    else:
        h = float(input("Please Enter your height (cm.) : "))
        w = float(input("Please Enter your weight (kg.) : "))
        h = h / 100
        result = float(("%.2f" % (w / (h**2))))
        if result >= 30.0:
            r = (f"Hello, {name}. Your BMI is {result} and you are FAT Level 3")
            print("-"*len(r))
            print(r)
            print("-" * len(r))
        elif result >= 25.0:
            r = (f"Hello, {name}. Your BMI is {result} and you are FAT Level 2")
            print("-" * len(r))
            print(r)
            print("-" * len(r))
        elif result >= 23:
            r = (f"Hello, {name}. Your BMI is {result} and you are FAT Level 1")
            print("-" * len(r))
            print(r)
            print("-" * len(r))
        elif result >= 18.5:
            r = (f"Hello, {name}. Your BMI is {result} and you are NORMAL")
            print("-" * len(r))
            print(r)
            print("-" * len(r))
        elif result < 18.5:
            r = (f"Hello, {name}. Your BMI is {result} and you are THIN")
            print("-" * len(r))
            print(r)
            print("-" * len(r))

txt = "#"*8+" Welcome to Body Mass Index (BMI) Calculator "+"#"*8
print("#"*len(txt))
print(txt)
print("#"*len(txt))
bmi()
while True:
    q = input("q to exit any key to continue... ")
    if q == 'q':
        break
    else:
        bmi()
