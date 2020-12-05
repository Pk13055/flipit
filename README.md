# Flipbook Generator - FlipIt

## Introduction

FlipIt has a very simple semantic language. However, it is extensive enough to
combine images into very intricate storylines, provided you have a diverse set
of images and some creativity.

## Language


## Running



### Containerized

```bash
docker build -t pk13055/flipit .
```

### Normal

```bash
pip3 install -r requirements.txt
```

## Development

```bash
pip3 install pip-tools
pip-compile requirements.in > requirements.txt
```
