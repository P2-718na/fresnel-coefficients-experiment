#!/usr/bin/env bash
mkdir -p ./build/docs/report &&
export $(cat ./docs/report/.env | xargs) &&
lualatex -output-directory=./build/docs/report ./docs/report/report.tex &&
bibtex ./build/docs/report/report.aux &&
lualatex -output-directory=./build/docs/report ./docs/report/report.tex; # Yep. Needed for bibtex.
