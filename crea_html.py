def doctype():
  c1 = '''
  <!DOCTYPE html>
  <html>
  <head>
  '''

  fil.write(c1)

def title(tit=''):
  title = '<title>' + tit + '</title>'
  fil.write(title)

def body():
  body1 = '''
  </head>
  <body>
  '''
  fil.write(body1)

def H1(t1=''):
  h1 = '<h1>' + t1 + '</h1>' 
  fil.write(h1)

def P(t1=''):
  p1 = '<p>' + t1 + '</p>'
  fil.write(p1)

def lista_ordenada(lista=''):
  fil.write('<ol>')

  for ss in lista:
    s = '<li>' + ss + '</li>'
    fil.write(s)

  fil.write('</ol>')


def resto():
  resto = '''
  </body>
  </html>
  '''
  fil.write(resto)

# inicio

file = 'prueba.html'
fil = open(file, 'w')

doctype()
title('holas')
body()

H1('hola')

fil.write('<font size="5">')

P('hola')

list = ['uno', 'dos', 'tres', 'cuatro']

lista_ordenada(list)
fil.write('</font>')

resto()


