print("Welcome to abc.bank ATM")

restart = "Y"
tries = 3
balance = 1000
while tries >= 0:
    pin = int(input("Please enter your pin: "))
    if pin == 1234:
        while restart not in ("N", "n", "No", "no"):
            print("Press 1 to check your balance")
            print("Press 2 to make a withdrawl")
            print("Press 3 to change your pin")
            print("Press 4 to return your card")
            selector = int(input("How may we sereve you?"))
            if selector == 1:
                print("Your current balance is $", balance)
                restart = input("Would you like to go back?")
                if restart not in ("N", "n", "No", "no"):
                    continue
            elif selector == 2:
                print("Your current balance is $", balance)
                print("How much would you like to withdrawl?")
                amount = int(input("Amount: "))
                print("Your remaining balance is $", balance - amount)
                restart = input("Would you like to go back?")
                if restart not in ("N", "n", "No", "no"):
                    continue
            elif selector == 3:
                old_pin = int(input("Enter your old pin: "))
                if old_pin == pin:
                    new_pin = int(input("Enter your new pin: "))
                    pin_check = str(new_pin)
                    if len(pin_check) < 4:
                        print("Enter a pin greater than 3 digits")
                        continue
                    else:
                        re_enter = int(input("Re-enter your new pin: "))
                        if new_pin == re_enter:
                            pin == new_pin
                            print("Your pin has been successfully changed")
                        else:
                            print("Your entered pin doesn't match")
                            break
                else:
                    print("You enter an incorrect pin")
                    break
            elif selector == 4:
                break
        print("Thank you for using our service")
    elif pin != 1234:
        tries = tries - 1
        print("Wrong pin!")
        continue
print("You've entered a wrong pin so many times")
    

            