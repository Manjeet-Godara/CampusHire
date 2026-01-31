def create_n_grams(file_string,constraint):
    n=len(file_string)
    n_grams=[]

    if n<=constraint:
        n_grams.append(file_string)
    else:   
        for i in range(n-constraint+1):
            current=""

            for j in range(constraint):
                current+=file_string[i+j]
        
            n_grams.append(current)

    return n_grams 

def jaccards_similarity(list1,list2):
    n1=len(list1)
    n2=len(list2)

    if n1==0 or n2==0:
        return 0
    
    n_grams_1={}

    for i in range(n1):

        if list1[i] not in n_grams_1:
            n_grams_1[list1[i]]=0
        n_grams_1[list1[i]]+=1
    
    inter_count=0
    union_count=n2

    for i in range(n2):

        if list2[i] in n_grams_1:
            n_grams_1[list2[i]]-=1
            inter_count+=1

            if n_grams_1[list2[i]]==0:
                del n_grams_1[list2[i]]
    
    union_count+=len(n_grams_1)

    return ((inter_count)*100)/union_count

