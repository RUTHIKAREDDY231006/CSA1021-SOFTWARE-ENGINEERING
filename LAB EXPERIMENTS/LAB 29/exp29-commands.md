# Experiment 29 – command log

Copy the commands you actually ran (with your own username/URLs) and attach their output as screenshots.

**Verify that the repository is up to date with the main branch.**

```bash
cd ~/Desktop/My-Personal-Project
git status
```

**Switch to the newly created branch using the following command.**

```bash
git checkout -b feature-login
```

**Verify that the feature branch is active.**

```bash
git branch
```

**Open the project in Visual Studio Code.**

```bash
code .
```

**Check the repository status to verify that login.py is detected as a new file.**

```bash
git status
```

**Add the new login.py file to the staging area.**

```bash
git add login.py
```

**Commit the changes with a meaningful commit message.**

```bash
git commit -m "Added login function"
```

**Push the feature-login branch to the GitHub repository.**

```bash
git push -u origin feature-login
```

**Switch to the main branch locally.**

```bash
git checkout main
```

**Pull the latest changes from GitHub.**

```bash
git pull origin main
```

**Verify that login.py is present in the project.**

```bash
ls
```
