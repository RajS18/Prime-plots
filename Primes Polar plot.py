import matplotlib.pyplot as plt
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def plot_primes(max_num):
    primes = [n for n in range(max_num) if is_prime(n)]
    angles = [(360/(2*math.pi))*i for i in primes]
    radii = primes

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
    ax.scatter(angles, radii)
    ax.set_rticks([])  # Remove radial tick labels if not necessary
    ax.set_title('Prime Numbers in Polar Coordinate System')

    plt.show()

max_number = 10000
plot_primes(max_number)
