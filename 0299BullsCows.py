class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        digits = [0] * 10
        size = len(secret)
        bulls, cows = 0, 0

        for i in range(size):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                # add 1 to digits if found it in secret
                # minus 1 from digits if found it in guess
                s, g = int(secret[i]), int(guess[i])
                if digits[s] < 0:
                    cows += 1
                if digits[g] > 0:
                    cows += 1
                digits[s] += 1
                digits[g] -= 1

        return str(bulls) + "A" + str(cows) + "B"

