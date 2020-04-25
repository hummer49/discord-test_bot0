import random

def flipCoin(user=None):
    aux = random.randint(0,1)
    if aux ==1:
        r = "heads"
    elif aux ==0:
        r = 'tails'
    print("It was {}\n".format(r))
    if user!=None:
        user = user.lower()
        if user == 'heads' or user == 'tails':
            if user != r:
                print("You lose")
            else:
                print("You win")
        return user == r



