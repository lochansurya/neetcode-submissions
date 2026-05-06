class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        table = [[0]*26 for _ in strs]
        bag = set()
        i = 0
        while i<n:
            string = strs[i]
            for ch in string:
                table[i][ord(ch) - ord('a')] += 1
            i += 1
        
        used = [False]*n
        ans =[]
        i = 0

        while i < n:
            if used[i]:
                i += 1
                continue
            group = [strs[i]]
            used[i] = True

            j = i + 1
            while j<n:
                k = 0

                while k < 26:
                    if table[i][k] != table[j][k]:
                        break
                    k += 1
                if k == 26:
                    group.append(strs[j])
                    used[j] = True
                
                j += 1
            ans.append(group)
            i += 1
        return ans
        