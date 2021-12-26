"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        q = deque([e for e in employees])
        empMap = {}
        empFound = None

        for e in employees:
            empMap[e.id] = e

        while q:
            emp = q.popleft()
            if emp.id == id:
                empFound = emp
                break
            for sub in emp.subordinates:
                q.append(sub)

        return self.findImportance(empFound, empMap) if empFound else 0


    def findImportance(self, emp, empMap):
        if not emp.subordinates:
            return emp.importance

        result = emp.importance
        for subId in emp.subordinates:
            result += self.findImportance(empMap[subId], empMap)

        return result

