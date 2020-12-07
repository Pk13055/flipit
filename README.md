# Flipbook Generator - FlipIt

## Introduction

FlipIt has a very simple semantic language. However, it is extensive enough to
combine images into very intricate storylines, provided you have a diverse set
of images and some creativity.

![demo-video](data/sample/demo.gif)

## Language

Very primitive but effective language:
```
[frame_id] [x] [y] [image_path]
```

- `frame_id`: Which frame do you want the object to be rendered in
- `x`: X coordinate (top left of the image)
- `y`: Y coordinate (top left of the image)
- `image_path`: relative to the notebook

There are a few assumptions made at this point:
- The language written follows exactly the specification (if any line has an error, the book will not generate the frame corresponding to the line)
- One `frame rate` and `height` and `width` for all the inputs supplied.

## Running

```bash
usage: fc.py [-h] [-f FRAMERATE] [--height HEIGHT] [--width WIDTH] [-i INPUTS]
             [-o OUTPUTS]

FlipIt - Flipbook compiler to compile the book Each row is
            represented as: [frame_id]  [x] [y] path/to/img/relative/to/input
        :Example:
            ./fc.py -i data/sample/newton.flip -o data/sample/newton.avi # (additionally any N more i, o pairs)

optional arguments:
  -h, --help            show this help message and exit
  -f FRAMERATE, --framerate FRAMERATE
                        frame rate of the output video
  --height HEIGHT       height of the output clip
  --width WIDTH         width of the output clip
  -i INPUTS, --input INPUTS
                        Input .flip file(s)
  -o OUTPUTS, --output OUTPUTS
                        output .avi file(s)
```


### Containerized

```bash
docker build -t pk13055/flipit .
docker run -v $PWD/data/sample/:/usr/src/app/data/sample/ pk13055/flipit -i ./data/sample/newton.flip -o ./data/sample/newton.avi
```

### Normal

```bash
pip3 install -r requirements.txt
# example query
./fc.py -i data/sample/newton.flip --o data/sample/newton.avi
```

## Development

```bash
pip3 install pip-tools
mkvirtualenv hasura-pk13055 --python python3
workon hasura-pk13055
pip-compile requirements.in > requirements.txt
deactivate
rmvirtualenv hasura-pk13055

```
