# For just one repo, go into to the relevant repo DIR and:
git config --local user.name "phulikely"
git config --local user.email "phulikely@gmail.com"


#For (global) default email (which is configured in your ~/.gitconfig):
git config --global user.name "Your Name Here"
git config --global user.email your@email.example


# You can check your Git settings with: 
git config user.name && git config user.email

-------------------------------------------------------

# Show current status
git stash show
# If nothing then
git stash

# Do something and apply your changes(which you have been saved by git stash)
git stash apply

# Show again
git stash show

# Clear all stash
git stash clear



-----
my branch: R-002-Optimize-Code-SLES15SP1-Sybase-Phuch
git rebase R-002-Optimize-Code
git log

git checkout R-002-Optimize-Code
git merge R-002-Optimize-Code-SLES15SP1-Sybase-Phuch

-----

# Undo a Git commit that was not pushed:
    # Method 1: Undo commit and keep all files staged
    git reset --soft HEAD~
    
    # Method 2: Undo commit and unstage all files
    git reset HEAD~
    
    # Method 3: Undo the commit and completely remove all changes
    git reset --hard HEAD~

-----

# Delete branch locally
git branch -d localBranchName

# Delete branch remotely
git push origin --delete remoteBranchName
