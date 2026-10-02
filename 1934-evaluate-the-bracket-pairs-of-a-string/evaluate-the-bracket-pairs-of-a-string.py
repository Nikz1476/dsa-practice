class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        #O(m+n), O(m) - m keys
        knowledge_map = {}
        i = 0
        answer = ""
        for key, value in knowledge:
            knowledge_map[key] = value

        while i < len(s):
            if s[i] != "(":
                answer +=s[i]
                i+=1
            else:
                j=i+1
                while s[j] != ")":
                    j+=1
                key = s[i+1:j]
                if key in knowledge_map:
                    answer += knowledge_map[key]
                else:
                    answer+= "?"
                i = j+1
        return answer


        # knowledge_map = {}
        # for key, value in knowledge:
        #     knowledge_map[key] = value

        # i = 0

        # while i < len(s):
        #     if s[i] == "(":
        #         j = i + 1

        #         while s[j] != ")":
        #             j += 1

        #         key = s[i + 1:j]

        #         if key in knowledge_map:
        #             value = knowledge_map[key]
        #         else:
        #             value = "?"

        #         s = s[:i] + value + s[j + 1:]
        #         i += len(value)
        #     else:
        #         i += 1

        # return s