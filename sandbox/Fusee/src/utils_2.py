import math
def points_dans_cercle(points, centre, rayon):
    cx, cy = centre
    for point in points:
        x, y = point
        distance = math.sqrt((x - cx)**2 + (y - cy)**2)
        if distance <= rayon:
            return False  # Au moins un point est à l'extérieur du cercle
    return True  # Tous les points sont à l'intérieur du cercle

# Exemple d'utilisation
points = [(1, 2), (3, 4), (5, 6)]
centre_cercle = (4, 5)
rayon_cercle = 3

if points_dans_cercle(points, centre_cercle, rayon_cercle):
    print("Tous les points sont à l'extérieur du cercle.")
else:
    print("Au moins un point est à l'intérieur ou sur le cercle.")
