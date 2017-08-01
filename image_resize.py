from PIL import Image
import argparse
import os
import math

def check_if_aspect_changed(x1, y1, x2, y2):
    return not math.isclose((x1 / y1), (x2 / y2), rel_tol=0.002)


def get_new_size(original_size, width=None, height=None, scale=None):
    if scale is not None:
        new_x, new_y = original_size[0] * scale, original_size[1] * scale
    
    elif (width and height) is not None:
        new_x, new_y = width, height
        if check_if_aspect_changed(original_size[0], original_size[1], new_x, new_y):
            print("Warning, aspect ratio changed!")
    
    elif width is not None:
        new_scale = original_size[0] / width
        new_height = original_size[1] // new_scale
        new_x, new_y = width, new_height
    
    elif height is not None:
        new_scale = original_size[1] / height
        new_width = original_size[0] // new_scale
        new_x, new_y = new_width, height
    else:
        new_x, new_y = (original_size)
    
    return (int(new_x), int(new_y))


def resize_image(input_path, output_path, width, heigh, scale):
    try:
        image = Image.open(input_path, 'r')
    except IOError as error:
        print(error)
    else:
        new_size = get_new_size(image.size, width, heigh, scale)
        resized_image = image.resize(new_size)
        pathname, extension = os.path.splitext(output_path)
        new_path = pathname + "__{}x{}".format(new_size[0], new_size[1]) + extension
        try:
            resized_image.save(new_path)
        except PermissionError as error:
            print(error.strerror)
        except IOError as error:
            print("Cannot convert: {}".format(error))
        else:
            print("File succesfully resized: {}".format(new_path))


def arguments_parser():
    parser = argparse.ArgumentParser(description='This is a simple utility to scale images.',
                                     epilog='Scale cannot be used with width or height.')
    
    parser.add_argument('input', help='path to image file', metavar='[/path/to/your/file]')
    
    group0 = parser.add_argument_group('output path')
    group1 = parser.add_argument_group('width and height')
    group2 = parser.add_argument_group('scale')
    
    group0.add_argument('-o', '--output', help='folder, where result image will be placed')
    group1.add_argument('-x', '--x_size', metavar='640', help='determines height of new image', type=int)
    group1.add_argument('-y', '--y_size', metavar='480', help='determines width of new image', type=int)
    group2.add_argument('-s', '--scale', metavar='1.6', help='determines a new image scale', type=float)
    
    return parser.parse_args()


def main():
    args = arguments_parser()
    
    if args.scale is not None and (args.x_size or args.y_size) is not None:
        print('Scale cannot be used with width or height arguments.\nUse only [-s] or [-x, -y]')
    if args.output is None:
        args.output = os.path.dirname(os.path.abspath(args.input))
    
    input_path = os.path.abspath(args.input)
    filename = os.path.basename(input_path)
    output_path = os.path.join(os.path.expanduser(args.output), filename)
    
    resize_image(input_path=input_path,
                 output_path=output_path,
                 width=args.x_size,
                 heigh=args.y_size,
                 scale=args.scale)


if __name__ == '__main__':
    main()
