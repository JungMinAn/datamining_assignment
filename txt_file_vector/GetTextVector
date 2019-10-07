import os
from konlpy.tag import Twitter
from collections import defaultdict, Counter
from math import log
directory = "./thirdassignment/"
indexfile = "index.txt"
idxf = open(indexfile, 'w')
ntdict = defaultdict(int)
files = os.listdir(directory)
filenum = 0
for file in files:
    if (".txt" not in file) and (".TXT" not in file):
        continue
    filenum += 1
    with open(directory + file, 'r', -1, "utf-8") as openfile:
        filetext = openfile.read()
        twit = Twitter()
        fnouns = twit.nouns(filetext)
        fset = set(fnouns)
        for n in fset:
            ntdict[n] +=1
    openfile.close()
ntindexlist = sorted(ntdict.items(), key=lambda x: x[1], reverse=True)
for i in range(len(ntindexlist)):
    ntindexlist[i] = ntindexlist[i][0]
for i in ntindexlist:
    idxf.write('{} {}\n'.format(i, ntdict[i]))
idxf.close()
files = os.listdir("./thirdassignment/")
resultfile = "word.txt"
rstf = open(resultfile, 'w')
vectorfile = "vector.txt"
tvf = open(vectorfile, 'w')
for file in files:
    if (".txt" not in file) and (".TXT" not in file):
        continue
    with open(directory + file, 'r', -1, "utf-8") as openfile:
        filetext = openfile.read()
        twit = Twitter()
        fnouns = twit.nouns(filetext)
        count = Counter(fnouns)
        for index, value in enumerate(ntindexlist):
            if value in count:
                rstf.write('{}:{} '.format(value, count[value]))
                wordvector = count[value] * log(filenum/ntdict[value], 2)
                tvf.write('{}:{} '.format(index, wordvector))
    openfile.close()
    rstf.write("\n\n")
    tvf.write("\n\n")
rstf.close()
tvf.close()
