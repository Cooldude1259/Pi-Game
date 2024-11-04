print("Hello, and welcome to the Pi quiz!")
print("You will have to name the digits of Pi 1 by 1")
print("Lets start you off.")
print("Finnish Pi one character at a time. Lets begin 3.")
pi = input()
if pi == "1":
    pi = input()
    if pi == "4":
        pi = input()
        if pi == "1":
            pi = input()
            if pi == "5":
                pi = input()
                if pi == "9":
                    pi = input()
                    if pi == "2":
                        pi = input()
                        if pi == "6":
                            pi = input()
                            if pi == "5":
                                pi = input()
                                if pi == "3":
                                    pi = input()
                                    if pi == "5":
                                        print("Amazing Job! You finnished the Quiz!")
                                    else:
                                        print("Incorrect: 5")
                                else:
                                    print("Incorrect: 3")
                            else:
                                print("Incorrect: 5")
                        else:
                            print("Incorrect: 6")
                    else:
                        print("Incorrect: 2")
                else:
                    print("Incorrect: 9")
            else:
                print("Incorrect: 5")
        else:
            print("Incorrect: 1")
    else:
        print("Incorrect: 4")
else:
    print("Incorrect: 1")
