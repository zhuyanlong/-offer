class Solution:
    def isStraight(self, nums):
        nums.sort()
        count=0
        i=0
        while i!=4:
            if nums[i]==0:
                count+=1
            else:
                if nums[i]!=nums[i+1]:
                    diff=nums[i+1]-nums[i]-1
                    if diff<=count:
                        count-=diff
                    else:
                        return False
                else:
                    return False
            i+=1
        return True

def main():
    nums=[0,0,2,2,5]
    s=Solution()
    print(s.isStraight(nums))

main()