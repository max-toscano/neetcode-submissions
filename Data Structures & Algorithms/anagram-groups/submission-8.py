class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for words in strs:
            sorted_word = "".join(sorted(words))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(words)
            else:
                anagrams[sorted_word] = [words]
        return list(anagrams.values())