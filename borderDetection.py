'''
    Function to compute qgrams(). 
    It takes a single string as i/p and returns a list with qgrams
'''
import random

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


# Begining of algorithm 
db = ['jacob','yacob','jaxob','sydny','sydni','sydney']
n = 2
S = 3

# Initializing
clustered_strings = []
clusters = []

IS = []

# Calling the func qgrams on every string in the database here. 
for alpha in db :
    #print(type(alpha))
    if alpha in clustered_strings :
        continue
    else :
        B = []
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
                #print(tp) 

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


#print(IS)
#print(tp)

  #  print(B)
