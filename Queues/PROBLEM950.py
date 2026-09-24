#REVEAL CARDS IN INCREASING ORDER 

from collections import deque
class Solution:
    def deckRevealedIncreasing(self,deck):
        #SORT THE CARDS THIS IS THE ORDER IN WHICH WE WANT THE CARDS TO BE REVEALED 
        deck.sort()
        #CREATE A QUEUE OF INDEXES THESES INDEXES REPRESENT THE POSITIONS WHERE WE WILL PLACE THE SORTED CARDS 
        positions=deque(range(len(deck)))
        #CREATE THE RESULT ARRAY INITIALLY ALL POSITIONS ARE EMPTY 
        answer=[0]*len(deck)
        #GO THROUGH THE SORTED CARDS 
        for card in deck:
            #GET THE POSITION WHERE THIS CARD SHOULD BE PLACED 
            index=positions.popleft()
            #PLACE THE CARD AT THAT POSITION 
            #IF THERE ARE STILL POSITIONS LEFT, MOVE THE NEXT POSITION TO THE BACK 
            #THIS SIMULATES: "MOVE THE NEXT CARD TO THE BOTTOM"
            if positions:
                positions.append(positions.popleft())
        #RETURN THE ARRANGED DECK
        return answer

obj = Solution()

deck = [17, 13, 11, 2, 3, 5, 7]

result = obj.deckRevealedIncreasing(deck)

print("Original Deck:", deck)
print("Arranged Deck:", result)