@echo off
REM This file generated by Jython installer
REM Created on XXX by Sebastien

set ARGS=
:loop
if [%1] == [] goto end
        set ARGS=%ARGS% %1
        shift
        goto loop
:end

.\ThirdPart\jython-2.1\jython ".\ThirdPart\jython-2.1\Tools\jythonc\jythonc.py" %ARGS%
