
def ala_scan(sequence):
    input_list = list(sequence.upper())
    clean_list=[]
    for i in input_list:
        if i != ' ':
            clean_list.append(i)

    output_list = [';Alanine Scan','\n',''.join(map(str,clean_list)),' ;Control','\n']
    my_row = []
    for i in range(0,len(clean_list)):
        for j in range(0,len(clean_list)):
            if i == j:
                if clean_list[j] == 'A':
                    my_row.append('G')
                else:
                    my_row.append('A')
            else:
                my_row.append(clean_list[j])
        output_list.append(''.join(map(str, my_row)))
        output_list.append('\n')
        my_row = []
    output_str = ''.join(map(str, output_list))
    return output_str

#-------------------------------

def n_trunc(sequence):
    input_list = list(sequence)
    clean_list=[]
    for i in input_list:
        if i != ' ':
            clean_list.append(i)
    
    output_list = [';N-terminal Truncation','\n',''.join(map(str, clean_list))+' ;Control','\n']
    my_row = []
    c=1
    for i in range(0,len(clean_list)):
        if c <= (len(clean_list)-5):
            my_row.append(''.join(map(str, clean_list[c:len(clean_list)])))
            my_row.append('\n')
            c += 1
            output_list.append(''.join(map(str, my_row)))
            my_row = []
    return ''.join(map(str, output_list))

#-------------------------------
def c_trunc(sequence):
    input_list = list(sequence)
    clean_list=[]
    for i in input_list:
        if i != ' ':
            clean_list.append(i)
    
    output_list = [';C-terminal Truncation','\n',''.join(map(str, clean_list))+' ;Control','\n']
    my_row = []
    c=1
    for i in range(0,len(clean_list)):
        if c <= (len(clean_list)-5):
            my_row.append(''.join(map(str, clean_list[0:len(clean_list)-c])))
            my_row.append('\n')
            c += 1
            output_list.append(''.join(map(str, my_row)))
            my_row = []
    return ''.join(map(str, output_list))

#-------------------------------

def n_c_trunc(sequence):
    input_list = list(sequence)
    clean_list=[]
    for i in input_list:
        if i != ' ':
            clean_list.append(i)
    
    output_list = [';N- & C-terminal Truncation','\n',''.join(map(str, clean_list))+' ;Control','\n']
    my_row = []
    c=1
    for i in range(0,len(clean_list)):
        if 5 <= len(clean_list[c:len(clean_list)-c]):
            my_row.append(''.join(map(str, clean_list[c:len(clean_list)-c])))
            my_row.append('\n')
            c += 1
            output_list.append(''.join(map(str, my_row)))
            my_row = []
    return ''.join(map(str, output_list))
#---------------------------------------

def point_sub(sequence):
    input_list = list(sequence)
    clean_list=[]
    for i in input_list:
        if i != ' ':
            clean_list.append(i)

    my_row = []
    res_list = [';Point Substitutions','\n']
    aa_list = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
    for i in range(0,len(clean_list)):
        res_list.append(''.join(map(str, clean_list))+' ;Control')
        res_list.append('\n')
        for n in range(0,len(aa_list)):
            if clean_list[i] != aa_list[n]:
                for j in range(0,len(clean_list)):
                    if i == j:
                        my_row.append(aa_list[n])
                    else:
                        my_row.append(clean_list[j])
                res_list.append(''.join(map(str, my_row)))
                res_list.append('\n')
                my_row = []
        res_list.append('\n')
    return ''.join(map(str, res_list))
