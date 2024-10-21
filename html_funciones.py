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

def H2(t1=''):
  h1 = '<h2>' + t1 + '</h2>'
  fil.write(h1)

def H3(t1=''):
  h1 = '<h3>' + t1 + '</h3>'
  fil.write(h1)

def H4(t1=''):
  h1 = '<h4>' + t1 + '</h4>'
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

# ===================================================================
# inicio

file = 'prueba.html'
fil = open(file, 'w')

doctype()
title('holas')
body()

H2('Ejercicio 1.')
H3('Crear un data-frame en pandas-python y guardarlo en un archivo CSV con la siguiente información.')

fil.write('<font size="5">')

lista_ordenada(list1)

fil.write('</font>')

H2('Ejercicio 2.')
H3('Leer el archivo CSV previamente guardado y hacer las instrucciones correspondientes para calcular losiguiente:')

fil.write('<font size="5">')

lista_ordenada(list2)

fil.write('</font>')

resto()


