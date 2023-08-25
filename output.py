import numpy as np
import matplotlib.pyplot as plt
from Set_Generator import MandelbrotSet_Generator, JuliaSet_Generator

class Output:
    # attributes
    cursor = complex(0,0)
    trajectory = None

    # settings
    default_settings = {
        'Mandelbrot': True,
        'show_trajectory': True,
        'trajectory_iterations': 30,
        'image_iterations': 100,
        'show_grid': True,
        'julia_c': complex(0,0),
        'plot_limit': {'x': 1.5, 'y': 1.5},
        'resolution': {'x': 600, 'y': 600},
    }
    settings = None

    # generators
    mb_generator = MandelbrotSet_Generator()
    julia_generator = JuliaSet_Generator()

    # plot attributes
    cursor_plot = None
    trajectory_plot = None
    fig = None
    ax = None
    dragging = False


    def __init__(self, **kwargs): 
        # store settings
        self.settings = self.default_settings.copy()
        self.settings.update(kwargs)

        self.initPlot()
        self.generateBackground()
        # plt.savefig('img/fractal.png', format='png', dpi=300)
        plt.show()



    def initPlot(self):
        plt.rcParams['savefig.dpi'] = 300
        # Create the figure
        x_limit = self.settings['plot_limit']['x']
        y_limit = self.settings['plot_limit']['y']

        self.fig, self.ax = plt.subplots(figsize=(10,10))
        self.ax.set_xlim(-x_limit, x_limit)
        self.ax.set_ylim(-y_limit, y_limit)
        self.ax.set_xlabel("Real")
        self.ax.set_ylabel("Imaginary")

        if (self.settings['show_grid']):
            self.ax.grid(True)

        # create cursor and trajectory
        if (self.settings['show_trajectory']):
            self.cursor_plot, = self.ax.plot(self.cursor.real, self.cursor.imag, 'bo', markersize=5, picker=5)
            self.trajectory_plot, = self.ax.plot(self.cursor.real, self.cursor.imag, 'o--', markersize=2, picker=2)
            self.initDragging()



    # logic for point dragging
    def initDragging(self):
        def on_press(event):
            if event.inaxes != self.ax: return
            contains, _ = self.cursor_plot.contains(event)
            if contains:
                self.dragging = True

        def on_release(event):
            self.dragging = False

        def on_motion(event):
            if self.dragging:
                self.cursor = complex(event.xdata, event.ydata)
                self.update()

        self.fig.canvas.mpl_connect('button_press_event', on_press)
        self.fig.canvas.mpl_connect('button_release_event', on_release)
        self.fig.canvas.mpl_connect('motion_notify_event', on_motion)


    # calculates the image
    def generateBackground(self):
        x_limit = self.settings['plot_limit']['x']
        y_limit = self.settings['plot_limit']['y']
        width = self.settings['resolution']['x']
        height = self.settings['resolution']['y']
        image_iterations = self.settings['image_iterations']

        if self.settings['Mandelbrot']:
            image = self.mb_generator.MandelbrotMatrix(x_limit,y_limit,width,height,image_iterations)
        else: 
            c = self.settings['julia_c']
            image = self.julia_generator.juliaMatrix(c,x_limit,y_limit,width,height,image_iterations)

        self.ax.imshow(image, extent=(-x_limit, x_limit, -y_limit, y_limit), cmap='plasma')


    # updates plot of cursor and trajectory
    def update(self):
            self.cursor_plot.set_data([self.cursor.real], [self.cursor.imag])
            self.update_trajectory()
            self.fig.canvas.draw()

    
    # updates plot of trajectory
    def update_trajectory(self):

        if self.settings['Mandelbrot']:
            self.trajectory = self.mb_generator.MandelbrotPoints(self.cursor, self.settings['trajectory_iterations'])
        else: 
            c = self.settings['julia_c']
            self.trajectory = self.julia_generator.juliaPoints(self.cursor, c, self.settings['trajectory_iterations'])

        xs = [z.real for z in self.trajectory]
        ys = [z.imag for z in self.trajectory]
        self.trajectory_plot.set_data(xs, ys)


