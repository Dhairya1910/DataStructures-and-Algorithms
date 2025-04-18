def intToRoman(val: int) -> str:
    arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    dic = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    ans = ""

    while val:
        for i in range(len(arr)):
            if val >= arr[i]:
                val = val - arr[i]
                ans = ans + dic[arr[i]]
                break
    return ans 
    

ans = intToRoman(1200)
print(ans)
