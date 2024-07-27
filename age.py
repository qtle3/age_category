# A program that tells the age category.

def main() :
    age = float(input("Give your age: "))

    if age < 0 :
        print("You are not born yet!")        
    elif age < 13 :
        print("Child")
    elif age < 20 :
        print("Teenager")
    elif age < 30 :
        print("Young Adult")
    elif age < 65 :
        print("Adult")
    else :
        print("Senior")

    print("Bye!")

main()
        
