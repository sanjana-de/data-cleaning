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
This function counts the longest sequence in the input list 
and returns the index of the 1st occurence of sub-sequence. 

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
    return ind 

'''
Function to convert q-grams to string 
'''
def qgrams_to_strings(some_list,n) :
    str = ""
    for q in some_list :
        str += q[:n-1]
        qgram_length = len(q)
        
    if(str[0]=='#' and str[len(str)-1]=='$') :
        str = str[1:-1]

    if(str[0]=='#') :
        str = str[1:]

    if str[len(str)-1]=='$' :
        str = str[:-1] 

    #print(str)
    return str 
    


# Begining of algorithm 
# db = ['jacob','yacob','jacob','jacob','jacob','jaxob','sydney','sydney','sydnei','sydnoy','sydney']
db = ['kolkata','kolkata','kolkata','kolkota','kalkata','kolkata','delhi','delhi','delli','dilli','delhi','delhi'] 
n = 2
S = 3

# Initializing
clustered_strings = []
clusters = []

#IS = []
cluster = {}

#O_content = []
#histogram_dict = {}
#hist_list = []

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

               
                O = union(O,overlap) 


            #print('Union of threshold value '+ str(o))
            print("union of threshold value :")
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
        index_ib = maxoccur(cluster_len) # gives the index of the occurence of longest sequence

        # 2.4 update clustered_strings
        cluster_values = list(cluster.values())
        cluster_ib_list = cluster_values[index_ib]
        print(cluster_ib_list)

        #clustered_strings.append(cluster_ib_list)
        #print(clustered_strings)
        cluster_ib_str = qgrams_to_strings(cluster_ib_list,2)
        clustered_strings.append(cluster_ib_str)
        print("printing clustered strings : ")
        print(clustered_strings) 


        # 2.5 updating clusters
        clusters.append(cluster_ib_list)
        #clusters = union(clusters,cluster_ib_list)
        print(clusters)

        # 2.6 emptying h[k], O, B
        B = []
        O = []
        histogram_dict = {}
        sorted_hist = {}
        hist_list = [] 
        
# 3 
# printing the clusters only
print("Clusters formed are: ")
print(clusters) 

indexlist = []
new_clust = []  # to store the clusters in a list

for i in range(len(clusters)) : 
    ci = clusters[i]
    clust_i = []    # to store the current formed cluster ci 
    if i not in indexlist :
        clust_i.append(ci)
    
    for j in range(i+1,len(clusters)) :
        cj = clusters[j]
        intersect = intersection(ci,cj)

        if len(intersect)!= 0 and j not in indexlist : 
            # print(intersection(ci,cj))
            clust_i.append(cj)
            indexlist.append(j) 

    #print(clust_i)
  
    if len(clust_i) != 0 :
        new_clust.append(clust_i)


print(new_clust)

# 4 


