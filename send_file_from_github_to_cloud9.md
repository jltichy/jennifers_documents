Open GitHub and make a new repository that contains a file.
Click on the name of the file and copy the url (as https).
Go to Cloud9.  In a new terminal, type the following:

jltichy:~/workspace (master) $ pwd
/home/ubuntu/workspace

#pwd is print working directory - it tells you where you are located

jltichy:~/workspace (master) $ git clone https://github.com/jltichy/practice_push_to_cloud9.git
Cloning into 'practice_push_to_cloud9'...
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 9 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (9/9), done.
Checking connectivity... done.

#git clone "plus the url copied from GitHub" clones the repository to Cloud9

jltichy:~/workspace (master) $ ls
bday.py  birthday.py  hello.py  practice_push_to_cloud9/

#ls is the list of information about the file; in this case, it lists all of the files in the current directory

jltichy:~/workspace (master) $ cd practice_push_to_cloud9/

#cd "plus the name of the new repository" changes the file directory to the new repository

jltichy:~/workspace/practice_push_to_cloud9 (master) $ ls
practice_send_to_cloud.py

#ls checks to see what files are in this directory 

----

You can then click on the new file (.py file) and it opens on the menu list in Cloud9 (left side of screen).  It can then be opened and changes can be made.

