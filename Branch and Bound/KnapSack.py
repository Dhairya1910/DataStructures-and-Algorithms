import heapq 

class Item:
  def __init__(self,Weight,Profit):
    self.Weight = Weight 
    self.Profit = Profit 
    self.ratio = self.Profit / self.Weight 

class Node:
  def __init__(self,level,Weight,Profit,Temp_price):
    self.level = level
    self.Weight = Weight 
    self.Profit = Profit 
    self.Temp_price = Temp_price

  def __lt__(self,other):
    return self.Temp_price > other.Temp_price

def Calculate_price(items,max_weight,node):
  num_items = len(items)
  if node.Weight >= max_weight:
    return 0 
  
  total_profit = node.Profit
  j = node.level + 1 
  total_weight = node.Weight 

  while j < num_items and (total_weight + items[j].Weight) <= max_weight:
    total_profit = total_profit + items[j].Profit 
    total_weight = total_weight + items[j].Weight
    j = j + 1 
  
  return total_profit 

def Knapsack(items,max_weight):
  num_items = len(items)
  sack = []
  max_profit = 0 
  Priority_queue = []
  items.sort(key = lambda x : x.ratio , reverse=True)

  root = Node(-1,0,0,0)
  root.Temp_price = Calculate_price(items,max_weight,root)
  heapq.heappush(Priority_queue,root)


  while Priority_queue:
    current_level = heapq.heappop(Priority_queue)
    if current_level == num_items-1:
      continue 
    next_level = current_level.level + 1 
    next_weight = current_level.Weight + items[next_level].Weight 
    if next_weight <= max_weight:
      next_profit = current_level.Profit + items[next_level].Profit
      if next_profit > max_profit:
        max_profit = next_profit 
      next_node = Node(next_level,next_weight,next_profit,0)
      next_node.Temp_price = Calculate_price(items,max_weight,next_node)
      sack.append(next_node)
      if next_node.Temp_price > max_profit:
        heapq.heappush(Priority_queue,next_node)
    
    next_node = Node(next_level,next_level,current_level.Profit,0)
    next_node.Temp_price = Calculate_price(items,max_weight,next_node)
    if next_node.Temp_price > max_profit:
      heapq.heappush(Priority_queue,next_node)
  return max_profit , sack


if __name__ == '__main__':
    item1 = Item(10, 200)
    item2 = Item(15, 210)
    item3 = Item(20, 350)
    item4 = Item(30, 400)
    pack = [item1, item2, item3, item4]
    max_weight = 70
    max_profit , sack = Knapsack(pack, max_weight)
    print(f"Maximum Profit: {max_profit}")
    print("Weight","Profit")
    for item in sack:
      if item.Profit == max_profit:
        print(item.Weight ,"\t", item.Profit)
        break
      else:
        print(item.Weight,"\t",item.Profit)


  


  
 

