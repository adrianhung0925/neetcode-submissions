class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_code = {}

        for word in strs:
            code = [0] * 26

            for char in word:
                code[ord(char) - ord("a")] += 1
            
            str_code = ",".join(str(x) for x in code)
            if str_code not in seen_code:
                seen_code[str_code] = [word]
            else:
                seen_code[str_code].append(word)

        return list(seen_code.values())
