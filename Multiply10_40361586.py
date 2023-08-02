#Daniel Junior Nyanganyura 40361586

import random, time

print("Let's practise the multiplication table.\n")

print("Please answer the 5 questions below.")
mark = 0
count=0
anothersession = "y"

while anothersession == "y" :
    timelapse1 = time.time()
    mark = 0
    while count < 5 :
        a = random.randint(1,10)
        b = random.randint(1,10)
        c = str(a) + " x "+ str(b) + ": "
        answer = int(input(c))
        if answer > 100 :
            print("Input Error: Answer is out of range - Please type your answer carefully.")
        else :
            if answer == (a*b):
                print("---Correct---")
                mark+=1
            else :
                print("---Incorrect---")
        count+=1
    count = 0
    timelapse2 = time.time()
    timetaken = round((timelapse2-timelapse1),1)
    print("Your mark is",mark,"out of 5\n")
    print("The time lapse to complete answer the questions, is",str(timetaken),"seconds.")
    print("="*10)
    anothersession = input("Would you like to do another session? (y/n): ")

input("Press enter to stop.")
