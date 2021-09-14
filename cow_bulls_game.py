import random
digit=5
name=input(" \U0001F412 enter your name \U0001F412: ")
print("*************",name,"***********")
print("**\U0001F973 WEL COME TO COWS AND BULLS GAME \U0001F973**")
print("--------------------------------")
def getSecretNum():
    number=list(range(10))
    random.shuffle(number)
    return number
def getclues():
    numbers=getSecretNum()
    secret_num=[]
    for i in range(digit):
        secret_num.append(numbers[i])
    return secret_num
def check_guess():
    bull=[]
    cow=[]
    num=getclues()
    i=0
    print(num)
    maxguess=10
    while maxguess>0:
        guess=int(input(" \U0001F49A enter the guess = "))
        position=int(input(" \U0001F33A enter the position of your number \U0001F33A= "))
        print("************************")
        if guess in num:
            index = num.index(guess)
            if index == position:
                if guess not in bull:
                    bull.insert(index,guess)
                    print("Bull",bull)
                else:
                    print(" \U0001F90E	You already used this digit try any different digit \U0001F90E	")
                    print("*************************")
            else:
                cow.append(guess)
                print(" \U0001F4A4	Cow,This number is in list you can reuse it \U0001F4A4	",cow)
        if bull == num:
            print(name," \U0001F98B Congractulations you win the game.......\U0001F98B	")
            print("*************************")
            break
        maxguess=maxguess-1
        print(maxguess," \U0001F337 Turns are left..\U0001F337")
    else:
        print(" \U0001F426 You ran out your tries,You Loose The Game..\U0001F426")
        print("*************************")
    return bull
check_guess()
def play_again():
    while True:
        again = input(" \U0001F986 If You Want To Play Again  Press Y For Yes or N of No  \U0001F986= ")
        if again == "Y":
            check_guess()
        else:
            break
play_again()











































