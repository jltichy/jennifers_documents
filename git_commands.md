Resources:

https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html

https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf


Commands that I tried:

git init
creates a new git repository

git init --bare
creates a new git repository that is the main storage container for the program

git clone
copies an existing repository onto the local machine

git status
tells you if you have new changes that need to be committed
use this often to see if files have been added or deleted or if changes have been made

git add
adds files; example:
git add octocat.txt
to add a file called octocat

git add
can also be used with wildcards; example:
git add '*.txt'
to add all files that end in .txt

git remote add
creates a remote repository at GitHub where we can send our local repository; example:
git remote add origin https://github.com/try-git/try_git.git
in this example, the name of the remote repository is origin

git commit
submits the changes to the repository; example:
git commit -m "Add cute octocat story"
to commit the changes and to make a comment (that's what the -m does)
example:
git commit -m "Remove all the cats"

git log
if you type this, a journal log is displayed to see what all has been done 
it's more comprehensive than git status (git status only tells you of the most recent changes since the last commit)

git push
this sends the local repository to GitHub; example:
git push -u origin master
the -u tells git to remember the parameters, origin is the name of the remote repository, and master is the default branch where we're sending this
another example:
git push
will push the work back to the remote repository on GitHub

git pull
use this command after some time to see changes that you or other users have made; example:
git pull origin master
origin is the name of the remote repository on GitHub and master is the default branch from GitHub

git diff HEAD
if there are differences after running a git pull, you can see what's changed by using this command
HEAD asks to see the most recent changes since the last commit

git diff --staged
this command asks for the differences since the last commit, and only asks for the files that are being staged (those that are going to be committed but haven't yet)

git reset
will remove files from the staging area if necessary; example:
git reset octofamily/octodog.txt
this command will take octodog.txt out of being staged for octofamily (the file is still there; it just won't be committed)

git checkout
resets the repository back to the last commit; example:
git checkout -- octocat.txt
example:
git checkout clean_up
switches back to the clean_up branch
example:
git checkout master
switches back to the master branch

git branch clean_up
code to merge the branches back into the master branch; example:
git branch clean_up

git branch
tells you the names of the current branches
can be used as is, or like this:
git branch -d clean_up
this will delete the branch called clean_up (since that branch is now merged with the master branch)

git rm
will remove files (including those in staging); example:
git rm '*.txt'

git merge
will merge the files back into master; example:
git merge clean_up
will merge the clean_up branch with the master branch
