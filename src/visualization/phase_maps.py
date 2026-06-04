import matplotlib.pyplot as plt

def plot_phase_space(x_list, y_list, title, filename=None):
    """
    Vizualizon hapesiren e fazes dhe ruan grafikun ne nje skedar.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(x_list, y_list, s=0.1, color='blue', marker='.')
    plt.title(title)
    plt.xlabel("Pozicioni (x)")
    plt.ylabel("Momenti / Y (p/y)")
    plt.grid(True, linestyle='--', alpha=0.6)
    
    if filename:
        plt.savefig(filename)
    plt.show()
