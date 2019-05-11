#coding:utf-8

read_file1 = "elwb/t1.txt"
read_file2 = "elwb/t2.txt"
write_file = "elwb/unique.txt"
str1 = []
str2 = []
str3 = []
with open(read_file1, 'r', encoding='UTF-8') as rf1, open(read_file2, 'r', encoding='UTF-8') as rf2, open(write_file, 'w', encoding='UTF-8') as wf:
    for line in rf1:
        if '\xef\xbb\xbf' in line:
            s1 = line.replace('\xef\xbb\xbf','')
            str1.append(s1.strip())
        else:
            str1.append(line.strip())
    
    for line in rf2:
        if '\xef\xbb\xbf' in line:
            s1 = line.replace('\xef\xbb\xbf','')
            str2.append(s1.strip())
        else:
            str2.append(line.strip())

    for i in str2:
        if i in str1:
            continue
        str3.append(i)
    print(len(str3))
    for j in str3:
        wf.write(j+'\n')