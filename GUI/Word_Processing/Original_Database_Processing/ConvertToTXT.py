file = "words_dictionary [MCOnverter.eu].txt"
f = open(file,"r")
file_list = [open("a_f.txt", "w"),open("b_f.txt", "w"),open("c_f.txt", "w"),open("d_f.txt", "w"),open("e_f.txt", "w"),open("f_f.txt", "w"),open("g_f.txt", "w"),open("h_f.txt", "w"),open("i_f.txt", "w"),open("j_f.txt", "w"),open("k_f.txt", "w"),open("l_f.txt", "w"),open("m_f.txt", "w"),open("n_f.txt", "w"),open("o_f.txt", "w"),open("p_f.txt", "w"),open("q_f.txt", "w"),open("r_f.txt", "w"),open("s_f.txt", "w"),open("t_f.txt", "w"),open("u_f.txt", "w"),open("v_f.txt", "w"),open("w_f.txt", "w"),open("x_f.txt", "w"),open("y_f.txt", "w"),open("z_f.txt", "w")]
word_list = []
a_l = []
b_l = []
c_l = []
d_l = []
e_l = []
f_l = []
g_l = []
h_l = []
i_l = []
j_l = []
k_l = []
l_l = []
m_l = []
n_l = []
o_l = []
p_l = []
q_l = []
r_l = []
s_l = []
t_l = []
u_l = []
v_l = []
w_l = []
x_l = []
y_l = []
z_l = []
all_l = [a_l,b_l,c_l,d_l,e_l,f_l,g_l,h_l,i_l,j_l,k_l,l_l,m_l,n_l,o_l,p_l,q_l,r_l,s_l,t_l,u_l,v_l,w_l,x_l,y_l,z_l]
all_d = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
alphabet = "abcdefghijklmnopqrstuvwxyz"
for line in f:
    if('"' in line):
        word = line[line.index('"')+1:line.rindex('"')].lower()
        for i in range(0,26):
            if(alphabet[i] in word):
                all_d[i][word] = 1
        word_list.append
for i in range(0,26):
    all_l[i] = list(all_d[i].keys())
    all_l[i].sort()
    file_list[i].write("\n".join(all_l[i]))

f.close()
for item in file_list:
    item.close()

print("Done")
    
    
