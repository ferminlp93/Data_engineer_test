# INSTRUCTIONS TO RUN THE SCRIPTS

## TECHNICAL TEST

### TASK 1
To execute the first task we will go to the directory ./Technical_Test/TASK1/scripts and we will open a python notebook (jupyter for example).

When we have the open notebook we will choose the file **data_export.ipynb** and execute the first cell that deals with doing everything necessary in the program.

This program generates 2 outputs **FinalData (id_new) .tsv** which fills the ids that are empty and **FinalData (id_old).tsv** that leaves the id as they came.

### TASK 2

To execute the second task we will go to the directory ./Technical_Test/TASK2_and_TASK3/ and open the terminal (linux or windows) to execute the program.
The python script to execute is **Orders.py**. If you put python Orders.py -h in the console and execute the output is:

usage: Orders.py [-h] [-o ORDERS] [-bs BATCH] [-i INTERVAL] [-d DIRECTORY]

optional arguments:
  -h, --help            show this help message and exit
  -o ORDERS, --orders ORDERS
                        Number of orders to generate which will each produce
                        two events.
  -bs BATCH, --batch BATCH
                        Batch size of events per file.
  -i INTERVAL, --interval INTERVAL
                        Interval in seconds between each file being created.
  -d DIRECTORY, --directory DIRECTORY
                        Output directory for all created files

For example you can call the script in this form:
python Orders.py  -o=5 -bs=2 -i=0 -d=./Orders/

 - 5 orders
 - Batch of 2
 - Interval of 0
 - Output directory ./Orders/

In addition to the functionality requested in the statement, one more has been added. When we execute an order the program will separate the placed orders and the result of them in separate files.


### TASK 3

To execute the third task, we will go to the directory ./Technical_Test/TASK2_and_TASK3/ and open the terminal (linux or windows) to execute the program.
The Python script to execute is **monitor.py**. 

This script monitors the folder ./Orders/ and counts the orders made so far. When the orders are processed they are moved to the historical folder ./Orders/Orders_history
