#!python3

import sys, os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    crontabtemp_path = '{}/{}'.format(dir_path, 'crontabtemp')

    try:
        f = open(crontabtemp_path)
        content = f.read()
    except Exception as err:
        print(err)
        sys.exit(2)
    else:
        f.close()

    content = content.split("\n")
    content = list(filter(lambda row: 'cronscript.sh > /' not in row and row != "", content))
    content = "\n".join(content).strip()

    try:
        f = open(crontabtemp_path, 'w')
        f.write(content)
        f.write("\n\n")
        f.close()
    except Exception as err:
        print(err)
        sys.exit(3)
    else:
        f.close()

    print(os.getenv('CRON_JOB'))
        