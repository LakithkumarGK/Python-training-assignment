Moving this workshop to include GitHub makes it real-world and collaborative — exactly what professionals need to learn. 
We'll now simulate two developers working on separate branches deva and devb, each with their own testing branches. 
Later, we'll simulate a bug fix and merge.

🌍 Part 1: Setup GitHub Repo and Clone Locally

✅ Step 1: Create a new GitHub repository
Go to https://github.com

Click New

Name it something like django-git-workshop

Keep it public or private

Do NOT initialize with README, .gitignore or license (we'll push from local first)

✅ Step 2: Clone it to your machine
On your machine:


git clone https://github.com/yourusername/django-git-workshop.git
cd django-git-workshop

Explanation:
👉 git clone <url> downloads the repo to your local machine.
Now you have a local copy linked to the remote GitHub repo.

✅ Step 3: Add your Django project to this folder


You can either create a new Django project or copy one in:


django-admin startproject myproject .
Then:


echo -e "*.pyc\n__pycache__/\ndb.sqlite3\n.env\n" > .gitignore
git add .
git commit -m "Initial Django project commit"
✅ Step 4: Push this to GitHub
bash
Copy
Edit
git push origin main
Explanation:
👉 git push origin main uploads the main branch to GitHub.

Now your GitHub repo has your Django code!

🌱 Part 2: Creating Feature and Test Branches

✅ Step 5: Create deva and devb branches

git checkout -b deva
git push origin deva

git checkout main
git checkout -b devb
git push origin devb
Explanation:
You simulate two developers working on separate branches.

✅ Step 6: Create testing branches from each

git checkout deva
git checkout -b deva-test
git push origin deva-test

git checkout devb
git checkout -b devb-test
git push origin devb-test
Now we have 4 branches on GitHub:

deva / deva-test

devb / devb-test

👨‍💻 Part 3: Make Changes and Push


✅ Step 7: Simulate work in deva-test

git checkout deva-test
# Add a view or modify a file in `blog/views.py`

git add .
git commit -m "Deva test: Added home view"
git push origin deva-test
👉 This shows how a developer:

Works in their branch

Commits code

Pushes to remote using git push origin <branch>

🔁 Part 4: Pulling and Syncing


✅ Step 8: Other dev pulls changes
Let’s simulate another dev working in devb-test:


git checkout devb-test
git pull origin devb-test
Explanation:

git pull origin devb-test fetches and merges changes from remote to local.

Useful when teammates push updates and you want to sync.

🐛 Part 5: Simulate Bug & Fix


✅ Step 9: Introduce a bug in deva-test
Modify a file and make a syntax error (like a missing parenthesis), then commit and push:


git commit -am "Introduced bug"
git push origin deva-test



✅ Step 10: Create a bug fix branch from deva-test
bash
Copy
Edit
git checkout -b deva-bugfix
# Fix the bug in code
git commit -am "Fixed bug in home view"
git push origin deva-bugfix
Now:

You can open a Pull Request (PR) on GitHub from deva-bugfix → deva-test

Or merge locally:


git checkout deva-test
git merge deva-bugfix
git push origin deva-test
🔀 Part 6: Merge to Main
Once tested:


git checkout deva
git merge deva-test
git push origin deva

git checkout main
git merge deva
git push origin main
🧠 Summary of Key Git/GitHub Concepts

Command	Purpose
git clone	Download remote repo to local
git add	Stage file(s) for commit
git commit	Save staged changes locally
git push origin <branch>	Upload changes to GitHub
git pull origin <branch>	Download changes from GitHub
git checkout -b <branch>	Create and switch to a new branch
git merge <branch>	Merge another branch into current
