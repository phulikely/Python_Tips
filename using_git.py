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
