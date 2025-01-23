import heapq

class items:
    def __init__(self,weight,profit):
        self.weight = weight 
        self.profit = profit 

def Knapsack(pack,max_weight,profit):
    Knapsack = []
    item = 0 
    while max_weight >= 0:
        item = item % 4 
        if max_weight < pack[item].weight:
            return Knapsack
        else:
            max_weight = max_weight - pack[item].weight
            profit = profit + pack[item].profit
            Knapsack.append(pack[item])
            item += 1 
    return Knapsack


if __name__ == '__main__':
    print("Knapsack")
    item1 = items(10,200)
    item2 = items(15,210)
    item3 = items(20,350)
    item4 = items(30,400)
    pack = [item1,item2,item3,item4]
    a = Knapsack(pack,90,0)
    total_weight = 0
    total_profit = 0
    for i in a:
        total_weight = total_weight + i.weight
        total_profit = total_profit + i.profit
        print((i.weight , i.profit))

    print(f"total profit : {total_profit} , total Weight : {total_weight}")
    
