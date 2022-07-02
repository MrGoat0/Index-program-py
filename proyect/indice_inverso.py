def low(z):
    return z.lower()
def first(z):
    return z[0]
def squish(x):
    s=set(x)
    return sorted([(i,x.count(i)) for i in s], key=first)

def clean(x):
    y=''
    s=['.',',','-','.pdf','.PDF','_','el', 'la', 'y', 'Los', 'los']
    for i in x:
        if i in s:  
            continue
        else:
            y+=i
    return y

d=dict()
ln=0
for line in open('prueba.txt'):
    ln+=1
    line=clean(line)
    l=line.split()
    for word in l:
        if word not in d:
            d[word]=[]
            d[word].append(1)
            d[word].append([ln])
        else:
            d[word][0]+=1
            d[word][1].append(ln)

print('list of d')
ld=list(d)
ld.sort(key=low)
for k in ld:
    print(k,d[k][0],squish(d[k][1]))
