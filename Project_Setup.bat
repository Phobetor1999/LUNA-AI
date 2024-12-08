@echo off
REM Copyright 2022 S2DesignsTeam (??anonimo??).
REM
REM Licensed under the Apache License, Version 2.0 (the "License");
REM you may not use this file except in compliance with the License.
REM You may obtain a copy of the License at
REM
REM      http://www.apache.org/licenses/LICENSE-2.0
REM
REM Unless required by applicable law or agreed to in writing, software
REM distributed under the License is distributed on an "AS IS" BASIS,
REM WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
REM See the License for the specific language governing permissions and
REM limitations under the License.
REM 
REM +-------------------------------------------------------------------------------------------+
REM � Table draw chars                                                                          �
REM �-------------------------------------------------------------------------------------------�
REM � Double lines         � Single line          � Double lined columns �   Double lined rows  �
REM �----------------------+----------------------+----------------------+----------------------�   
REM � Example  � ANSI CHAR � Example  � ANSI CHAR � Example  � ANSI CHAR � Example  � ANSI CHAR �
REM �----------+-----------+----------+-----------+----------+-----------+----------+-----------�
REM � +---+    � ���ͻ     � +---+    � ���Ŀ     � +---+    � ���ķ     � +---+    � ���͸     �
REM � � � �    � � � �     � � � �    � � � �     � � � �    � � � �     � � � �    � � � �     �
REM � �-+-�    � ���͹     � +-+-�    � ���Ĵ     � �-+-�    � ���Ķ     � �-+-�    � ���͵     �
REM � � � �    � � � �     � � � �    � � � �     � � � �    � � � �     � � � �    � � � �     �
REM � +---+    � ���ͼ     � +---+    � �����     � +---+    � ���Ľ     � +---+    � ���;     �
REM +-------------------------------------------------------------------------------------------+
REM 
REM +---------------------------------------------------------------------------------------------------------------+
REM � TEXT COLORS                                                                                                   �
REM �---------------------------------------------------------------------------------------------------------------�
REM � FORE COLORS                                           � BACKGROUND COLORS                                     �
REM �-------------------------------------------------------+-------------------------------------------------------�   
REM �           DARKER          �           LIGHTER         �           DARKER          �           LIGHTER         �
REM �---------------------------+---------------------------+---------------------------+---------------------------�
REM � COLOR NAME  �  ANSI CODE  � COLOR NAME  �  ANSI CODE  � COLOR NAME  �  ANSI CODE  � COLOR NAME  �  ANSI CODE  �
REM �-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------�
REM � BLACK       � [30m       � BLACK       � [90m       �             �             �             �             �
REM � RED         � [31m       � RED         � [91m       �             �             �             �             �
REM � GREEN       � [32m       � GREEN       � [92m       �             �             �             �             �
REM � YELLOW      � [33m       � YELLOW      � [93m       �             �             �             �             �
REM � BLUE        � [34m       � BLUE        � [94m       �             �             �             �             �
REM � MAGENTA     � [35m       � MAGENTA     � [95m       �             �             �             �             �
REM � CYAN        � [36m       � CYAN        � [96m       �             �             �             �             �
REM � WHITE       � [37m       � WHITE       � [97m       �             �             �             �             �
REM +---------------------------------------------------------------------------------------------------------------+

echo �����������������������������������������������������������������������������ͻ
echo � LUNA-AI Project setup procedure                                             �
echo �����������������������������������������������������������������������������ͼ
echo La directory corrente e': %CD%
:: Imposta la directory del progetto
set PROJECT_DIR=%CD%
pause

CLS
echo �����������������������������������������������������������������������������ͻ
echo � Installazione o Aggiornamento di pip...                                     �
echo �����������������������������������������������������������������������������ͼ
python -m pip install --upgrade pip
call :CHECK_FAIL
pause

CLS
echo �����������������������������������������������������������������������������ͻ
echo � Installazione virtualenv...                                                 �
echo �����������������������������������������������������������������������������ͼ
echo Installazione virtualenv
python -m pip install virtualenv
call :CHECK_FAIL
pause

CLS
echo �����������������������������������������������������������������������������ͻ
echo � Creazione dell'environment virtuale per Luna-AI...                          �
echo �����������������������������������������������������������������������������ͼ
python -m venv venv
call :CHECK_FAIL
pause

CLS
echo �����������������������������������������������������������������������������ͻ
echo � Verifico se Git e' inizializzato...                                         �
echo �����������������������������������������������������������������������������ͼ
:: Verifica se Git   inizializzato
if not exist ".git" (
    echo Inizializzo il repository Git...
    git init
	call :CHECK_FAIL
)

echo �����������������������������������������������������������������������������ͻ
echo � Configuro il repository remoto...                                           �
echo �����������������������������������������������������������������������������ͼ
:: Configura il repository remoto
git remote remove origin 2>nul
call :CHECK_FAIL

git remote add origin https://github.com/Phobetor1999/LUNA-AI.git
call :CHECK_FAIL

echo �����������������������������������������������������������������������������ͻ
echo � Verifico la configurazione del repository remoto...                         �
echo �����������������������������������������������������������������������������ͼ
:: Verifica la configurazione del repository
git remote -v
call :CHECK_FAIL

:: Crea la directory .vscode se non esiste
echo �����������������������������������������������������������������������������ͻ
echo � Creazione del File settings.json di vscode per il progetto Luna-AI...       �
echo �����������������������������������������������������������������������������ͼ
if not exist ".vscode" (
    mkdir .vscode
	call :CHECK_FAIL
)
:: Scrive il file settings.json utilizzato da Visual Studio Code
echo {
echo     "git.remote": "origin",
echo     "git.url": "https://github.com/Phobetor1999/LUNA-AI.git",
echo     "python.pythonPath": "venv\\Scripts\\python.exe",
echo     "python.envFile": "${workspaceFolder}\\.env",
echo     "python.formatting.provider": "black",
echo     "python.terminal.activateEnvInCurrentTerminal": true,
echo     "editor.formatOnSave": true,
echo     "files.exclude": {
echo        "**/__pycache__": true,
echo        "**/*.pyc": true
echo     },
echo     "python.createEnvironment.contentButton": "show",
echo     "python.linting.enabled": true,
echo     "python.linting.pylintEnabled": true,
echo     "python.linting.pylintArgs": [
echo         "--disable=C0111" 
echo     ]
echo }
) > .vscode\settings.json
echo File settings.json creato con successo nella cartella .vscode!
call :CHECK_FAIL
pause

CLS
echo �����������������������������������������������������������������������������ͻ
echo � Installazione dei pacchetti richiesti dal progetto Luna-AI e avvio di       �
echo � Visual Studio Code.                                                         �
echo �����������������������������������������������������������������������������ͼ
call ".\venv\scripts\activate.bat"
call :CHECK_FAIL
pause

python -m pip install --upgrade pip
call :CHECK_FAIL
pause

pip install -r requirements.txt
call :CHECK_FAIL
pause

start "" && code %PROJECT_DIR% :0

REM start "" && .\venv\Scripts\activate.bat && python -m pip install --upgrade pip &&  pip install -r requirements.txt && code %PROJECT_DIR% | .\venv\Scripts\activate.bat :0
goto :eof

:: /// check if the app has failed
:CHECK_FAIL
if NOT ["%errorlevel%"]==["0"] (
    pause
    exit /b %errorlevel%
)
goto :eof 