class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict_freq={}
        for num in nums:
            dict_freq[num]=dict_freq.get(num,0)+1
        max_freq=0
        for count in dict_freq.values():
            if count > max_freq:
                max_freq=count
        ele_count=0
        for num,count in dict_freq.items():
            if count==max_freq:
                ele_count += max_freq
        return ele_count

        