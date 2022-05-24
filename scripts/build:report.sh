#!/usr/bin/env bash
mkdir -p ./docs/report/build;
pdflatex -output-directory=./docs/report/build ./docs/report/report.tex
