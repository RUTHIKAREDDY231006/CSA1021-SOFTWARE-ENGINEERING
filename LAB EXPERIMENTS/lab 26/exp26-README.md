# Experiment 26: Cloning a GitHub Repository and Editing Files Locally

**Tool:** Git/GitHub &nbsp;|&nbsp; **Course Outcome:** CO3 &nbsp;|&nbsp; **Course:** CSA10 Software Engineering

## Aim

To clone an existing GitHub repository to the local machine, navigate into it, open it in an editor and modify a file.

## Procedure outline

1. Select a GitHub Repository
2. Clone the Repository
3. Navigate to the Repository Directory
4. Open the Repository and Modify the File
5. Verify the Changes
6. Save the Updated File

## Expected output

git clone reports “Cloning into 'My-Personal-Project'… done.”

ls lists the repository files; README.md opens in VS Code.

After editing and saving, git status shows modified: README.md.

## GitHub deliverables (what to commit in this folder)

- [ ] Screenshot of `git clone`, `ls`, VS Code with README open
- [ ] Screenshot of `git status` showing `modified: README.md`

## Screenshots to capture (save in `screenshots/`)


## Links

Fill these in `links.md` before submitting.

## Result

Thus an existing GitHub repository was cloned to the local machine and a file was opened and modified successfully.

<details><summary>Viva voce questions</summary>

**1. What does git clone copy?**

Ans: All files, branches and the full history of the repository.

**2. What is git remote -v?**

Ans: A command that lists the remote URLs for fetch and push.

**3. Which command shows the changes made to a file?**

Ans: git diff.

**4. Differentiate HTTPS and SSH cloning.**

Ans: HTTPS uses a token for authentication; SSH uses a key pair.

**5. Can you clone a private repository?**

Ans: Yes, if you have access and authenticate.

</details>
