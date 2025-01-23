# BASEBALL GAME
def calPoints(operations) :
    n = len(operations)
    stack = []
    i = 0
    count = 0 
    while i <= n-1 :
        if operations[i] == "C":
            stack.pop()
            i = i+1 
            count = count -1 
            print(count)
        elif operations[i] == "D":
            val = int(stack[count-1]) * 2 
            stack.append(val)
            i = i+1 
            count=count+1
            print("D",count)
        elif operations[i] == "+":
            print("before",count)
            print(stack)
            val = int(stack[count-1])+int(stack[count-2])
            stack.append(val)
            i = i+1 
            count = count +1 
            print("+",count)
        else :
            stack.append(int(operations[i]))
            i = i+1 
            count = count +1 
            print("else",count)
    print(sum(stack))
    return sum(stack)

calPoints(["5","2","C","D","+"])


        # out = [0] * len(temperatures)
        # count = 0
        # n = len(temperatures)
        # for i in range(0,n-1):
        #     for j in range(i+1,n):
        #         count = count + 1 
        #         if temperatures[j] > temperatures[i]:
        #             out[i] = count
        #             count = 0 
        #             break
        #     count = 0
        # return out 