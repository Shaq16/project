# Install Git
sudo apt update
sudo apt install git -y

# Configure Git
git config --global user.name "YourName"
git config --global user.email "yourmail@gmail.com"

# Verify Configuration
git config --global user.name
git config --global user.email

# Create Project Folder
mkdir project
cd project

# Initialize Local Git Repository
git init

# Create File
echo "Hello DevOps" > app.py

# Check Repository Status
git status

# Add File to Staging Area
git add app.py

# Add All Files
git add .

# Commit Changes
git commit -m "Initial Commit"

# View Commit History
git log

# One-Line Commit History
git log --oneline

# View Uncommitted Changes
git diff

# Clone Existing Repository
git clone https://github.com/username/repository.git

# Connect Local Repo to GitHub Repo
git remote add origin https://github.com/username/repository.git

# Verify Remote Repository
git remote -v

# Push Code to GitHub
git push -u origin master

# Pull Latest Changes from GitHub
git pull origin master
