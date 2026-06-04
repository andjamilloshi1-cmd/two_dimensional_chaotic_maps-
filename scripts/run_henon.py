import sys import os
# Shtojme rrugen e projektit per te importuar
modulet nga dosja src
sys. path. appena(os •path. abspath (os.path. join(os
•path dirname(_file), ' •.')))
from src.models.henon import henon mar from src.visualization phase_maps import
plot_phase_space
def run ():
# Parametrat fillestare per simulimin
x, y = 0.1, 0.1
*_lista
=[]
Y_lista = []
# Simulimi per 10,000 hapa per te
formuar atraktorin
print ( "Duke llogaritur harten e
Henonit……"'）
for i in range (10000) :
x, y = henon_map (x, y)
x lista.append (x)
y_ lista. append (y)
# Gjenerimi i grafikut
plot phase space(x_lista, y_lista,
"Atraktori i Henonit")
print ( "Simulimi perfundoi me sukses.")
if
name run ()
main ":
