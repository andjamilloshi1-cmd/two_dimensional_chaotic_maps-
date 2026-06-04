import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(*file*), '..')))
from src.models.standard_map import standard_map
from src.visualization.phase_maps import plot_phase_space
def run():
x, p = 0.1, 0.1
x_lista = []
p_lista = []
for i in range(5000):
x, p = standard_map(x, p)
x_lista.append(x)
p_lista.append(p)
plot_phase_space(x_lista, p_lista, "Standard Map")
if *name* == "*main*":
run()
