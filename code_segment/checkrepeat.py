#coding:utf-8
"""
遍历文件，删除另一文件与之相同的内容
"""
read_file1 = "elwb/t2.txt"
read_file2 = "elwb/t1.txt"
write_file = "elwb/unique.txt"
"""
with open(read_file1, 'rb') as rf1, open(read_file2, 'rb') as rf2, open(write_file, 'wb') as wf:
#with open(read_file1, 'r', encoding='UTF-8') as rf1, open(read_file2, 'r', encoding='UTF-8') as rf2, open(write_file, 'w', encoding='UTF-8') as wf:
    for line, i in enumerate(rf1):
        if line > 13: break
        print(str(line)+'\r', end='')
        
        unic = True
        for j in rf2:
            if i == j:
                print(i, j)
                unic = False
                break
        if unic:
            wf.write(i)


print(line)
print('done.')
"""
with open(read_file1, 'rb') as rf1, open(read_file2, 'rb') as rf2, open(write_file, 'wb') as wf:
    for _ in range(13):
        ii = rf1.readline()
        jj = rf2.readline()
        print(ii, jj)