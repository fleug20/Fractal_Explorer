import numpy as np


"""
generates data associated with the Mandelbrot set
"""
class MandelbrotSet_Generator:

    def __init__(self):
        pass

    # returns a matrix containing the iterations
    def MandelbrotMatrix(self, x_limit, y_limit, width, height, max_iterations):
        complexMatrix = np.zeros((height, width))
        r_values = np.linspace(-x_limit, x_limit, width)
        i_values = np.linspace(y_limit, -y_limit, height)
        R, I = np.meshgrid(r_values, i_values)
        complexMatrix = R + 1j*I

        vf = np.vectorize(self.MandelbrotIterations)
        image = vf(complexMatrix, max_iterations)

        return image


    # returns an array of points as complex numbers
    def MandelbrotPoints(self, c, iterations):
        array = np.zeros((iterations+1), dtype=np.complex128)
        array[0] = 0
        array[1] = c
        z = c
        for n in range(2, iterations+1):
            z = self.f(z, c)
            array[n] = z

        return array


    # returns the amount of iterations before diverging to infinity
    def MandelbrotIterations(self, c, max_iterations):
        z = 0
        for n in range(max_iterations):
            if abs(z) > 2:
                return n
            z = self.f(z, c)
        return max_iterations


    # the Mandelbrot function
    @staticmethod
    def f(z, c):
        return z**2 + c


"""
generates data associated with the julia set
"""
class JuliaSet_Generator:

    def __init__(self):
        pass


    # returns a matrix containing the iterations
    def juliaMatrix(self, c, x_limit, y_limit, width, height, max_iterations):
        complexMatrix = np.zeros((height, width))
        r_values = np.linspace(-x_limit, x_limit, width)
        i_values = np.linspace(y_limit, -y_limit, height)
        R, I = np.meshgrid(r_values, i_values)
        complexMatrix = R + 1j*I

        vf = np.vectorize(self.juliaIterations)
        image = vf(complexMatrix, c, max_iterations)

        return image


    # returns an array of points as complex numbers
    def juliaPoints(self, z0, c, iterations):
        array = np.zeros((iterations+1), dtype=np.complex128)
        array[0] = z0
        z = z0
        for n in range(1, iterations+1):
            z = self.f(z, c)
            array[n] = z

        return array


    # returns the amount of iterations before diverging to infinity
    def juliaIterations(self, z0, c, max_iterations):
        z = z0
        for n in range(max_iterations):
            if abs(z) > 2:
                return n
            z = self.f(z, c)
        return max_iterations


    @staticmethod
    def f(z, c):
        return z**2 + c