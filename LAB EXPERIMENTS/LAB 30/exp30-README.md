# Experiment 30: Forking, Feature Branch and Pull Request to the Original Repository

**Tool:** Git/GitHub &nbsp;|&nbsp; **Course Outcome:** CO4 &nbsp;|&nbsp; **Course:** CSA10 Software Engineering

## Aim

To fork a team member’s repository, clone it, create a feature branch, implement a feature without affecting existing code, push it to the fork and submit a pull request to the original repository.

## Procedure outline

1. Fork the Repository
2. Clone the Forked Repository
3. Create a Feature Branch
4. Implement the Feature
5. Verify the Changes
6. Stage and Commit the Changes
7. Push the Feature Branch
8. Create a Pull Request
9. Verify the Pull Request

## Expected output

Fork of 3-Simple-Python-Projects created and cloned.

Branch feature-update created; ytDownloader.py modified, committed (“Added project info feature”) and pushed.

Pull request from the fork’s feature-update branch to the original repository’s main branch is opened.

## GitHub deliverables (what to commit in this folder)

- [ ] URL of your fork and of the original repository
- [ ] Screenshot of branch `feature-update`, commit and push
- [ ] Pull-request URL to the original repository
- [ ] Screenshot of the open PR

## Screenshots to capture (save in `screenshots/`)


## Links

Fill these in `links.md` before submitting.

## Result

Thus the repository was forked and cloned, a feature was implemented on a separate branch, pushed to the fork and a pull request was submitted to the original repository.

<details><summary>Viva voce questions</summary>

**1. What is upstream?**

Ans: The original repository from which a fork was created.

**2. How do you keep a fork in sync?**

Ans: git fetch upstream and git merge upstream/main (or Sync fork on GitHub).

**3. Can you push directly to the original repository?**

Ans: Not without write access; you use a pull request instead.

**4. Why implement the feature on a new branch?**

Ans: So existing code on main is not affected.

**5. What is shown in the Files changed tab of a PR?**

Ans: The line-by-line diff of all modified files.

Department of Computer Science and Engineering  |  Page 1

</details>
