# Experiment 24: CI/CD Pipeline for a Flask Application using GitHub Actions with Cloud Deployment

**Tool:** GitHub Actions, Docker &nbsp;|&nbsp; **Course Outcome:** CO3 &nbsp;|&nbsp; **Course:** CSA10 Software Engineering

## Aim

To create a CI/CD pipeline with GitHub Actions for a containerized Flask application that automatically tests the code, builds and pushes the Docker image to Docker Hub and deploys the application to a cloud platform (Heroku / AWS).

## Procedure outline

1. Set Up the Repository and Flask Application
2. Create the Cloud Application and Secrets
3. Define the GitHub Actions Workflow
4. Push the Code and Trigger the Pipeline
5. Verify Testing, Image and Deployment
6. Test the Pipeline with a Failing and a Passing Change

## Expected output

Actions run shows jobs test → build-and-push → deploy completed successfully.

pytest reports 2 passed.

Docker Hub shows the new image; the deployment link (e.g. https://<app-name>.herokuapp.com) displays the Flask application.

## GitHub deliverables (what to commit in this folder)

- [ ] the `exp24-*` project files as its own repo (app.py, test_app.py, requirements.txt, Dockerfile, `.github/workflows/ci-cd.yml`)
- [ ] Screenshot of the Actions run (test → build-and-push → deploy)
- [ ] Screenshot of `pytest` = 2 passed, Docker Hub image and live URL

> **Separate repository needed:** this experiment runs from its own repository (`flask-cicd`). Push the contents of the `exp24-*` project files as a repo of that name (GitHub Actions only reads `.github/workflows/` from the repository root). Then paste its URL into `links.md` here.

## Screenshots to capture (save in `screenshots/`)


## Links

Fill these in `links.md` before submitting.

## Result

Thus a CI/CD pipeline was created with GitHub Actions that tests, builds and pushes the Docker image of the Flask application and deploys it to the cloud automatically.

<details><summary>Viva voce questions</summary>

**1. What does the needs keyword do?**

Ans: Makes a job wait for the successful completion of another job.

**2. Why are tests run before building the image?**

Ans: To prevent broken code from being packaged and deployed.

**3. How does Heroku know which port to use?**

Ans: It sets the PORT environment variable that the app must listen on.

**4. What is pytest?**

Ans: A Python testing framework for writing and running unit tests.

**5. What triggers this workflow?**

Ans: A push or pull request to the main branch (and optionally manual dispatch).

</details>
