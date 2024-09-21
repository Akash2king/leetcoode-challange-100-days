class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
    
        # Initialize the insert position pointer
        insertPos = 2
        
        # Start checking from the third element
        for i in range(2, len(nums)):
           
            if nums[i] != nums[insertPos - 2]:
                
                nums[insertPos] = nums[i]
                # Move the insert position forward
                insertPos += 1
        
        return insertPos

