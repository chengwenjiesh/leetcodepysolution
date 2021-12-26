class Solution:
    def singleNumber(self, nums):
        # nums has at least 2 num occuring only once
        diffBit = 0
        for num in nums:
            diffBit ^= num

        # diff should have at least one bit as '1'
        # find that bit first
        diffBit = diffBit & (-diffBit)

        # bit indicate the two number are different on that bit
        # separate nums into 2 parts: '1' on that bit and '0' on that bit

        result = [0] * 2
        for num in nums:
            if num & diffBit == 0:
                result[0] ^= num
            else:
                result[1] ^= num

        return result

if __name__ == '__main__':
    sol = Solution()
    res = sol.singleNumber([1,2,3,2,4,4])
    print(res)

