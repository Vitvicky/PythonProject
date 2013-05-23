import re

text='This is some text -- with punctuation.'
pattern = 'is'
print 'Text  :',text

m=re.match(pattern, text)
print 'Match :',m
s=re.search(pattern, text)
print 'search :',s