class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(0,n):
            nums.insert((2*i)+1,nums.pop(n+i))
        return nums