#!/bin/bash
export PYTHONPATH="./src/main/python;${PYTHONPATH}"
python -m unittest discover -v -s src/test/python/codequest -p "test_*.py"
