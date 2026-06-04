import numpy as np

def calculate_divergence(p1, p2):
    """
    Llogarit distancen Euklidiane midis dy trajektoreve.
    Mat ndjeshmerine ndaj kushteve fillestare.
    """
    return np.sqrt((p1[0] - p2[0])*2 + (p1[1] - p2[1])*2)

def analyze_sensitivity(model_func, start_point, delta=1e-5, steps=50):
    """
    Gjurmon si distanca midis dy pikave rritet gjate iteracioneve.
    Konfirmon sjelljen kaotike te sistemit.
    """
    p1 = start_point
    p2 = (start_point[0] + delta, start_point[1])
    divergences = []
    
    for _ in range(steps):
        p1 = model_func(*p1)
        p2 = model_func(*p2)
        div = calculate_divergence(p1, p2)
        divergences.append(div)
    return divergences
