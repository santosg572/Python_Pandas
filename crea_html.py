
def H1(t1=''):
  h1 = '<h1>' + t1 + '</h1>' 
  fil.write(h1)

def P(t1=''):
  p1 = '<p>' + t1 + '</p>'
  fil.write(p1)

file = 'prueba.html'
fil = open(file, 'w')

c1 = '''
<!DOCTYPE html>
<html>
<head>
'''

t1 = 'hola'

fil.write(c1)

title = '<title>' + t1 + '</title>'

fil.write(title)

body = '''
</head>
<body>
'''

fil.write(body)

t1 = 'This is a Heading'

h1 = '<h1>' + t1 + '</h1>'

fil.write(h1)

H1('hola')

t2 = 'This is a paragraph.'

p1 = '<p>' + t2 + '</p>'

fil.write(p1)

resto = '''
</body>
</html>
'''

fil.write(resto)

