echo $'Run Python:\n'
time python slow-factors.py

echo $'\nCompile C:'
time gcc -O3 slow-factors.c -o slow-factors

echo $'\nRun C:\n'
time ./slow-factors
