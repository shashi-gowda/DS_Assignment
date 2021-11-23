'''Write a program to find the smallest number using a stack'''


class stack:
    def __init__(self):
        self.s=[]
        self.smallest_num=None

    def push(self,x):
        if not self.s:
            self.smallest_num=x
            self.s.append(x)
            return
        if x<self.smallest_num:
            self.s.append(2*x-self.smallest_num)
            self.smallest_num=x
        else:
            self.s.append(x)

    def pop(self):

        if not self.s:
            return -1

        top=self.s.pop()

        if top<self.smallest_num:
            k=self.smallest_num
            self.smallest_num=2*k-top
            return k
        else:
            return top

    def getMin(self):
        if not self.s:
            return -1
        else:
            return self.smallest_num

min_num=stack()

for x in range(5):
    min_num.push(x)

print(min_num.s)

print(min_num.getMin())