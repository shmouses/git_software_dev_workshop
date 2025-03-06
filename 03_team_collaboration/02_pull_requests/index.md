---
layout: default
title: Pull Requests
permalink: /git_software_dev_workshop/03_team_collaboration/02_pull_requests/
progress: 70
previous: /git_software_dev_workshop/03_team_collaboration/01_forking_and_remote/
next: /git_software_dev_workshop/04_project_management/01_git_for_leaders/
---

# Pull Requests

Learn how to effectively create and manage pull requests for collaborative development.

## Creating Pull Requests

### 1. Basic Pull Request

1. Push your changes to a branch
2. Go to GitHub repository
3. Click "New Pull Request"
4. Select base and compare branches
5. Add description and create PR

### 2. Pull Request Best Practices

- Write clear titles
- Provide detailed descriptions
- Link related issues
- Include screenshots if needed
- Reference documentation

## Managing Pull Requests

### 1. Review Process

```bash
# Fetch latest changes
git fetch origin

# Update your branch
git checkout feature-branch
git rebase origin/main
```

### 2. Addressing Feedback

1. Make requested changes
2. Commit and push updates
3. Respond to comments
4. Request re-review if needed

### 3. Merging Pull Requests

- Ensure all checks pass
- Get required approvals
- Resolve conflicts if any
- Choose merge strategy
- Delete branch after merge

## Advanced Pull Request Features

### 1. Draft Pull Requests

- Mark PR as draft
- Get early feedback
- Convert to ready when complete

### 2. Pull Request Templates

Create `.github/pull_request_template.md`:
```markdown
## Description
[Describe your changes]

## Related Issue
[Link to issue]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update

## Testing
[Describe testing steps]
```

### 3. Review Comments

- Use inline comments
- Suggest changes
- Request changes
- Approve changes

## Best Practices

1. Keep PRs focused and small
2. Update PRs regularly
3. Respond to feedback promptly
4. Follow project guidelines
5. Clean up after merging

## Practice Exercises

1. Create a new feature branch
2. Make changes and push them
3. Create a pull request
4. Address review comments
5. Merge the pull request

## Next Steps

In the next section, we'll learn about:
- Git for project leaders
- Setting up project structure
- Workflow management
- Team collaboration

[Continue to Git for Project Leaders →](/git_software_dev_workshop/04_project_management/01_git_for_leaders/) 