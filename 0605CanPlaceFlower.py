class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if n <= 0:
            return True

        cnt = 0
        for i, place in enumerate(flowerbed):
            if place == 0:
                nextPlace = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
                prevPlace = flowerbed[i - 1] if i > 0 else 0
                if not prevPlace and not nextPlace:
                    flowerbed[i] = 1
                    cnt += 1
                    if cnt == n:
                        return True
                    
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPlaceFlowers([1,0,0,0,1],1))
    print(sol.canPlaceFlowers([1,0,0,0,1],2))
