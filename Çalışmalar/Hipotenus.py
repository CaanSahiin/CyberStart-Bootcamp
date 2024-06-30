import math

# Noktaların tanımlanması
points = [(1, 2), (3, 5), (7, 8), (4, 6)]

# Öklid Mesafesi için Fonksiyon Tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mesafelerin Hesaplanması ve Minimum Mesafenin Bulunması
def findMinimumDistance(points):
    n = len(points)
    if n < 2:
        return None
    
    # Başlangıçta minimum mesafe sonsuz kabul edilir
    min_distance = float('inf')

    # Her bir nokta çifti arasındaki mesafeleri hesapla
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclideanDistance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
    
    return min_distance

# Minimum mesafenin bulunması
min_distance = findMinimumDistance(points)

# Sonucun Yazdırılması
print("Verilen noktalar arasındaki minimum Öklid mesafesi:", min_distance)
