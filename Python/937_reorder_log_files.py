from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letterLogs = []
        digitLogs = []

        for log in logs:
            identifier, content = log.split(" ", 1)
            if content[0].isalpha():
                letterLogs.append(log)
            else:
                digitLogs.append(log)

        letterLogs.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))

        return letterLogs + digitLogs
