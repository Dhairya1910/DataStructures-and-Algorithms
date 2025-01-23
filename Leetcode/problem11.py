import copy
def solution(no):
    res = []
    total = 0
    carry = 0 
    index = -1 
    if no[0] == 0 : 
        return [1]
    
    while True:
        if index == -1 : 
            total = no[index] + 1 + carry
            num = total % 10 
            carry = total // 10 
            no[index] = num 
        if  index <= -len(no) and carry:
            res.append(carry)
            no = res + no 
            carry = 0    
        if carry :  
            index = index-1 
            total = no[index] + carry
            num = total % 10 
            carry = total // 10 
            no[index] = num
        if carry == 0 :
            break 
    return no 




a = solution([1])
print(a)

