"""Fit a polynomial to a given set of data points using optimization."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def error_poly(C, data):
    """Compute error between given polynomial and observed data.

    Parameters
    ----------
    C: numpy.poly1d object or equivalent array representing polynomial coefficients
    data: 2D array where each row is a point (x, y)

    Returns error as a single real value.
    """

    # Metric: Sum of squared Y-axis differences
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
    return err


def fit_poly(data, error_func, degree=4):
    """Fit a polynomial to given data, using supplied error function.

    Parameters
    ----------
    data: 2D array where each row is a point (x, y)
    error_func: function that computes the error between a polynomial and observed data

    Returns polynomial that minimizes the error function.
    """

    # Generate initial guess for polynomial model (all coeffs = 1)
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))

    # Plot initial guess (optional)
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label="Initial guess")

    # Call optimizer to minimize error function
    result = spo.minimize(error_poly, Cguess, args=(data,), method='SLSQP', options={'disp': True})
    return np.poly1d(result.x)  # convert optimal result into a poly1d obeject and return


def test_run():
    # Define original polynomial
    Corig = np.poly1d([1.5, -10, -5, 60, 50])
    print("Original polynomial: {}*x^4 + {}*x^3 + {}*x^2 + {}*x + {}".format(Corig[4], Corig[3], Corig[2], Corig[1], Corig[0]))
    Xorig = np.linspace(-5, 5, 21)
    Yorig = np.polyval(Corig, Xorig)
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original polynomial")

    # Generate noisy data points
    noise_sigma = 30.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T  # Convert the input to an array, then transpose
    plt.plot(data[:, 0], data[:, 1], 'go', label="Data points")

    # Try to fit a polynomial to this data
    Cfit = fit_poly(data, error_poly)
    print("Fitted polynomial: {}*x^4 + {}*x^3 + {}*x^2 + {}*x + {}".format(Cfit[4], Cfit[3], Cfit[2], Cfit[1], Cfit[0]))
    plt.plot(data[:, 0], np.polyval(Cfit, data[:, 0]), 'r--', linewidth=2.0, label="Fitted polynomial")

    # Add a legend and show plot
    plt.legend()
    plt.show()


if __name__ == "__main__":
    test_run()
