# coding:utf-8
"""
单个文件去重，重复行数简单记录在log.txt文件
"""
read_file = "elwb/wubi86_trans.txt"
write_file = "elwb/repeat.txt"
dic = {}
with open(read_file, 'rb') as rf:
    with open("elwb/log.txt", 'w') as wlog:
        for i, line in enumerate(rf):
            if line in dic:
                wlog.write(str(i)+'\n')
                continue
            else:
                dic[line] = i
    
with open(write_file, 'wb') as wf:
    for k in dic:
        wf.write(k)

print('done')