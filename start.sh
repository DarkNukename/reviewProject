#!/bin/bash

gnome-terminal -- bash -c "source ./venv/bin/activate; cd ./A; echo SERVICE - A; python3 manage.py runserver 8000; exec bash"
gnome-terminal -- bash -c "source ./venv/bin/activate; cd ./application; echo APPLICATION; python3 manage.py runserver 8001; exec bash"
gnome-terminal -- bash -c "source ./venv/bin/activate; cd ./application; celery -A application worker -B -l INFO; exec bash"