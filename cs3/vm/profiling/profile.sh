echo $'Run Python:\n'
time python slow-factors.py

echo $'\nCompile C:'
# Turn off optimizations so that gcc doesn't compute answer at compile time
time gcc -O0 slow-factors.c -o slow-factors

echo $'\nRun C:\n'
time ./slow-factors
