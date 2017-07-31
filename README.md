# Image Resizer

This script will resize your image.

Anton Demkin, 2017

# Installation
The script requires Python 3. To install additional modules run this terminal command from folder where you put this script:
```
pip3 install -r requirements.txt
```

# Usage

To run this script, use terminal:
```
$ python3 image_resize.py [arguments]
```

####Available arguments:

-h --help: get help

#####Required arguments:

[path] - full path or filename of image you want to resize

#####Optional arguments:

-s --scale: scale ratio. Can not be used with -x or -y arguments

-x --x_size: width of resized image

-y --y_size: height of resized image

-o --output: resized image will be placed at desired location 

# Example

```
$ image_resize.py img.jpg -s 2
File succesfully resized: /Users/antondemkin/PycharmProjects/devman/12_image_resize/img__1778x1008.jpg

$ image_resize.py img.jpg -x 100 -y 300 -o ~/Desktop
Warning, aspect ratio changed!
File succesfully resized: /Users/antondemkin/Desktop/img__100x300.jpg
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
