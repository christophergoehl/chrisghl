from master.apr_lib import *

def create_baskets(file):
    file = open(file, "r")
    counter: int = 0
    i = 0
    for lines in file:
        counter += 1
        c = counter
        allset.append("SC" + str(c))
        allset[i] = i_bsk("SC" + str(c))
        allset[i].add_bsk(lines)
        i+=1

create_baskets("baskets.txt")
for i in allset:
    print(i.bsk)



print(allset)



