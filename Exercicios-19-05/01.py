# embaralhar string

from random import sample

def embaralharString(texto, transform=1):
  embaralhado = sample(texto, len(texto))
  embaralhado = ''.join(embaralhado)
  
  if transform == 1:
    embaralhado = embaralhado.upper()
  elif transform == 2:
    embaralhado = embaralhado.lower()
  
  return(embaralhado)

print(embaralharString('João'))
print(embaralharString('José', 2))
  