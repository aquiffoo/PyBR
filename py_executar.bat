@echo off
setlocal
set PYBR_COMPILADOR="C:\Compilador_PyBR\PyBR\compilador.py"
python %PYBR_COMPILADOR% %1.pybr
endlocal
