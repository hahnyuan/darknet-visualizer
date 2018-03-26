def read_option(l,current):
    if '=' in l:
        l=l.split('=')
        current[l[0].strip()]=l[1].strip()
def read_cfg(filename):
    file=open(filename,'r')
    options=[]
    current={}
    for i in file.readlines():
        #print(i)
        if(i[0]=='['):
            options.append(current.copy())
            current.clear()
            current['type']=i.split(']')[0][1:]
            pass
        elif(i[0] in ['\0','#',';']):
            pass
        else:
            read_option(i,current)
    file.close()
    return options[1:]