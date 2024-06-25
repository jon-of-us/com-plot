# %%
import polya
import numpy as np
import matplotlib.pyplot as plt


# %%
def f(z):
    z = z * 1j
    res = 1
    for i in range(3, 4):
        res *= 1 / (np.exp(z / i) - 1)
    return res
    # return 1 / z


polya.streamplot(
    f,
    y_space=np.linspace(-2, 2, 50),
    x_space=np.linspace(-30, 30, 100),
    vector_density=5,
)
plt.show()

# %%
