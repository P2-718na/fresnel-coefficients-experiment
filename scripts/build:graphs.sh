#!/usr/bin/env bash
mkdir -p ./build/graphs;
for script in ./code/graphs/*py
do
  python "$script";
  echo "Building: $script...";
done

