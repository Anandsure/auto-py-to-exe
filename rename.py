from glob import glob
from os import rename
for fname in glob('*.jpeg'):
    t=''
    for i in fname:
        if i !='.':
            t+=i
        else:
            break
    rename(fname, t+'.anand')
for fname in glob('*.png'):
    t=''
    for i in fname:
        if i !='.':
            t+=i
        else:
            break
    rename(fname, t+'.anand')
for fname in glob('*.jpg'):
    t=''
    for i in fname:
        if i !='.':
            t+=i
        else:
            break
    rename(fname, t+'.anand')