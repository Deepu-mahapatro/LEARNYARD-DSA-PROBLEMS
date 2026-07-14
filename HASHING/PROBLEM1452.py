#PEOPLE WHOSE LIST OF FAVORITE COMPANIES IS NOT A SUBSET OF ANOTHER LIST


from typing import List
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        #CONVERT ECAH PERSON'S COMPANY LIST INTO A SET
        company_sets=[set(companies) for companies in favoriteCompanies]
        #STORE THE INDICES OF PEOPLE WHOSE LIST IS NOT A SUBSET
        answer=[]
        #CHECK EVERY PERSONS COMPANY LIST
        for i in range(len(company_sets)):
            is_subset=False
            #COMPARE WITH EVERY OTHER PERSONS COMPANY LIST
            for j in range(len(company_sets)):
                #SKIP COMPARING THE SAME PERSON
                if i==j:
                    continue
                #IF PERSON I'S LIST IS A SUBSET OF PERSON J'S LIST
                #THEN PERSON I SHOULD NOT BE INCLUDED IN THE ANSWER
                if company_sets[i].issubset(company_sets[j]):
                    is_subset=True
                    break
            #IF THE LIST IS NOT A SUBSET OF ANYONE ELSE'S LIST
            #THEM AS STHE INDEX TO THE ANSWER
            if not is_subset:
                answer.append(i)
        return answer
obj=Solution()
favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
print(obj.peopleIndexes(favoriteCompanies))