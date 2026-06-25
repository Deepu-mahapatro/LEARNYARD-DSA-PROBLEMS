#REMOVE DUPLICATES FROM SORTED ARRAY

def duplicate(nums):
    if len(nums)==0:
        return -1
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
nums=[2,2,3,4]
print(duplicate(nums))