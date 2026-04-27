class Solution:
    def countSeniors(self, details: List[str]) -> int:
        current = ""
        counter = 0
        for person in details:
            current = person[11:13]
            if int(current) > 60:
                counter += 1
        return counter