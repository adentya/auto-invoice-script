#!/bin/bash

crontab -l > crontabtemp

my_pwd="$(dirname "${BASH_SOURCE[0]}")"

crontab_script="${my_pwd}/crontab.py"

cron_job="$(python3 "${crontab_script}")"

exit_code=$?

if [[ $exit_code = 0 ]]; then
    echo "${cron_job} /bin/bash $(pwd)/cronscript.sh > $(pwd)/cronerror.log 2>&1 # Auto Invoice Script" >> crontabtemp
    echo "" >> crontabtemp
    crontab crontabtemp
fi