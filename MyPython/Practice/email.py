import re
 
address=re.compile(
                   '''
                   [\w\d.+-]+     #username
                   @
                   ([\w\d.]+\.)+  #domin name prefix
                   (com|org|edu)
                   ''',
                   re.UNICODE | re.VERBOSE
                   )

candidates = [
    u'first.last@gmail.com',
    u'wssg1992@163.com',
    u'awdasdw@mail.example.com',
    u'awdawdada@example.foo',
              ]

for m in candidates:
    match = address.search(m)
    print '%-30s  %s' % (m,'matches' if match else 'no')
    
    