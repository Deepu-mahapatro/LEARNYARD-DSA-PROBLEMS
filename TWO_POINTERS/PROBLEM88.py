#MERGE SORTED ARRAYS

#USING BACKWARD TO REPLACE THE 0'S METHOD
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1  #LAST VALID ELEMENT IN NUMS1
        j=n-1  #LAST ELEMENT IN NUMS2
        k=m+n-1  #LAST POSITION IN NUMS1
        #COMPARE ELEMENTS FORM END
        while i>=0 and j>=0:
            #IF NUMS1 ELEMENT IS LARGER
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            #PLACE NUMS2 ELEMENT AT POSITION K
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        #COMPARE REMAINING ELEMENTS FROM NUMS2
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
        #NO NEED FOR WHILE I>=0 REMAINING ELEMENTS IN NUMS1 ARE ALREADY IN PLACE
obj=Solution()
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
print(obj.merge(nums1,m,nums2,n))
print(nums1)


#USING A NORMAL SAMPLE TEST 
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=0
        result=[]
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        while i<m:
            result.append(nums1[i])
            i+=1
        while j<n:
            result.append(nums2[j])
            j+=1
        return result
obj=Solution()
nums1=[1,3,6,8]
nums2=[2,4,5]
print(obj.merge(nums1,4,nums2,3))