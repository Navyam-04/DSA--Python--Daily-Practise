class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        fruits_count={}
        left=0
        max_length=0
        for right in range(len(fruits)):
            incoming_fruits=fruits[right]
            fruits_count[incoming_fruits]=fruits_count.get(incoming_fruits,0)+1
            while len(fruits_count)>2:
                outgoing_fruits=fruits[left]
                fruits_count[outgoing_fruits]-=1
                if fruits_count[outgoing_fruits]==0:
                    del fruits_count[outgoing_fruits]
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length
        