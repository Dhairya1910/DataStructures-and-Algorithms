class HashTable:
    def __init__(self,size):
        self.size = size 
        self.hash_table = self.Create_Bucket()
    
    def Create_Bucket(self):
        return [[] for _  in range(self.size)]

    def set_val(self,key,val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_val = False 
        for index,record in enumerate(bucket):
            record_key , record_val = record

            if record_key == key : 
                found_val = True 
                break 
        
        if found_val : 
            bucket[index] = (key,val)
        else:
            bucket.append((key,val))

    def get_val(self,key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False 
        for index , record in enumerate(bucket):
            record_key , record_val = record
        
            if record_key == key:
                found_key = True 
                print("Key found ")
                break 

        if found_key:
            return record_val
        else :
            return "No record "
            
    def Delete_val(self,key):

        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False 

        for index, records in enumerate(bucket):
            record_key , record_val = records 

            if record_key == key : 
                found_key = True 
                break 

        if found_key:
            bucket.pop(index)
            print("Key and value removed succesfully delete ")

    def __str__(self) :
        return "".join(str(item) for item in self.hash_table)



MyHash = HashTable(50)
MyHash.set_val(10,"S1mple is greatest")
val = MyHash.get_val(10)
MyHash.Delete_val(10)
print(val)
hash_table = str(MyHash)
print(hash_table)








        