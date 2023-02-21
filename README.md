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
- git add -A - stages all changes
- git add . - stages new and modified files only
- git add -u - stages modified and deleted files only
- git add <file> - stages a specific file

4 Commit changes - git commit

Committing
- git commit -m "Updating readme" (m = message)

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
git stash - making a change but not commiting it yet.
git stash pop - rebrings the change
git stash save "name of the modification"
git stash list - shows all the modif that are saved in stash
git stash apply 0 -removes modifications
git commit -am - adds in staging and commits at the same time
git reset <specific file> - unstages the change
git add -p - to see all changes. then type y (yes), n(no)
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

- Git cherry-pick - apply the changes introduced by some existing commits
git cherry-pick [--edit] [-n] [-m <parent-number>] [-s] [-x] [--ff]
                       [-S[<keyid>]] <commit>...
   or: git cherry-pick (--continue | --skip | --abort | --quit)

    --quit                end revert or cherry-pick sequence
    --continue            resume revert or cherry-pick sequence
    --abort               cancel revert or cherry-pick sequence
    --skip                skip current commit and continue
    --cleanup <mode>      how to strip spaces and #comments from message
    -n, --no-commit       don't automatically commit
    -e, --edit            edit the commit message
    -s, --signoff         add a Signed-off-by trailer
    -m, --mainline <parent-number>
                          select mainline parent
    --rerere-autoupdate   update the index with reused conflict resolution if possible
    --strategy <strategy>
                          merge strategy
    -X, --strategy-option <option>
                          option for merge strategy
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit
    -x                    append commit name
    --ff                  allow fast-forward
    --allow-empty         preserve initially empty commits
    --allow-empty-message
                          allow commits with empty messages
    --keep-redundant-commits
                          keep redundant, empty commits


- These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

Git Reset

- git reset --soft HEAD~1 (1=1 commit back) (undo the commit - can be done before being pushed to the remote)
- git reset --hard HEAD~5 resets the current branch to the commit just before the last 5 (see man 
gitrevisions for details about this notation and other cool alternatives like HEAD@{2 days ago}). 
As it is a hard reset, it will also overwrite every change in the working tree as well. See man git-reset.
- git merge --squash HEAD@{1} HEAD@{1} is where the branch was just before the previous command 
(again, see man gitrevisions). This command sets the state of the index to be as it would just after a 
merge from that commit. This whole operation could be a way to take 5 commits from a branch in which you 
started a new feature and squash them to a single commit, a meaningful one.
