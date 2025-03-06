---
layout: default
title: Basic Git Commands
permalink: /01_basic_concepts/02_basic_commands/
progress: 20
previous: /01_basic_concepts/01_introduction/
next: /01_basic_concepts/03_working_with_files/
---

# Basic Git Commands

In this section, we'll explore the fundamental Git commands that you'll use on a daily basis.

## Essential Commands

### 1. git init
Initializes a new Git repository in the current directory.

```bash
git init
```

### 2. git status
Shows the current state of your working directory and staging area.

```bash
git status
```

### 3. git add
Adds files to the staging area.

```bash
# Add a specific file
git add filename.txt

# Add all files
git add .
```

### 4. git commit
Creates a new commit with the staged changes.

```bash
git commit -m "Your commit message"
```

### 5. git log
Shows the commit history.

```bash
# Basic log
git log

# Compact log
git log --oneline

# Graphical log
git log --graph --oneline --all
```

### 6. git diff
Shows changes between commits, branches, or the working directory.

```bash
# Show changes in working directory
git diff

# Show changes in staging area
git diff --staged

# Show changes between commits
git diff commit1 commit2
```

## Working with Files

### 1. git rm
Removes files from Git tracking.

```bash
# Remove file from Git and filesystem
git rm filename.txt

# Remove file from Git only
git rm --cached filename.txt
```

### 2. git mv
Moves or renames files.

```bash
git mv oldname.txt newname.txt
```

## Practice Exercises

1. Create a new directory and initialize a Git repository
2. Create three files with different content
3. Stage and commit each file separately
4. Make changes to one file and view the differences
5. View the commit history in different formats

## Next Steps

In the next section, we'll learn about:
- Working with files in detail
- Understanding the Git workflow
- Common Git operations
- Best practices for commits

[Continue to Working with Files →](/01_basic_concepts/03_working_with_files/) 