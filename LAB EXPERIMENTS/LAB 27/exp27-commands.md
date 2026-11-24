# Experiment 27 – command log

Copy the commands you actually ran (with your own username/URLs) and attach their output as screenshots.

**Wait for the cloning process to complete successfully.**

```bash
git clone <repository_url>
```

**List the repository files to verify that the repository was cloned successfully.**

```bash
cd <repository_name>
ls
```

**Locate the file that needs to be modified, such as README.md or any source code file.**

```bash
code .
```

**Check the status of the repository to identify the modified file.**

```bash
git status
```

**Verify that the file has been staged successfully.**

```bash
git add README.md
git status
```

**Provide a meaningful commit message describing the modification.**

```bash
git commit -m "Updated README"
```

**Upload the committed changes from the local repository to the GitHub remote repository using git push.**

```bash
git push origin main
```
