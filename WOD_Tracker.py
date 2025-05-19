
from Route import *
from Login import *

treinos = []
listaDeCadastro = []
arquivo = "valores.txt"
usuario = 0
cadastrado = 0

try:
    valores = eval(load(arquivo))
except:
    valores = []
