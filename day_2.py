def removeDuplicates(nums) :
    i=0
    j=1
    if len(nums) != 1:
        while j != len(nums)-1 :
            if nums[i] != nums[j] :
                j+=1
                i+=1
            else:
                del nums[j]
        if nums[i] == nums[j] :
            del nums[j]
        return len(nums)
    return 1