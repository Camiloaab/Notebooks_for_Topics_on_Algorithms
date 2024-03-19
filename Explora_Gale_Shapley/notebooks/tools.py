import numpy as np
import matplotlib.pyplot as plt
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

good={'men_pref': [[2, 4, 6, 7, 0, 3, 5, 1],
  [0, 2, 4, 6, 7, 3, 1, 5],
  [5, 2, 1, 0, 4, 7, 3, 6],
  [6, 1, 4, 5, 0, 7, 3, 2],
  [4, 2, 6, 1, 0, 7, 3, 5],
  [3, 6, 2, 1, 5, 4, 7, 0],
  [1, 7, 2, 4, 0, 3, 6, 5],
  [6, 7, 5, 0, 2, 4, 3, 1]],
 'women_pref': [[4, 0, 1, 5, 7, 2, 6, 3],
  [1, 3, 6, 5, 4, 0, 7, 2],
  [0, 1, 7, 4, 2, 5, 6, 3],
  [4, 1, 2, 3, 5, 7, 0, 6],
  [1, 0, 4, 2, 6, 5, 7, 3],
  [0, 7, 2, 5, 6, 4, 1, 3],
  [6, 3, 4, 5, 2, 1, 7, 0],
  [2, 1, 7, 4, 0, 3, 6, 5]],
 'stable_marriages': [(1, 3, 0, 5, 4, 2, 6, 7),
  (1, 3, 0, 5, 4, 7, 6, 2),
  (1, 6, 0, 5, 4, 2, 3, 7),
  (1, 6, 0, 5, 4, 7, 3, 2),
  (4, 3, 0, 5, 1, 2, 6, 7),
  (4, 3, 0, 5, 1, 7, 6, 2),
  (4, 6, 0, 5, 1, 2, 3, 7),
  (4, 6, 0, 5, 1, 7, 3, 2)]}

def make_table(data,title,yellow=True,constant_width=True):

    back_ground_color='#F1FAEE'
    column_name_color='#F1FAEE'
    cell_color='#F1FAEE'
    if not yellow:
        back_ground_color='#F1FAEE'
        column_name_color='#457B9D'
        #cell_color='#A8DADC'
    


    fig=plt.figure(figsize=(6, 3),dpi=300)
    fig.patch.set_facecolor(back_ground_color)
    plt.axis('off')  # Hide the axes

    table = plt.table(cellText=data, loc='center',cellLoc='center')

    # # Formatting the table
    # # Set column widths based on the longest text in each column
    if not constant_width:
        num_rows, num_cols = len(data), len(data[0])
        cell_text_lengths = [[len(cell) for cell in row] for row in data]
        max_text_lengths = [max(col) for col in zip(*cell_text_lengths)]
        column_widths = [max_text_lengths[j] for j in range(num_cols)]
        table.auto_set_column_width(col=list(range(num_cols)))
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)  # Adjust the scale as needed
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)  # Adjust the table size
    # Apply colors
    for (i, j), cell in table.get_celld().items():
        if not (i*j)==0:
            cell.set_facecolor(cell_color)
        else:
                cell.set_facecolor(column_name_color)
    
    plt.title(title)
    return fig