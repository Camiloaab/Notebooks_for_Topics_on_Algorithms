import numpy as np
def reverse(preferences):
    n= len(preferences)
    return [preferences.index(i) for i in range(n)]


def gale_shapley(p_prefs, d_prefs):## This function takes the matrix preferences of the proponents and disponents.
    ## it returns a list d_partners whose i-th component is the partner of the i-th disponent
    n = len(p_prefs)
    d_partner = [-1] * n
    p_free = [True] * n
    free_count = n
    proposals=[[]]
    relationships=[[]]

    while free_count:
        m = p_free.index(True)
        for w in p_prefs[m]:
            if d_partner[w] == -1:
                d_partner[w] = m
                p_free[m] = False
                free_count -= 1
                proposals.append([(m,w)])
                proposals.append([])
                relationships.append(relationships[-1])
                relationships.append(relationships[-1]+[(m,w)])
                break
            else:
                m1 = d_partner[w]
                w_list = d_prefs[w]
                if w_list.index(m) < w_list.index(m1):
                    d_partner[w] = m
                    p_free[m] = False
                    p_free[m1] = True
                    proposals.append([(m,w)])
                    proposals.append([])
                    relationships.append(relationships[-1])
                    new_rel=relationships[-1]+[(m,w)]
                    new_rel.remove((m1,w))
                    relationships.append(new_rel)
                    break
                else:
                    proposals.append([(m,w)])
                    proposals.append([])
                    relationships.append(relationships[-1])
                    relationships.append(relationships[-1])

    return {"disponents_partners":d_partner,"proposals":proposals,"relationships":relationships}




def make_preferences(n):
    ans=[]
    for i in range(n):
        ans.append(list(np.random.permutation(list(range(n)))))
    return ans