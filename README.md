# CI/CD Pipeline: GitHub Actions → Docker → AWS EC2

This repository contains a simple Flask application with a complete CI/CD pipeline built using **GitHub Actions**, **Docker**, and deployed on an **AWS EC2 instance**.

Whenever code is pushed to the `main` branch, a GitHub Actions workflow is triggered that:

- Builds a Docker image
- Runs tests using `pytest`
- Deploys the app on a running EC2 instance via SSH

---

## Tutorial & Explanation

Want to understand how this works step-by-step?  
I’ve written a complete hands-on guide with setup instructions, YAML explanation, and diagram walkthrough.

**Read the full tutorial on Medium**:  
**[How to Build CI/CD Pipeline with GitHub Actions and Deploy to EC2](https://prasadkhatake.medium.com/create-ci-cd-pipeline-using-github-actions-and-deploy-app-on-aws-ec2-c987ce5c2791)**

---

##  Technologies Used

- Python (Flask)
- Docker
- GitHub Actions
- AWS EC2


---

## Project Structure

```

.
├── app.py             # Main Flask server
├── tests.py           # Basic test case
├── Dockerfile         # Docker config to build image
├── .github/
│   |── workflows/
│       |── cicd.yaml  # GitHub Actions workflow file

````



---

## Setup

If you want to run locally:

```bash
# Run server
python3 app.py

# Run tests
pytest tests.py
