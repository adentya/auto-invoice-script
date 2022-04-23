#!/bin/bash

my_pwd="$(dirname "${BASH_SOURCE[0]}")"
venv_file_exist=false
venv_activate="${my_pwd}/venv/bin/activate"

if [[ -f "${venv_activate}" ]]; then
    venv_file_exist=true
fi

if [[ $venv_file_exist = true ]]; then
    source $venv_activate
fi

my_script="${my_pwd}/script.py"
python3 $my_script

if [[ $venv_file_exist = true ]]; then
    deactivate
fi