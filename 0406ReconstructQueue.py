class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        size = len(people)
        result = []

        for i in range(size):
            height, cnt = people[i][0], people[i][1]
            result.insert(cnt, people[i])

        return result

