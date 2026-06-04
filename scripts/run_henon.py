import sys
import os
# Vendos shtegun për të gjetur dosjen src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))
from src.models.henon import henon_map
from src.visualization.phase_maps import plot_phase_space

def run():
    x, y = 0.1, 0.1
    x_lista = []
    y_lista = []
    
    # Simulimi
    for i in range(10000):
        x, y = henon_map(x, y)
        x_lista.append(x)
        y_lista.append(y)
        
    # Ruajtja e figurës (kjo të duhet për "Figurat kryesore")
    plot_phase_space(x_lista, y_lista, "Atraktori i Henonit", filename="henon_plot.png")

if _name_ == "_main_":
    run()
