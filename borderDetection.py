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

                temp = inverse_strings(tp[0],db)  # 2.2.1.2
                #IS.append(inv_s)
                for ki in tp : 
                    inv_s = inverse_strings(ki,db)
                    temp = intersection(temp,inv_s)
                    #print(temp)

                print(str(tp) + ': '+str(temp))

                O = union(O,temp)
                #print('Union of')
                #print(O)
                '''

                for j in range(1,o+1) : # 2.2.1.1
                    #print(random.choice(B))
                    tup.append(random.choice(B))
                print(tup)
             
                '''
            print('Union of threshold value '+ str(o))
            print(O)
        print("Center bag changes")

            # 2.2.2 


#print(IS)
#print(tp)

  #  print(B)
