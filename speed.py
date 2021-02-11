#speed.py
#Wilco Ng 05/06/20
#To issue out speeding tickets
def wanted():
    wanted_list = ["sam", "trisan", "ravi", "scott", "jardong", "wok", "nya", "mya", "gibson", "hi", "kok"]
    name = input("Wut is your name? ").lower().strip()
    if name in wanted_list:
        print("PEW PEW YOU HAVE BEEN THE SHOT WITH MY K-NIfe")
        exit()
    else:
        pass

def whoe_cod():
    while True:
        try:
            speed = float(input("What is your speed? "))
            speed_limit = float(input("What was the speed limit? "))
            #finding the overspeed
            sped = speed - speed_limit
            #deciding on the outcomes
            if 1 <= sped < 50:
                cost = sped * 10
                print("You must pay the price of ${}".format(10 * round(sped)))
                break
            elif speed == speed_limit:
                print("You are gud to going".format(sped))
                break
            elif sped <= -1:
                print("Since your speed was not over the speed you are gud".format(sped))
                break
            elif 50 <= sped <= 80:
                cost = sped * 10
                print("Since your speed was {} over the speed you must give the licence".format(sped))
                break
            elif sped >= 81:
                print("Since your speed was {} over the speed you are crime go to bar hoouse".format(sped))
                break
        #to make the user enter a number
        except ValueError:
            print("Plox enter a number/integer")

wanted()
whoe_cod()
