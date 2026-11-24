# Experiment 27: Committing and Pushing Changes to GitHub

**Tool:** Git/GitHub &nbsp;|&nbsp; **Course Outcome:** CO4 &nbsp;|&nbsp; **Course:** CSA10 Software Engineering

## Aim

To modify a file in a cloned repository, stage and commit the changes with a meaningful message, and push them to the remote GitHub repository.

## Procedure outline

1. Clone the Repository
2. Navigate to the Repository
3. Open the Repository and Modify the File
4. Check the Repository Status
5. Stage the Changes
6. Commit the Changes
7. Push the Changes to GitHub
8. Verify the Changes

## Expected output

git commit -m "Updated README" shows 1 file changed.

git status shows the branch ahead of origin/main by 1 commit; after git push it is up to date.

The updated README is visible on GitHub with the new commit message.

## GitHub deliverables (what to commit in this folder)

- [ ] Screenshots of `git commit`, `git status` (ahead by 1) and `git push`
- [ ] Screenshot of the commit on GitHub

## Screenshots to capture (save in `screenshots/`)


## Links

Fill these in `links.md` before submitting.

## Result

Thus the changes made to the cloned repository were staged, committed and pushed to GitHub successfully.

<details><summary>Viva voce questions</summary>

**1. What is a commit?**

Ans: A snapshot of staged changes with metadata and a message.

**2. How do you change the last commit message?**

Ans: git commit --amend -m "new message" (before pushing).

**3. What does “ahead of origin/main by 1 commit” mean?**

Ans: There is one local commit not yet pushed.

**4. How do you stage all changed files?**

Ans: git add . or git add -A.

**5. What is HEAD?**

Ans: A pointer to the current branch’s latest commit.

</details>
