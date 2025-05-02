https://github.com/mindful-ai/ust-gitdemo.git

Create a new repository on the command line
------------------------------------------------------------------------------------------
echo "# ust-gitdemo" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mindful-ai/ust-gitdemo.git  -> link current local git repo with github repo
git push -u origin main -> upload current local main to git main

Push an existing repository from the command line
------------------------------------------------------------------------------------------

git remote add origin https://github.com/mindful-ai/ust-gitdemo.git
git branch -M main
git push -u origin main


------------------------------------------------------------------------------------------
WORKFLOW INVOLVING GITHUB
------------------------------------------------------------------------------------------

Step 1:
------------------------------------------------------------------------------------------

Clone the repository
> git clone https://github.com/mindful-ai/ust-gitdemo.git

Create a django project in this folder

Issue the commands to push into github
> git add .
> git commit -m 'Initial Commit'
> git push origin main     -> main should be the name of the main branch locally, uploads main to github repo

You should see the webproject loaded in github



Step 2:
------------------------------------------------------------------------------------------

> git checkout -b deva   -> create a branch locally
> git push origin deva   -> push that to github
  
> git checkout main

> git checkout -b devb   -> create a branch locally
> git push origin devb   -> push that to github

> git checkout main

> git checkout -b deva-test   -> create a branch locally
> git push origin deva-test   -> push that to github
  
> git checkout main

> git checkout -b devb-test   -> create a branch locally
> git push origin devb-test   -> push that to github

Overall we will now have 4 branches

Step 3:
------------------------------------------------------------------------------------------

Make some changes and push

> git checkout deva-test

Do the modifications

> git add .
> git commit -m
> git push origin deva-test

You have worked on a specific branch, comitted and uploaded

It creates a Pull Request -> You can accept it or reject it

Step 4:
------------------------------------------------------------------------------------------

Since the Pull Request was accepted in the GitHub and the changes was merged into Main
We will now sync the local repository, because the local repository is not reflecting the 
merge

> git pull origin main