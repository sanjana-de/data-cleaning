'''
    Function to compute qgrams(). 
    It takes a single string as i/p and returns a list with qgrams
'''
import random
import operator
from itertools import groupby

def qgrams(str,n) :
    modstr = '#' + str + '$'
    b = []
    #print(modstr)
    for i in range(len(modstr)-n+1) :
        qgr = modstr[i:i+n]
        #print(qgr)
        b.append(qgr)

    #print(b)
    return b 

''' 
    Function to compute inverse strings. 
    It returns the list of indexes containing the given qgram. 
'''
def inverse_strings(qgr,db) :
    res = []
    Bag = []
    for alpha in db :
        Bag = qgrams(alpha,2)
        if qgr in Bag :
            res.append(db.index(alpha))
    return res


def intersection(list1,list2) :
    return list(set(list1) & set(list2))


def union(list1,list2) :
    return list(set(list1) | set(list2))

def overlapStrings(tp) :
    overlap = []
    overlap = inverse_strings(tp[0],db)
    for ki in tp :
        inv_str = inverse_strings(ki,db) 
        overlap = intersection(overlap,inv_str) 

    #print(overlap)
    return overlap 

def count_qgrams(seq) -> dict:
    hist = {}
    for i in seq :
        hist[i] = hist.get(i,0)+1

    return hist 


def extract_bag(hist,size) :
    bag = []
    for key in hist.keys():
        bag.append(key)

    return bag[:size] 

'''
def longest_sequence(cluster_list) :
    # freq = max(set(cluster_list), key = cluster_list.count)
    count_max = 0
    
    for i in range(len(cluster_list)-1) :
        #i=i+1
        if cluster_list[i] == cluster_list[i+1] :
            count = 1
            while cluster_list[i] == cluster_list[i+1] and i<(len(cluster_list)-2):
                i = i+1
                count= count+1
            if i==(len(cluster_list)-2) and cluster_list[i]==cluster_list[i+1]:
                count = count+1
                #i = i+1
            if count>count_max :
                count_max = count
                value = cluster_list[i]
                index = i-(count_max-1)
        count = 0
    print(value)
    print(index)

'''

def maxoccur(cl) :
    temp = groupby(cl)
    res = max(temp, key = lambda sub: len(list(sub[1])))
    #print(res)

    num_times, occurrence = max((len(list(values)), key) for key, values in groupby(cl))
    print("%d occurred %d times" % (occurrence, num_times))

    for i in cl :
        if i == occurrence :
            ind = cl.index(i)
            t= ind
            for j in range(num_times) :
                assert cl[t]==occurrence
                t=t+1

    print(ind)


# Begining of algorithm 
db = ['jacob','yacob','jaxob','sydny','sydni','sydney']
n = 2
S = 3

# Initializing
clustered_strings = []
clusters = []

#IS = []
cluster = {}
# Calling the func qgrams on every string in the database here. 
for alpha in db :
    #print(type(alpha))
    if alpha in clustered_strings :
        continue
    else :
        #B = []
        B = qgrams(alpha,n)

        # max border
        bm = len(B)

        # Initializing current cluster
        O = []

        for o in reversed(range(1,bm)) :  # 2.2
            #print(o)
            #k = []  #to store all the sample tuples
            
            for i in range(1,S+1) : # 2.2.1 
                tup = [] # to store one randomly generated tuple
                
                while len(tup) != o :  # 2.2.1.1
                    ki = random.choice(B)
                    if ki in tup :
                        continue
                    else :
                        tup.append(ki)
                tp = tuple(tup)  # one tuple generated here
                print(tp) 

                overlap = overlapStrings(tp) # 2.2.1.2
                print(overlap)

                '''
                temp = inverse_strings(tp[0],db)  # 2.2.1.2

                for ki in tp : 
                    inv_s = inverse_strings(ki,db)
                    temp = intersection(temp,inv_s)

                print(str(tp) + ': '+str(temp))
                '''
                O = union(O,overlap) 

                '''

                for j in range(1,o+1) : # 2.2.1.1
                    #print(random.choice(B))
                    tup.append(random.choice(B))
                print(tup)
             
                '''
            print('Union of threshold value '+ str(o))
            print(O)
            print('\n\n')

             #print("Center bag changes")

            # 2.2.2 
            print("Updating the center of cluster now")

            # collecting the contents of indexed O
            O_content = []
            histogram_dict = {}
            hist_list = []

            for i in O :
                O_content.append(db[i])

            # 2.2.2.1
            sum_a = 0
            for a in O_content :
                print(a)
                # Changing center bag here itsef ( !! Not sure)
                B = qgrams(a,2)
                sum_a += len(B) 
                for k in B :
                    #histogram_dict[k].append(1)
                    # forming a tuple to calculate histogram 
                    hist_list.append(k)
                    
            #print(hist_list)
            histogram_dict = count_qgrams(hist_list)
            #print(histogram_dict)

            # 2.2.2.2  ( to sort histogram_dict by values )
            sorted_hist = dict(sorted(histogram_dict.items(), key=operator.itemgetter(1),reverse=True))
            print(sorted_hist)

            # 2.2.2.3 
            A = int(sum_a/len(O_content))
            print(A)
            #print(O_content)

            # 2.2.2.4
            B = extract_bag(sorted_hist,A)
            print(B) 

            # 2.2.3 
            cluster[o] = B

        # 2.3 
        print("Printing the cluster[]\n")
        print(cluster)
        # finding the longest sequence ib to ib + delta 
        cluster_len = []
        for key in cluster : 
            cluster_len.append(len(cluster[key]))

        print(cluster_len)  # contains the length of all the elements

        #longest_sequence(cluster_len)
        maxoccur(cluster_len) # gives the index of the occurence of longest sequence









