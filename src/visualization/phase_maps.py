import matplotlib.pyplot as plt
def plot_phase_space(x_list, y_list, title):
    # Vizaton grafikun e shperndarjes
    plt.figure(figsize=(8, 6))
    plt.scatter(x_list, y_list, s=0.1, color='blue')
    plt.title(title)
    plt.grid(True)
    plt.show()
