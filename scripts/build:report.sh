#!/usr/bin/env bash
mkdir -p ./build/docs/report;
pdflatex -output-directory=./build/docs/report ./docs/report/report.tex
