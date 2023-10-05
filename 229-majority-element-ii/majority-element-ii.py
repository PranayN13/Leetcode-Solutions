class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        candidate1 = None
        count1 = 0
        candidate2 = None
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        n = len(nums)
        result = []

        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        return result


        """ 1. Initialize candidate1, candidate2 as None and count1, count2 as 0.
            2. Iterate through each element num in the given list nums.
                - If num matches candidate1, increment count1 by 1.
                - Else if num matches candidate2, increment count2 by 1.
                - Else if count1 is 0, update candidate1 to num and set count1 to 1.
                - Else if count2 is 0, update candidate2 to num and set count2 to 1.
                - Otherwise, decrement count1 and count2 by 1.
            3. Reset count1 and count2 to 0.
            4. Iterate through each element num in nums again.
                - If num matches candidate1, increment count1 by 1.
                - Else if num matches candidate2, increment count2 by 1.
            5. Initialize an empty list result.
            6. If count1 is greater than n/3, append candidate1 to the result.
            7. If count2 is greater than n/3, append candidate2 to the result.
            8. Return the result list containing the majority elements occurring more than n/3 times."""
            