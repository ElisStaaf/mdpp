#!/bin/sh

FS="/usr/local/bin"

cp src/* $FS && \
mv "$FS/mdpp.py" "$FS/mdpp"
