---
layout: default
title: Working with Files in Git
permalink: /01_basic_concepts/03_working_with_files/
progress: 30
previous: /01_basic_concepts/02_basic_commands/
next: /02_advanced_concepts/01_branching/
---

# Working with Files in Git

Learn how to effectively manage files in your Git repository.

## File States

Files in Git can be in one of three states:
1. Modified (in working directory)
2. Staged (in staging area)
3. Committed (in repository)

## File Operations

### 1. Adding Files

```bash
# Add specific file
git add filename.txt

# Add all files
git add .

# Add files by pattern
git add *.txt
```

### 2. Removing Files

```bash
# Remove file from Git and filesystem
git rm filename.txt

# Remove file from Git only
git rm --cached filename.txt

# Remove directory
git rm -r directory/
```

### 3. Moving Files

```bash
# Move or rename file
git mv oldname.txt newname.txt
```

### 4. Ignoring Files

Create a `.gitignore` file:
```bash
# Ignore specific files
*.log
*.tmp

# Ignore directories
node_modules/
venv/

# Ignore all files in directory
directory/*
!directory/.gitkeep
```

## File Status

### 1. Checking Status

```bash
# Basic status
git status

# Short status
git status -s

# Ignored files
git status --ignored
```

### 2. Viewing Changes

```bash
# View changes in working directory
git diff

# View changes in staging area
git diff --staged

# View changes in specific file
git diff filename.txt
```

## Best Practices

1. Keep files focused and small
2. Use meaningful file names
3. Organize files logically
4. Keep sensitive data out of Git
5. Use .gitignore effectively

## Practice Exercises

1. Create a new directory structure
2. Add and commit multiple files
3. Move and rename files
4. Set up .gitignore
5. Practice file operations

## Next Steps

In the next section, we'll learn about:
- Branching in Git
- Creating and managing branches
- Branch workflows
- Branch best practices

[Continue to Branching →](/02_advanced_concepts/01_branching/) 