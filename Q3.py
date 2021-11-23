'''Write a program to check if two strings are a rotation of each other?'''


def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = string1 + string1
 
    if size1 != size2:
        return 0
  
    if (temp.count(string2)> 0):
        print("Strings are rotations of each other")
    else:
        print("Strings are not rotations of each other")

areRotations('cat','tca')