#MINIMUM NUMBER OF K CONSECUTIVE BIT FLIPS 

class Solution:
    def minKBitFlips(self,nums,k):
        #LENGTH OF THE ARRAY 
        n=len(nums)
        #STORES WHERE THE EFFECT IF A FLIP STARTS IR STOPS
        #WE USE N+1 BECAUSE A FLIP CAN END AT INDEX N
        flip=[0]*(n+1)
        #NUMBER OF FLIPS CURRENTLY AFFECTING TEH CURRENT INDEX 
        current_flips=0
        #TOTAL NUMBER OF FLIPS PERFORMED 
        answer=0
        #GO THROUGH THE ARRAY FROM LEFT TOI RIGHT 
        for i in range(n):
            #ADD THE CHANGE IN FLIP EFFECT AT THIS INDEX 
            current_flips+=flip[i]
            #GET THE ORIGINAL VALUE 
            current_value=nums[i]
            #IF AN ODD NUMBER OF FLIPS ARE ACTIVE THE CURRENT VALUE GETS FLIPPED 
            if current_flips%2==1:
                current_value^=1
            #IF THE CURRENT VALUE IS ALREADY 1 WE SKIP IT 
            if current_value==1:
                continue 
            #IF THE CURRENT VALUE IS ZERO WE MUST START A NEW FLIP 
            #BUT WE NEED K ELEMENTS FOR THE FLIP IF THERE WERE LESS THE K ELEMENTS ITS IMPOSSIBLE TO FLIP 
            if i+k>n:
                return -1
            #START A NEW FLIP 
            current_flips+=1
            #THIS FLIPS STOPS AFFECTING ELEMENTS STATING INDEX I+K
            flip[i+k]-=1
            #COUNT THIS FLIP 
            answer+=1
        #RETURN THE MINIMUM NUMBER OF FLIPS 
        return answer
obj = Solution()

nums = [0, 1, 0]
k = 2

result = obj.minKBitFlips(nums, k)

print("Input:", nums)
print("K:", k)
print("Minimum Number of Flips:", result)