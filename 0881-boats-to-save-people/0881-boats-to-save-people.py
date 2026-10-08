class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        n=len(people)
        people.sort()
        left=0
        boat_count=0
        right=n-1
        while left <= right:
            if people[left]+people[right] <= limit:
                left+=1
                right-=1
            else:
                right-=1
            boat_count+=1
        return boat_count
            
        