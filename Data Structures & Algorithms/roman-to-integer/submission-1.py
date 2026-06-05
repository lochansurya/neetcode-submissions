class Solution:
    def romanToInt(self, s: str) -> int:
        symtab = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        roman_string = s
        n = len(roman_string)
        cur, nex = 0, 1

        ans = 0
        while cur < n:
            ch = s[cur]
            val = symtab[ch]
            ans += val
            if nex==n:
                break
            next_val = symtab[s[nex]]
            if val < next_val:
                ans -= 2*val
            
            cur = nex
            nex += 1

        return ans