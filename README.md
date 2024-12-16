# bindoku

Simple binary sudoku written in python using ncurses

# Install

To install you should first clone the repo
```shell
$ git clone htts://github.com/neochar/bindoku.git && cd bindoku
```

## conda

Then, assuming you have conda installed, create environment:
```shell
$ conda create -n bindoku python=3.11
```

And then activate it by:
```shell
$ conda activate bindoku
```

## virtualenv

Alternatively, you can use `virtualenv`:
```shell
$ python3 -m virtualenv .venv
```

And then activate it by:
```shell
$ source .venv/bin/activate
```

## Install requirements

Once you have your environment ready to be used, run:
```shell
$ pip install -f requirements.txt
```

# Run

In order to play, you have to help me write a code :)
But you can see generated field by typing:
```shell
$ python3 bindoku.py
```

## Shortcuts

* `q` - exit
* `1` - 2x2 field
* `2` - 3x3 field
* `3` - 4x4 field
* `0` - reload process
* `h` - shift field left
* `j` - shift field down
* `k` - shift field up
* `l` - shift field right 
* `r` - rotate the field
* `i` - invert the field

While you manipulating the field, you also can see error messages,
which tell you what exactly goes wrong. It's a basic implmentation
of a game rules, which will be used in future development.

~~~
The goal of the game will be to fill all empty cells using game rules.
~~~
