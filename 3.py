# Install Java
sudo apt update
sudo apt install fontconfig openjdk-17-jre -y

# Add Jenkins key
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

# Add Jenkins repository
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
https://pkg.jenkins.io/debian-stable binary/" | \
sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

# Update packages
sudo apt update

# Install Jenkins
sudo apt install jenkins -y

# Start Jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins

# Check Jenkins status
sudo systemctl status jenkins

# Get Jenkins admin password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword


Jenkins Steps

1. Open
   http://localhost:8080

2. Install Plugin
   Manage Jenkins
   -> Plugins
   -> Available Plugins
   -> Search:
      Build Pipeline
   -> Install

--------------------------------------------------

Create Job1

3. New Item
   -> Freestyle Project
   -> Name:
      git_job

4. Source Code Management
   -> Git
   -> Paste GitHub Repo URL

5. Build Steps
   -> Execute Shell

6. Add:
   python3 test.py

7. Apply and Save

--------------------------------------------------

Create Job2

8. New Item
   -> Freestyle Project
   -> Name:
      job2

9. Build Steps
   -> Execute Shell

10. Add:
    echo "Job2 Running"
    date

11. Apply and Save

--------------------------------------------------

Create Job3

12. New Item
    -> Freestyle Project
    -> Name:
       job3

13. Build Steps
    -> Execute Shell

14. Add:
    echo "Job3 Running"
    pwd

15. Apply and Save

--------------------------------------------------

Pipeline Connections

16. Open git_job
    -> Configure
    -> Post-build Actions
    -> Build other projects
    -> Add:
       job2
    -> Save

17. Open job2
    -> Configure
    -> Post-build Actions
    -> Build other projects
    -> Add:
       job3
    -> Save

--------------------------------------------------

Pipeline Visualization

18. Dashboard
    -> Click +

19. View Name:
    pipeline_views

20. Select:
    Build Pipeline View

21. Create

22. Initial Job:
    git_job

23. Save

--------------------------------------------------

Run Pipeline

24. Open git_job
    -> Build Now

Pipeline Flow:

git_job
   ↓
job2
   ↓
job3
