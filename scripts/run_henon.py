import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(*file*), '..')))
from src.models.henon import henon_map
from src.visualization.phase_maps import plot_phase_space
def run():
x, y = 0.1, 0.1
x_lista = []
y_lista = []
for i in range(10000):
x, y = henon_map(x, y)
x_lista.append(x)
y_lista.append(y)
plot_phase_space(x_lista, y_lista, "Atraktori i Henonit")
if _name_ == "_main_":
run()
