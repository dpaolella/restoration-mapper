
1. Create a fork of David’s repository
* Do it in the GUI online
* Copy the url
2. Follow these steps to set upstream
```
# Add 'upstream' repo to list of remotes
git remote add upstream https://github.com/UPSTREAM-USER/ORIGINAL-PROJECT.git

# Verify the new remote named 'upstream'
git remote -v
```
    * Whenever you want to update your fork with the latest upstream changes, you'll need to first fetch the upstream repo's branches and latest commits to bring them into your repository:
``` 
# Fetch from upstream remote
git fetch upstream

# View all branches, including those from upstream
git branch -va
```   
 * Now, checkout your own master branch and merge the upstream repo's master branch:
``` 
# Checkout your master branch and merge upstream
git checkout master
git merge upstream/master
```

# Daniel added:
git push origin master
3. Follow below steps to make your master up to date with fork (by fork I will always mean David’s repository)
4. Checkout your own master
    * Git checkout master
5. Create your own branch
    * Git checkout -b <your_name>
6. Make sure that branch exists on GitHub
    * git push --set-upstream origin my-branch
7. Work on your local files
8. Commit them
    * Git add .
    * Git commit -m “your note"
9. Push them to github
    * Git push origin
    * 
When you are ready to share with the rest of the team:
1. Make sure it doesn’t conflict with the master
# Fetch upstream master and merge with your repo's master branch
git fetch upstream
git checkout master
git merge upstream/master


# If there were any new commits, rebase your development branch
git checkout newfeature
git rebase master
2. Commit your local, merge conflict free branch
3. Push to GitHub 
4. Go to GitHub GUI and create a pull request
    * It will automatically compare it to the fork
    * Select master branch from David’s repository vs your named branch
    * Write explainer of the work you did
5. Merge it in yourself or wait for approval

To start working on your branch again:
1. Fetch the forked repository
    * Git fetch upstream
2. Check out your master
    * Git checkout master
3. Merge in the fork
    * Git merge upstream/master
4. Push to your github
    * Git push origin
5. Checkout your branch again
    * Git checkout daniel
6. Merge master into it
    * Git merge master
    * —> This will do a “fast-forward” and it should say that as an output in your terminal

Done

