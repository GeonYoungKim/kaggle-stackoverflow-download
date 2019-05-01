import re
str="""
a c|v^b\n
geonyeong
"""
str=re.sub('\n','@', str)
str=re.sub('\t',' ', str)
str=re.sub('<(/)?([a-zA-Z]*)(\\s[a-zA-Z]*=[^>]*)?(\\s)*(/)?>',' ',str)
str=re.sub('[^\\uAC00-\\uD7A3xfe0-9a-zA-Z<>:|@\\\\s]',' ', str)
str=re.sub(' +', ' ', str)
print(str)