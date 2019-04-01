#coding=utf-8
s=''
str=u'we大厦都，是r324驱蚊器wer'
for w in str:
    if  w>= u'\u4e00' and w<=u'\u9fa5':
        s+=w
print s
 
大厦都是驱蚊器
 
根据编码判断是否为中文，对中文标点符号无效