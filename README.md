Usage:

    virtualenv .
    source bin/activate
    python helpdesk.py input.txt > result.csv

Where input.txt contains a list of names one per line:

    classpass
    udemy
    someotherhelpdesk 


The script will check for domains such as udemy.zendesk.com, udemy.desk.com.. etc...
