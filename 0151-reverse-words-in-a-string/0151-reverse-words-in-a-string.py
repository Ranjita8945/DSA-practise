class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ")
        words = [word for word in words if word]
        words = [" ".join(words[::-1])]
        return words[0]

       
        