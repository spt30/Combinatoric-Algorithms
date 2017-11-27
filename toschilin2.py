import copy

def find_start_x():
    # print('FIND')
    for i in range(k):
        if (source[i] == 0 and source_used[i] != 2):
            # print('FINDRESULT', i)
            source_used[i] += 1;
            return i+1;
    # print('FINDRESULT NO FIND')
    return 0;

def dfs_x(start):
    # print('DFSX', start)
    i = 0
    complementary_chain = False
    while (not(complementary_chain) and i < l):
        if (flow[start][i] == 0):
            if (dfs_y_t(i)):
                source[start] = 1;
                flow[start][i] = 1;
                effluent[i] = 1;
                complementary_chain = True;
                # print('DFSXRESULT', start, '-> ', i)
        i+=1
    if(not(complementary_chain)):
        i = 0
        while (not(complementary_chain) and i < l):
            if (flow[start][i] == 0):
                if (dfs_y(i)):
                    source[start] = 1;
                    flow[start][i] = 1;
                    effluent[i] = 1;
                    complementary_chain = True;
                    # print('DFSXRESULT', start, '-> ', i)
            i+=1
    # print('DFSXRESULT', start, complementary_chain)
    return complementary_chain

def dfs_y_t(start):
    # print('DFSY_T', start)
    if effluent[start] == 0:
        # print('DFSYRESULT', start, '-> t')
        return True;
    
def dfs_y(start):
    for i in range(k):
        if flow[i][start] == 1:
            if(dfs_x(i)):
                flow[i][start] = 0
                # print('DFSY', start, '-> X', i)
                return True;
    # print('DFSYRESULT', start, 'NO FREE EDGES')
    return 0;

input_file = open("in.txt", "r")
count_x_y = input_file.readline().split(' ')
array_of_string = []
k = int(count_x_y[0])
l = int(count_x_y[1])
i = 0
while i < k:
    array_of_string.append(input_file.readline())
    i+=1
input_file.close()
matrix = []
flow = []
for x in range(k):
    array_for_one_string = array_of_string[x].split(' ')
    if x != k-1:
        array_for_one_string[l-1] = array_for_one_string[l-1][:-1]
    # print(array_for_one_string)
    matrix.append(copy.copy(array_for_one_string))
    flow.append(copy.copy(array_for_one_string))

# print(matrix)
# print(flow)
# print('\n')
for i in range(k):
    for j in range(l):
        matrix[i][j] = int(matrix[i][j])
        flow[i][j] = int(flow[i][j]) - 1;
source = []
effluent = []
for s in range(k):
    source.append(0)
for t in range(l):
    effluent.append(0)
# print(source)
# print(flow)
# print(effluent)
# print('\n')
source_used = []
for x in range(k):
    source_used.append(0);
while(find_start_x()):
    # print(source)
    # print(flow)
    # print(effluent)
    # first = find_start_x() - 1
    # print(first)
    dfs_x(find_start_x() - 1)
    # print(source)
    # print(flow)
    # print(effluent)
    # print('\n')
# print(source)
print(flow)
# print(effluent)
# print('\n')
output = []
output_file = open("out.txt", "w")
# output_file.write('[')
print(k, l)
for i in range(k):
    output.append(1)
    j = 0
    while (j < l and flow[i][j] != 1):
        print(i, j, l, flow[i][j])
        output[i] += 1
        j += 1
    if output[i] == l+1:
        output[i] = 0
        # print(i, j, l, flow[i][j])
    # output_file.write(str(output[i])
output_file.write(str(output))
# output_file.write(']')
# print(output)
output_file.close()

