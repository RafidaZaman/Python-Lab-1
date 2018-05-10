#Problem 3: Given a list of n number, write a Python program to find triplets in the list which gives the sum of zero.

def Triplets(Input, l):
    TripletExist = True
    for i in range(0, l - 2):
        for j in range(i + 1, l - 1):
            for k in range(j + 1, l):
                if (Input[i] + Input[j] + Input[k] == 0):
                    print("Triplets: [(", Input[i], Input[j], Input[k], ")]")
                if (TripletExist == False):
                    print(" No Triplets ")
Input = [1, 3, 6, 2, -1, 2, 8, -2, 9]
l = len(Input)
Triplets(Input, l)