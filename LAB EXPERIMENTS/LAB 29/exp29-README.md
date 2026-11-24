# Experiment 29: Feature Branch (feature-login) and Pull Request

**Tool:** Git/GitHub &nbsp;|&nbsp; **Course Outcome:** CO4 &nbsp;|&nbsp; **Course:** CSA10 Software Engineering

## Aim

To create a feature branch named feature-login, implement a simple login function in login.py, commit and push it, and create and merge a pull request into the main branch.

## Procedure outline

1. Open the GitHub Repository
2. Create the Feature Branch
3. Create the Login File
4. Check the Changes
5. Stage and Commit the Changes
6. Push the Feature Branch
7. Create a Pull Request
8. Review and Merge the Pull Request
9. Verify the Merged Feature

## Expected output

Branch feature-login created; login.py added and committed (“Added login function”).

Pull request “Add Login Function” created from feature-login to main and merged.

After git checkout main and git pull, login.py is present in main.

## GitHub deliverables (what to commit in this folder)

- [ ] `project/login.py`
- [ ] Screenshot of branch `feature-login`, commit and push
- [ ] Pull-request URL (`Add Login Function`) and merged-PR screenshot
- [ ] Screenshot of `ls` on `main` showing `login.py`

## Screenshots to capture (save in `screenshots/`)


## Links

Fill these in `links.md` before submitting.

## Result

Thus a feature-login branch was created, a login function was implemented, pushed and merged into the main branch through a pull request.

<details><summary>Viva voce questions</summary>

**1. What does git checkout -b do?**

Ans: Creates a new branch and switches to it.

**2. What does -u in git push -u do?**

Ans: Sets the upstream (tracking) branch.

**3. How do you delete a branch locally?**

Ans: git branch -d feature-login.

**4. What is git switch?**

Ans: A newer command to change branches (git switch -c creates one).

**5. Why should a feature be merged through a PR?**

Ans: To allow code review and checks before it reaches main.

</details>
