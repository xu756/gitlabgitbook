#!/bin/bash
for i in `ps -ef | grep gitbook | grep serve`; do kill -9 $i ; done;
gitbook serve
