import argparse
from Output import Output


def main():
    parser = argparse.ArgumentParser(description="Julia/Mandelbrot Set Generator")

    # Boolean flags for Mandelbrot and Julia sets
    parser.add_argument('--julia', action='store_true', help='Generate Julia Set')
    
    # Other settings
    parser.add_argument('--show_trajectory', action='store_true', help='Show trajectory')
    parser.add_argument('--trajectory_iterations', type=int, default=30, help='Number of trajectory iterations')
    parser.add_argument('--image_iterations', type=int, default=100, help='Number of iterations for generating the fractal image')
    parser.add_argument('--grid', action='store_true', help='Show grid on plot')
    parser.add_argument('--julia_c', type=complex, default=0+0j, help='Complex number c for Julia Set')
    parser.add_argument('--plot_limit', type=parse_float_tuple, default=(1.5,1.5), help='Plot limit for x and y axis')
    parser.add_argument('--resolution', type=parse_int_tuple, default=(600,600), help='Resolution for x and y axis')

    args = parser.parse_args()

    settings = {
        'Mandelbrot': not args.julia,
        'show_trajectory': args.show_trajectory,
        'trajectory_iterations': args.trajectory_iterations,
        'image_iterations': args.image_iterations,
        'show_grid': args.grid,
        'julia_c': args.julia_c,
        'plot_limit': {'x': args.plot_limit[0], 'y': args.plot_limit[1]},
        'resolution': {'x': args.resolution[0], 'y': args.resolution[1]},
    }

    print("generating... please wait")
    Output(**settings)

def parse_float_tuple(value):
    try:
        x, y = map(float, value.split(','))
        return x, y
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid tuple format for float values. Expected 'x,y'.")

def parse_int_tuple(value):
    try:
        x, y = map(int, value.split(','))
        return x, y
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid tuple format for integer values. Expected 'x,y'.")



if __name__ == "__main__":
    main()



