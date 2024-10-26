# This is a README for the Hadoop repo.

### In this repo we will practicing Hadoop for hosting information across multiple systems
<br>

### Author - Ethan Zalta
<br>


# Tasks
### There are 8 tasks in this project

## Task 0
* Write a bash script createdirectories.sh that creates the directory /holbies and /holbies/input within HDFS.

## Task 1
* Write a bash script lao.shthat upload the file lao.txt to the /holbies/input directory on the HDFS.

## Task 2
* Write a bash script text.sh that displays the content of the file lao.txt on the HDFS.

## Task 3
* For this part we need to install the snakebite library.

* pip install snakebite-py3

* Write a function def createdir(l): that creates the directories listed on l within HDFS

## Task 4
* Write a function def deletedir(l): that removes the directories listed on l within HDFS

## Task 5
* Write a function def download(l): that retrieves from the HDFS files listed in l and store them in the home /tmp folder of the user

## Task 6
* The aim of this task and the next one is to run a Mapreduce application on a Hadoop environment with Python. You have to write two Python programs: mapper.py and reducer.py

* Write the script mapper.py that takes the rows of the salaries.csv and print the id, the company and the totalyearlycompensation items. Id and company will be separated by a tabulation while company and totalyearlycompensation will be separated by a comma.

## Task 7
* Write the script reducer.py that takes the output of the mapper.py script and gives the top ten salaries sorted by totalyearlycompensation. The output should be as below. The mapper and reducer should be run on the Hadoop environment with the mapred command.

You have to:

1- Use the put command to upload the salaries.csv file on the HDFS system on /holbies/input.

2- The output should be stored in the /holbies/output/ folder on the HDFS system.

3- You’re only allowed to use an array of 10 element on your reducer


