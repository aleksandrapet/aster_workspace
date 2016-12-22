#!/bin/bash
cd ~/AsterW_GUI
pyuic4 mainwindow.ui > mainwindow_auto.py
python main.py &>>  aster.log
python3 main.py &>>  aster.log
