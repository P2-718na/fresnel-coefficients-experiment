#!/usr/bin/env bash
mkdir -p ./build/docs/report;
lualatex -output-directory=./build/docs/report ./docs/report/report.tex
