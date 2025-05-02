------------------------------------------------------------------------------------------
INITIAL SETUP
------------------------------------------------------------------------------------------

Create a django project
> django-admin createproject web_project
> cd web_project

Initialize the git repository
> git init

Create a .gitignore
Add .pyc, __pycache__, db.sqlite3, ...
Whatever you donot want to git to track

Do first commit
> git add .
> git status 
> git commit -m 'Initial Commit on Main Branch'
> git status

Rename the master to main, if required:
> git branch -m master main

Check the commits:
> git log --oneline

Output ->
0707f5f (HEAD -> main) Initial Commit on Master (Main) Branch

------------------------------------------------------------------------------------------
DEVELOPMENT WORKFLOW
------------------------------------------------------------------------------------------

Create a development branch
> git checkout -b development    -> Creates a branch called development

Make a simple change in the development branch
> python manage.py startapp blog
> git add .
> git commit -m "Added blog app"

Notice, currently we are in the development branch
Create a testing branch from development 
> git checkout -b testing

Simlate one bug fix in testing
Do some changes in some file, say views.py
> git add blog/views.py
> git commit -m 'Added content to views.py'


See all the branches
> git branch

------------------------------------------------------------------------------------------
MERGE THE WORK
------------------------------------------------------------------------------------------

Merge testing into development
> git checkout development    -> come back to development
> git merge testing

Merge development into main
> git checkout main
> git merge development

Delete the merged branches
> git branch -d testing
> git branch -d development

------------------------------------------------------------------------------------------
USEFUL COMMANDS SUMMARY
------------------------------------------------------------------------------------------


git status → Check current status

git log → Show commit history

git diff → Show differences before commit

git branch → Show branches

git checkout → Switch branches

git merge → Merge branches

git add <file> / git add . → Stage files

git commit -m "msg" → Commit changes
