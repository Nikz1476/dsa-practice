class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #time - O(n log n)
        #space - O(n)
        loss = {}

        for w, l in matches:
            if w not in loss:
                loss[w] = 0   # winner initially has 0 losses
            loss[l] = loss.get(l, 0) + 1

        zero_loss = []
        one_loss = []

        for player, cnt in loss.items():
            if cnt == 0:
                zero_loss.append(player)
            elif cnt == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]

        # alternate(same time and space complexity):
        #         loss = {}
        # players = set()

        # for w, l in matches:
        #     players.add(w)
        #     players.add(l)
        #     loss[l] = loss.get(l, 0) + 1

        # zero_loss = []
        # one_loss = []

        # for p in players:
        #     if p not in loss:
        #         zero_loss.append(p)
        #     elif loss[p] == 1:
        #         one_loss.append(p)

        # return [sorted(zero_loss), sorted(one_loss)]
        