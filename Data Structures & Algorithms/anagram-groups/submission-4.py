class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        output_arr = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in seen:
                seen[sorted_word].append(word)
            else:
                seen[sorted_word] = [word]
        
        for arr in seen.values():
            output_arr.append(arr)

        return output_arr