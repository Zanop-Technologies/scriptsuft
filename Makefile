SHELL := /bin/sh
.PHONY: all build clean
all: build

build:
	sh ./build.sh

clean:
	rm -rf dist
