# Git Conflict Resolution

Learn how to handle and resolve merge conflicts effectively in Git.

## Understanding Merge Conflicts

Merge conflicts occur when Git can't automatically merge changes from different branches. This happens when:
- Same lines are modified in different branches
- One branch deletes a file while another modifies it
- Different branches modify the same section of code

## Types of Conflicts

### 1. Content Conflicts
```python
<<<<<<< HEAD
def calculate_total(items):
    return sum(item.price for item in items)
=======
def calculate_total(items):
    total = 0
    for item in items:
        total += item.price
    return total
>>>>>>> feature/discount
```

### 2. File Conflicts
- One branch deletes a file
- Another branch modifies the same file
- Git doesn't know which change to keep

### 3. Binary File Conflicts
- Conflicts in non-text files
- Git can't merge automatically
- Manual resolution required

## Resolving Conflicts

### 1. Identify Conflicts
```bash
# Check status
git status

# See conflicting files
git diff
```

### 2. Choose Resolution Strategy
1. **Accept Current Change**
```bash
git checkout --ours <file>
```

2. **Accept Incoming Change**
```bash
git checkout --theirs <file>
```

3. **Manual Resolution**
   - Edit files directly
   - Remove conflict markers
   - Keep desired changes

### 3. Complete Resolution
```bash
# Add resolved files
git add <file>

# Complete merge
git commit -m "Resolved merge conflicts"
```

## Exercise: Conflict Resolution Practice

### Setup
1. Create a new branch:
```bash
git checkout -b feature/new-feature
```

2. Make changes in main:
```bash
git checkout main
# Edit file
git add .
git commit -m "Update main branch"
```

3. Make conflicting changes in feature branch:
```bash
git checkout feature/new-feature
# Edit same file
git add .
git commit -m "Update feature branch"
```

4. Try to merge:
```bash
git merge main
```

### Resolution Steps
1. Identify conflicts
2. Choose resolution strategy
3. Edit files
4. Complete merge

## Best Practices

### 1. Prevention
- Keep branches up to date
- Communicate with team
- Make small, focused changes
- Regular merges to main

### 2. Resolution
- Understand changes before resolving
- Test after resolution
- Document resolution process
- Use merge tools when helpful

### 3. After Resolution
- Verify changes
- Run tests
- Update documentation
- Communicate with team

## Common Issues and Solutions

### Issue 1: Aborting Merge
```bash
# Solution: Abort merge
git merge --abort
```

### Issue 2: Stuck in Merge State
```bash
# Solution: Reset to last commit
git reset --hard HEAD
```

### Issue 3: Complex Conflicts
```bash
# Solution: Use merge tool
git mergetool
```

## Advanced Techniques

### 1. Interactive Rebase
```bash
git rebase -i HEAD~3
```

### 2. Cherry-pick
```bash
git cherry-pick <commit-hash>
```

### 3. Stash Changes
```bash
git stash
git stash pop
```

## Next Steps

In the next section, we'll learn about:
- Advanced Git workflows
- Branching strategies
- Release management
- Team collaboration 