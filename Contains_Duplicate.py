#To check that does an array (integer) has duplicates or not
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset= set()
#Here we are using hashset method...
#Storing the array in hashset as defining set() method in python      
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)    
        return False    
        
