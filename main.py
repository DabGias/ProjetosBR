import requests

from CEP import CEP

cep = 12345678
objeto_cep = CEP(cep)
a = objeto_cep.acessa_via_cep()
print(a)
