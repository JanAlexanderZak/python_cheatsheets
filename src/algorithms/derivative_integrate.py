import matplotlib.pyplot as plt
import numpy as np

delta = 1e-10
x_values = np.arange(-10, 10, 0.1)
to_power_n = 2


def f(x: np.ndarray, n=to_power_n, a=1, d=0, e=0) -> float:
    # f(x) = (a * (x - d) ** 2) + e
    return a * (x - d) ** n + e


def derive(func, x: np.ndarray) -> np.ndarray:
    # f'(a) = (f(a + h) - f(a)) / h
    return (func(x + delta) - f(x)) / delta


def integrate(func, x: np.ndarray) -> np.ndarray:
    # F(x) = (1 / 3) x ** 3 + C
    return (1 / (to_power_n + 1)) * func(x) * x + 0


def calc_area_under_curve(func, _borders: np.ndarray) -> float:
    print("b", integrate(func, _borders[1]))
    print("a", integrate(func, _borders[0]))
    return integrate(func, _borders[1]) - integrate(func, _borders[0])


borders = np.array([-2., 2.])
print(calc_area_under_curve(f, borders))

# Plot results
xlim = (-10, 10)
fig, axs = plt.subplots(3, figsize=(5, 20))

axs[0].plot(x_values, f(x_values, 2))
axs[0].set_title("f(x)")
axs[0].set_xlim(xlim)
axs[0].set_ylim(0, 100)

axs[1].plot(x_values, derive(f, x_values))
axs[1].set_title("f'(x)")
axs[1].set_xlim(xlim)

axs[2].plot(x_values, integrate(f, x_values))
axs[2].set_title("F(x)")
axs[2].set_xlim(xlim)
axs[2].set_ylim(-100, 100)

plt.tight_layout()
plt.show()
