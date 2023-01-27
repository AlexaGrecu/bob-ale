# bob-ale

## un proiect cu bob

* git

git clone https://github.com/AlexaGrecu/bob-ale.git -b add-python
git init
git add -u
git commit -m "changes to readme file"

* git workflow

Git Workflow

1 Create a repo - git init
2 Make changes
3 Add the changes - git add

Staging:
git add -A - stages all changes
git add . - stages new and modified files only
git add -u - stages modified and deleted files only
git add <file> - stages a specific file

4 Commit changes - git commit

Committing
git commit -m "Updating readme" (m = message)
git reset --soft HEAD~1 (1=1 commit back) (undo the commit - can be done before being pushed to the remote)

5 Push commits to the remote repo - git push

git push <remote> <branch>
eg: git push origin main

6 Pull updates from remote repo -git pull

git pull <remote> <branch>
eg: git pull origin main

7 Repeat steps 2-6

* git useful commands

Initial configurations
git config --global user.name "Your Username"
git config --global user.email "Your Email address"


pwd - print working directory
cd - change directory
cd .. - go to the parent directory
mkdir - make directory 
ls -a - command to see hidden files
git status = shows status 
git init - created local repository
git diff - see the differences
git stash - making a change but not comming it yet.
git stash pop - rebrings the change
git stash save "name of the modification"
git stash list - shows all the modif that are saved in stash
git stash apply 0 -removes modifications
git commit -am - adds in staging and commits at the same time
git reset <specific file> - unstages the change
git add -p - to see all changes. then time y (yes), n(no)
git checkout -b +name of the branch - creating a new branch
git push origin 02_01 --set-upstream - first time pushing this branch
git log - checks the latest commits (to get out select "Q")
git checkout - - to go back on the last branch

Git Hooks:
Python - pre-commit
Node: husky

Pre-commit 
.pre-commit-config.yaml
pip install pre-commit

Git log:

git log --oneline
git log --graph --oneline
git commit --amend -m "mesaj"
git revert name of the commit 


on Github if you are on a repo and hit "." you open the code editor in the browser!!