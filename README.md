# File Sorter

## Objective

The objective for this project was to sort the given files into sub-directories depending on the year,month,day and the type of file.

## How To Use This Tool

#### Step 1:
>Before you use this tool, ensure that all the files are in the same directory.
Run the python file in the parent directory of all the files.
Ensure you have pip working on this machine, to verify you can just type in pip
If that resulted in an error then we can install pip using the following command

```sudo apt-get install python3-pip```
```sudo apt-get install git```

*if you are presented with a prompt enter 'y' for yes*

### Step 2:
>Now we can run the file, to run the file we can enter the following command

```python3 Automation_File_Sorter.py Sample/```

***for demo I have included a sample folder which includes all the files***

To try the sample file we can write the following command on terminal

```python3 Automation_File_Sorter.py Sample/```

### Installation Summary

```
git clone https://github.com/mayfled/File_sorter.git
cd File_sorter
pip install -r requirements.txt
python3 Automation_File_Sorter.py Sample/
cd Sample

--------------
Folder construction
    - YY
        - MM
            - DD
                - TS
                - RS
                - FS
```
