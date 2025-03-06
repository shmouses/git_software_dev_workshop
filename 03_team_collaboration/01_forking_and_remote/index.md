---
layout: default
title: Forking and Remote Repositories
permalink: /03_team_collaboration/01_forking_and_remote/
progress: 60
previous: /02_advanced_concepts/02_merging/
next: /03_team_collaboration/02_pull_requests/
---

# Forking and Remote Repositories

Learn how to work with remote repositories and collaborate with others using forks.

## Remote Repositories

A remote repository is a version of your project that is hosted on the internet or network.

### Adding Remotes

```bash
# Add a remote repository
git remote add origin https://github.com/username/repository.git

# View remotes
git remote -v
```

### Working with Remotes

```bash
# Fetch changes from remote
git fetch origin

# Pull changes from remote
git pull origin main

# Push changes to remote
git push origin main
```

## Forking

Forking is creating a copy of a repository on GitHub that you can modify without affecting the original.

### Fork Workflow

1. Fork the repository on GitHub
2. Clone your fork locally
3. Add the original repository as upstream
4. Make changes and push to your fork
5. Create a pull request

### Setting Up Your Fork

```bash
# Clone your fork
git clone https://github.com/your-username/repository.git

# Add the original repository as upstream
git remote add upstream https://github.com/original-owner/repository.git

# Verify remotes
git remote -v
```

### Keeping Your Fork Updated

```bash
# Fetch changes from upstream
git fetch upstream

# Merge upstream changes into your local main
git checkout main
git merge upstream/main

# Push changes to your fork
git push origin main
```

## Best Practices

1. Keep your fork up to date
2. Use feature branches
3. Write clear commit messages
4. Follow the project's contribution guidelines
5. Test your changes before submitting

## Practice Exercises

1. Fork a repository on GitHub
2. Clone your fork locally
3. Add the original repository as upstream
4. Create a feature branch
5. Make changes and push them to your fork

## Next Steps

In the next section, we'll learn about:
- Creating pull requests
- Code review process
- Managing pull requests
- Collaboration best practices

[Continue to Pull Requests →](/git_software_dev_workshop/03_team_collaboration/02_pull_requests/) 