import random
print("What do you want?")
Craving = input()


list = ["Lucky you!!!", "No, you will go out for 10 minute \n take some fresh breath", "No, you will do what you suppose to do but after 10 minute take a break", "No, Dont be so pussy, whole live in your hand, dont give up!!!" ]

rndomint = random.randint(0, len(list) - 1)
print(rndomint)
print(list[rndomint])
