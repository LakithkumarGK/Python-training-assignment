Initialize Git on a folder, making it a Repository [How?]
Git now creates a hidden folder to keep track of changes in that folder
When a file is changed, added or deleted, it is considered modified

You select the modified files you want to Stage
The Staged files are Committed, which prompts Git to store a permanent snapshot of the files [How?]
Snapshot means the current state of the files that are being tracked. [How?]


Git allows you to see the full history of every commit. [How?]
You can revert back to any previous commit. [How?]
Git does not store a separate copy of every file in every commit, but keeps track of changes made in each commit!

-----------------------------------------------------------------------------------------------------

Global settings (one time execution)
> git config --global user.name purushotham
> git config --global user.email purushotham@mindfullearing.in


Consider: .\day-27\workspace
Convert this into a git repository
> git init

Add a file and check the status:
> git add sample.txt
> git status

Commit with a message
> git commit -m "This is the first commit"

List the commits
> git log 

Check the staging area
> git status     
There will be no files that are tracked because you just commited

Modify sample.txt and words.txt, and do another commit
> git add sample.txt words.txt


Going back to a previous commit TEMPORARILY:
> git log --oneline

output ->
f716432 (HEAD -> master) This is second commit
7601da8 This is a first commit

Going back to first commit
> git checkout 7601da8

You will go back to the previous commit


Comming back to the latest:
> git checkout master   

NOTE: checkout is a multi-purpose command


-----------------------------------------------------------------------

Reset to a previous commit
git reset <commit-hash> 

You pushed a commit and want to undo it:
git revert <commit-hash>