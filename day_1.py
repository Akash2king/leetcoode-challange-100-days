# two sum problem

def twoSum(nums, target):
    if len(nums) >= 2:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i!=j:
                    sum=nums[i]+nums[j]
                    if target == sum :
                        return [i,j]


        