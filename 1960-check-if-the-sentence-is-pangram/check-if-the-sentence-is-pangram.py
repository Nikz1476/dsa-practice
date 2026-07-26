class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        freq = {}
        for i in range(len(sentence)):
            freq[sentence[i]] = freq.get(sentence[i],0)+1
        return len(freq) == 26