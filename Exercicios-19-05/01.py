from random import sample

TRANSFORM_UPPER = 1
TRANSFORM_LOWER = 2

def embaralhar_string(texto, transform=TRANSFORM_UPPER):
  string_embaralhada = ''.join(sample(texto, len(texto)))
  
  if transform == TRANSFORM_UPPER:
    string_embaralhada = string_embaralhada.upper()
  elif transform == TRANSFORM_LOWER:
    string_embaralhada = string_embaralhada.lower()
  else:
    raise ValueError("Opção de transformação inválida.")
  
  return string_embaralhada

print(embaralhar_string('João'))
print(embaralhar_string('José', transform=TRANSFORM_LOWER))
