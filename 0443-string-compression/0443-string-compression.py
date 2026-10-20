class Solution:
    def compress(self, chars: list[str]) -> int:
        
        
        n = len(chars)
        if n == 0: return 0
        i, write = 0, 0
        for j in range(n):
            if j == n-1 or chars[j]!= chars[j+1]:
                chars[write] = chars[i]
                write += 1
                if j > i:
                    for c in str(j - i + 1):
                        chars[write] = c
                        write += 1
                i = j + 1
        return write


