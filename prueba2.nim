import rdstdin

var list: seq[string]
var str = readLineFromStdin("Cual es tu Nombre? ")

if str.len > 0:
  list.add str
  while str.len > 0:
    str = ""
    str = readLineFromStdin("Agrega mas Nombres?,o presiona ENTER ")
    if str.len > 0: list.add str

for name in list: echo name