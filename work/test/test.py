n = input('请输入金额(0<n<100000)：')
length =len(n)
n = int(n)
s = ''
w = int(n/10000)
k = int((n%10000)/1000)
h = int((n%1000)/100)
t = int((n%100)/10)
g = n%10
list1 = [0,g,t,h,k,w]
table = ['','壹','贰','叁','肆','伍','陆','柒','捌','玖']
match length:
    case 1:
        s+=table[g]
    case 2:
        s+=table[t]+'拾'+table[g]
    case 3:
        s+=table[h]+'百'
        if t==0 and g!=0:
            s+='零'+table[g]
        else:
            s+=table[t]+'拾'+table[g]
    case 4:
        s+=table[k]+'千'
        if t==0 and h==0 and g!=0:
            s+='零'+table[g]
        if t!=0:
            if h!=0:
                s+=table[h]+'百'+table[t]+'拾'+table[g]
            else:
                s+='零'+table[t] +'拾'+table[g]
        else:
            s+=table[h]+'百'
    case 5:
        s+=table[w]+'万'
        if k==0 and h!=0 and t==0:
            if g==0:
                s+='零'+table[h]+'百'
            else:
                s+='零'+table[h]+'百零'+table[g]
        if k==0 and t!=0:
            if h==0:
                s+='零'+table[t]+'拾'+table[g]
            else:
                s+='零'+table[h]+'百'+table[t]+'拾'+table[g]
        if k!=0 and t!=0:
            if h==0:
                s+= table[k]+'千零' + table[t] + '拾' + table[g]
            else:
                s += table[k] + '千' +table[h] + '百' + table[t] + '拾' + table[g]
        if k!=0 and t==0 and g!=0:
            if h==0:
                s += table[k] + '千零' + table[g]
            else:
                s += table[k] + '千' + table[h] + '百零'+ table[g]
        if k!=0 and t==0 and g==0:
            if h==0:
                s += table[k] + '千'
            else:
                s += table[k] + '千' + table[h] + '百'
        if k==0 and t==0 and h==0 and g!=0:
            s += '零' + table[g]
print(s+'元')



