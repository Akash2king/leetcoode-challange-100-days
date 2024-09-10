def removeElement(nums, val) :
    j=0
    while j <= len(nums)-1 :
        if nums[j] == val :
            nums.remove(nums[j])
            j-=1
        j+=1
    return len(nums)