---
layout: default
title: Branching in Git
permalink: /02_advanced_concepts/01_branching/
progress: 40
previous: /01_basic_concepts/03_working_with_files/
next: /02_advanced_concepts/02_merging/
---

# Branching in Git

Branching is one of Git's most powerful features, allowing you to work on multiple features or versions simultaneously.

## What is a Branch?

A branch is a lightweight movable pointer to a commit. The default branch is called `main` (or `master` in older repositories).

## Basic Branch Commands

### 1. Creating Branches

```bash
# Create a new branch
git branch feature-name

# Create and switch to a new branch
git checkout -b feature-name
```

### 2. Switching Branches

```bash
# Switch to an existing branch
git checkout branch-name

# Switch to main branch
git checkout main
```

### 3. Listing Branches

```bash
# List all local branches
git branch

# List all branches (local and remote)
git branch -a
```

### 4. Deleting Branches

```bash
# Delete a local branch
git branch -d branch-name

# Force delete a branch
git branch -D branch-name
```

## Branch Workflow

1. Create a new branch for your feature
2. Make changes and commit them
3. Switch back to main
4. Merge your feature branch
5. Delete the feature branch

## Best Practices

1. Use descriptive branch names
2. Keep branches focused and small
3. Regularly update your branches with main
4. Delete branches after merging
5. Use feature branches for new features

## Practice Exercises

1. Create a new feature branch
2. Make some changes and commit them
3. Switch back to main
4. Create another branch for a different feature
5. View all branches and their status

## Next Steps

In the next section, we'll learn about:
- Merging branches
- Resolving merge conflicts
- Advanced branching strategies
- Branch management best practices

[Continue to Merging →](/git_software_dev_workshop/02_advanced_concepts/02_merging/) 