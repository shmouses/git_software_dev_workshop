---
layout: default
title: Merging in Git
permalink: /git_software_dev_workshop/02_advanced_concepts/02_merging/
progress: 50
previous: /git_software_dev_workshop/02_advanced_concepts/01_branching/
next: /git_software_dev_workshop/03_team_collaboration/01_forking_and_remote/
---

# Merging in Git

Learn how to combine changes from different branches using Git's merging capabilities.

## Types of Merges

### 1. Fast-forward Merge
When the target branch is directly ahead of the current branch.

```bash
# Switch to main branch
git checkout main

# Merge feature branch
git merge feature-branch
```

### 2. Three-way Merge
When branches have diverged and need to be combined.

```bash
# Merge with conflict resolution
git merge feature-branch
```

### 3. Rebase
Alternative to merging that creates a linear history.

```bash
# Rebase feature branch onto main
git checkout feature-branch
git rebase main
```

## Merge Conflicts

### 1. Identifying Conflicts

```bash
# Check status
git status

# View conflicts
git diff
```

### 2. Resolving Conflicts

1. Open conflicted files
2. Choose changes or combine them
3. Remove conflict markers
4. Stage resolved files
5. Complete the merge

```bash
# After resolving conflicts
git add resolved-file.txt
git commit -m "Resolve merge conflicts"
```

## Merge Strategies

### 1. Recursive Merge
Default strategy for three-way merges.

```bash
git merge -X theirs feature-branch
```

### 2. Octopus Merge
For merging multiple branches.

```bash
git merge branch1 branch2 branch3
```

### 3. Ours/Theirs
Prefer changes from one branch.

```bash
# Prefer current branch
git merge -X ours feature-branch

# Prefer feature branch
git merge -X theirs feature-branch
```

## Best Practices

1. Keep branches up to date
2. Test before merging
3. Use meaningful commit messages
4. Review changes before merging
5. Clean up after merging

## Practice Exercises

1. Create and merge feature branches
2. Resolve merge conflicts
3. Practice different merge strategies
4. Clean up merged branches
5. Review merge history

## Next Steps

In the next section, we'll learn about:
- Working with remote repositories
- Forking repositories
- Pull requests
- Collaboration workflows

[Continue to Forking and Remote Repositories →](/git_software_dev_workshop/03_team_collaboration/01_forking_and_remote/) 