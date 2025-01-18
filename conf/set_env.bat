@echo off

REM 获取当前脚本所在目录
set SCRIPT_DIR=%~dp0

REM 移除末尾的反斜杠
set SCRIPT_DIR=%SCRIPT_DIR:~0,-1%

REM 获取项目的根木偶
set PROJECT_HOME_DIR=%SCRIPT_DIR%\..

set OLD_CD=%CD%

pushd %PROJECT_HOME_DIR%
set PYTHONPATH=%PYTHONPATH%;%CD%

pushd %OLD_CD%

echo PYTHONPATH is set to: %PYTHONPATH%
pause