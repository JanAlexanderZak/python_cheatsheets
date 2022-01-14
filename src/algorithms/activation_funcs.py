import matplotlib.pyplot as plt
import numpy as np


def step(z):
    return np.sign(z)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def relu(z):
    return np.maximum(0, z)


def derivative(func, _x, delta=1e-10):
    return (func(_x + delta) - func(_x)) / delta


x = np.linspace(-5, 5, 200)
axis_limits = [-5, 5, -1.5, 1.5]
fig, axs = plt.subplots(ncols=2, figsize=(14, 7))
axs[0].plot(x, step(x), "--", label="Step")
axs[0].plot(x, sigmoid(x), label="Sigmoid")
axs[0].plot(x, np.tanh(x), label="Tanh")
axs[0].plot(x, relu(x), "-.", label="ReLU")
axs[0].legend(loc="lower right")
axs[0].set_title("Activation functions")
axs[0].axis(axis_limits)
axs[0].grid(True)

axs[1].plot(x, derivative(np.sign, x), "--", label="Step")
axs[1].plot(x, derivative(sigmoid, x), label="Sigmoid")
axs[1].plot(x, derivative(np.tanh, x), label="Tanh")
axs[1].plot(x, derivative(relu, x), "-.", label="ReLU")
axs[1].legend(loc="lower left")
axs[1].set_title("Derivatives of activations")
axs[1].axis(axis_limits)
axs[1].grid(True)
plt.show()