# Experiment 28: Pulling Collaborator Changes from GitHub

**Tool:** Git/GitHub &nbsp;|&nbsp; **Course Outcome:** CO4 &nbsp;|&nbsp; **Course:** CSA10 Software Engineering

## Aim

To pull the latest changes made by a collaborator from the GitHub repository into the local repository and verify that the local copy is up to date.

## Procedure outline

1. Clone the Repository
2. Navigate to the Repository
3. Ask the Collaborator to Make Changes
4. Check the Local Repository
5. Pull the Latest Changes
6. Verify the Pulled Changes
7. Confirm the Repository is Updated

## Expected output

Collaborator’s commit “Updated README by collaborator” is pushed to GitHub.

git pull origin main shows Fast-forward, 1 file changed.

README.md in VS Code shows the collaborator’s change; git status reports the branch is up to date.

## GitHub deliverables (what to commit in this folder)

- [ ] Collaborator's commit on GitHub (screenshot)
- [ ] Screenshot of `git pull origin main` (Fast-forward)
- [ ] Screenshot of README in VS Code showing the change

## Links

Fill these in `links.md` before submitting.

## Result

Thus the latest changes made by the collaborator were pulled from GitHub and verified in the local repository.

<details><summary>Viva voce questions</summary>

**1. Differentiate git pull and git fetch.**

Ans: fetch only downloads; pull downloads and merges.

**2. What is a Fast-forward?**

Ans: When the local branch has no new commits, Git simply moves the pointer to the remote commit.

**3. How do you add a collaborator?**

Ans: Repository Settings → Collaborators → Add people.

**4. What happens if both of you changed the same line?**

Ans: git pull reports a merge conflict that must be resolved manually.

**5. What is git pull --rebase?**

Ans: It replays local commits on top of the fetched commits instead of creating a merge commit.

</details>
