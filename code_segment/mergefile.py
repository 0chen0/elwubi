read_file1 = "elwb/ww1.txt"
read_file2 = "elwb/ww2.txt"
write_file = "elwb/repeat.txt"
dic = {}
with open(read_file1, 'rb') as rf1:
    
    for i, line in enumerate(rf1):
        if line in dic:            
            continue
        else:
            dic[line] = i

with open(read_file2, 'rb') as rf2:
    
    for i, line in enumerate(rf2):
        if line in dic:            
            continue
        else:
            dic[line] = i

    
with open(write_file, 'wb') as wf:
    for k in dic:
        wf.write(k)

print('done')