## Overview

This repo is a fork of the official [Stockfish](https://stockfishchess.org) [repo](https://github.com/official-stockfish/Stockfish) - created to implement a Python wrapper around the C++ code Stockfish's UCI chess engine.

The details of the effort can be found in [this](https://nsriniva.github.io/2022-07-23-Stockfish-C++-Python-cppyy/) post on my [portfolio site](https://nsriniva.github.io/)

## Files

The following files were modified
```
.../src/Makefile b/src/Makefile
.../src/movegen.h b/src/movegen.h
.../src/uci.cpp b/src/uci.cpp
.../src/uci.h b/src/uci.h
```

The following files were added
```
.../src/move_generator.py b/src/move_generator.py
.../src/stockfish.h b/src/stockfish.h
.../src/stockfish.py b/src/stockfish.py
```
