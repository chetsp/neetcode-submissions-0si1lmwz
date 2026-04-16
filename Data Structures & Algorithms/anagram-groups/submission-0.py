'''from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use list as the default factory
        premap = defaultdict(list)
        
        for s in strs:
            # Convert the sorted list to a tuple so it can be a dict key
            key = tuple(sorted(s))
            premap[key].append(s)

        return list(premap.values())'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Tuples are hashable; lists are not
            res[tuple(count)].append(s)
        return list(res.values())