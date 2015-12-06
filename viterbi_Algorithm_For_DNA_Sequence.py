
#---------------------------------------------------
#Implement Viterbi Algorithm
#----------------------------------------------------

#Author : Sai Chandesh Gurramkonda


import math


#To save transition probabilities

def trans_prob(states):
    
    print "\nEnter the transition probabilities as s1s1,s1s2...snsn-1,snsn"
    for i in range(states):
        for j in range(states):
            x = input("\nEnter the value : ")
            trans[i][j]=x


# To save initial probabilites

def init_prob(states):
    print "\nEnter the initial probabilities for all the states"
    for i in range(states):
        x = input("\nEnter the value : ")
        init.append(x)
    
    

#To save the emission probailities

def emiss_prob(states,feat):


    print "\nEnter the emission probabilities as p(A|s1),p(C|s1),p(G|s1)...p(C|s2),p(G|s2),p(T|s2)"
    for i in range(states):
        for j in range(feat):
            x = input("\nEnter the value : ")
            ems[i][j]=x
    


#Get the states

def get_states(states):
    print "\nEnter the name of the hidden states"
    for i in range(states):
        p = "\nState"+str(i+1)+" : "
        x = raw_input(p)
        state[x]= i



# Get the features

def get_Features(feature):
    print "\nEnter the name of the features"
    for i in range(ftr):
        p = "\nFeature"+str(i+1)+" : "
        x = raw_input(p)
        features[x]= i


#backtrack algorithm

def back_track(index,counter):
    track = []
    if counter == 0 :
        return -1
    else :
        for i in range(total_states):
            x = output[i][index-1]
            y = trans[index][i]
            z = x * y
            track.append(z)
        max_res = track[0]
        answer_index = 0
        for i in range(total_states):
            if track[i] > max_res :
                max_res = track[i]
                answer_index = i
        
        for k,v in state.items():
            if v == answer_index :
                ans_index = k
            
        backtrack.append(ans_index)

        counter = counter -1

        back_track(answer_index,counter)




        


# viterbi function

def viterbi(t,states):
    f1 = sequence[0]
    for key in features:
        if key == f1 :
            val = features[key]
    for d in range(states):
        x = ems[d][val]
        y = init[d]
        output[d][0] = x * y
    
    temp= []
    for i in range(1,t):
        f1 = sequence[i]
        for key in features:
            if key == f1 :
                val = features[key]
        for c in range(states):
            x = ems[c][val]
            for j in range(states):
                y = output[j][i-1]
                z = trans[c][j]
                q = y * z
                temp.append(q)
            maximum = temp[0]
            index = 0
            for j in range(states):
                if temp[j] > maximum :
                    maximum = temp[j]
                    
            temp=[]
            
        
            output[c][i] = x * maximum

    result = output[0][t-1]
    res_index = 0
    for i in range(1,states):
        if output[i][t-1] > result :
            result == output[i][t-1]
            res_index = i

    
    print "\nViterbi matrix :\n"
    for k,v in state.items():
        if v == res_index :
            ans_index = k
    backtrack.append(ans_index)

# Output

    for i in range(t):
        f1 = sequence[i]
        for j in range(states):
            for k,v in state.items():
                if v == j:
                    print "\nP%s(%s,%d) : %.6f" %(k,f1,(i+1),output[j][i])
           
          
        


    
    print "\nMost likely hidden states at each step are : "
#implement back track algorithm
    count = t-1
    back_track(res_index,count)

    rev = t-1
    

    for i in range(t):

        print "\nStep - %d : %s"%((i+1),(backtrack[rev]))
        rev-=rev




        
            
#Main (Program Strats From Here)


backtrack = []
init = []
features = {}
state = {}

answer_index =0

total_states = input("Enter the number of states in the Hidden Markov Model\t: ")

get_states(total_states)
ftr= input("\nEnter the number of features : ")



trans = [[0]*total_states for i in range(total_states)]
ems = [[0]*ftr for i in range(total_states)]

get_Features(ftr)



init_prob(total_states)
trans_prob(total_states)
emiss_prob(total_states,ftr)


sequence = raw_input("\nEnter the sequence : ")
length = len(sequence)
output = [[0]*length for i in range(total_states)]


viterbi(length,total_states)




