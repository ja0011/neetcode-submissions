class Solution:
    def calPoints(self, operations: List[str]) -> int:
        empty = []
        for i in operations:
            if i == "+":
                empty.append(empty[-1] + empty[-2])
            elif i == "D":
                empty.append(empty[-1]*2)
            elif i == "C":
                empty.pop()
            else:
                empty.append(int(i))
        return sum(empty)
        