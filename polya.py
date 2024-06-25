import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import defaults


def vectorfield(
    f,
    x_space=defaults.x_space,
    y_space=defaults.y_space,
    vector_density=defaults.vector_density,
):
    """Plot the Polya vector field of complex function f."""
    x, y = np.meshgrid(x_space, y_space)
    z = x + 1j * y
    fz = f(z)
    norm = np.abs(fz)
    fz = np.where(norm < 1e-6, 1, fz / norm)
    plt.quiver(
        x,
        y,
        np.real(fz),
        -np.imag(fz),
        norm,  # Use norm as color for vectors
        cmap=cm.viridis,  # Choose a colormap for the color mapping
        norm=colors.LogNorm(),  # Normalize the color mapping
    )


def streamplot(
    f,
    x_space=defaults.x_space,
    y_space=defaults.y_space,
    vector_density=defaults.vector_density,
):
    """Plot the Polya vector field of complex function f as streamplot."""
    x, y = np.meshgrid(x_space, y_space)
    z = x + 1j * y
    fz = f(z)
    plt.axis("equal")
    plt.streamplot(x, y, np.real(fz), -np.imag(fz), vector_density)
