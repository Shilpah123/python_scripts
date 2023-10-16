# python_scripts

#parse_multiple_htmls.py -> Can parse through multiple HTML files placed in a directory and gives us the count of 2022 and 2023 occurrences.

#Before you begin:
#You need to install BeautifulSoup library to run these scripts.
#Go to Python directory that has the python.exe file. Open command prompt and execute the following command:
#pip install BeautifulSoup

#You can use Ananconda Spyder to run these scripts.

#upload_to_server_and_unzip.py -> Connects to remote server, uploads zip, unzips, adds read write execute permissions to unzipped files and folder. 
Following libraries are needed:
pip install paramiko
pip install time
pip install random

#script1_post_migration_cleanup.py -> This script was created to cleanup files for migration from UniDoc DTD to Oxygen DITA DTD. 
This script performs the following tasks:
Replaces <emphasis> with <i>; </emphasis> with </i>; <command> with <codeph>; nsnconcept with concept, nsntask with task, nsnmap with map
Removes keys from concept,task,topic
Removes rotate attribute from <entry> tag in tables
Removes attributes that are not supported in ditamap.

#script2_script2_final_script_improved_exe_time_globalpath.py -> This script was created to prepare files to move to Oxygen DITA DTD. 
This script changes the figure, concept, table id to lowercase in .xml files.
Changes topic references in .ditamap files to lowercase and changes file reference extension from .xml to .dita.
Changes the extension of file reference in topics from xml to dita. 
Changes the file extension from .xml to .dita and changes filename to lowercase. 

