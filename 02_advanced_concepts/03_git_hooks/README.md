# Git Hooks and Automation

Git hooks are scripts that Git executes before or after events such as commit, push, and receive. They're perfect for automating tasks and enforcing standards.

## Types of Git Hooks

### Client-Side Hooks
- `pre-commit`: Runs before commit message is created
- `prepare-commit-msg`: Runs before commit message editor is started
- `commit-msg`: Runs after commit message is created
- `post-commit`: Runs after commit is completed
- `pre-rebase`: Runs before rebase operation
- `post-checkout`: Runs after checkout operation
- `post-merge`: Runs after merge operation
- `pre-push`: Runs before push operation

### Server-Side Hooks
- `pre-receive`: Runs before references are updated
- `update`: Runs before each reference is updated
- `post-receive`: Runs after all references are updated

## Setting Up Git Hooks

### 1. Create Hooks Directory
```bash
mkdir -p .git/hooks
```

### 2. Create Pre-commit Hook
```bash
#!/bin/sh

# Run tests
python -m pytest tests/

# Check code style
black --check .
flake8 .

# Check for sensitive data
if git diff --cached | grep -E "password|secret|key"; then
    echo "Error: Found potential sensitive data in commit"
    exit 1
fi
```

### 3. Make Hook Executable
```bash
chmod +x .git/hooks/pre-commit
```

## Example: Pre-commit Hook for Python Project

Create `.git/hooks/pre-commit`:
```bash
#!/bin/sh

# Get list of staged Python files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=d | grep '\.py$')

if [ -n "$STAGED_FILES" ]; then
    # Run tests
    python -m pytest tests/
    TEST_RESULT=$?

    # Format code
    black $STAGED_FILES
    git add $STAGED_FILES

    # Check code style
    flake8 $STAGED_FILES
    STYLE_RESULT=$?

    # Exit if tests or style checks failed
    if [ $TEST_RESULT -ne 0 ] || [ $STYLE_RESULT -ne 0 ]; then
        echo "Pre-commit checks failed. Please fix the issues and try again."
        exit 1
    fi
fi
```

## Exercise: Implementing Git Hooks

1. **Setup Pre-commit Hook**
   - Create a pre-commit hook that:
     - Runs tests
     - Checks code style
     - Validates commit messages

2. **Setup Pre-push Hook**
   - Create a pre-push hook that:
     - Ensures all tests pass
     - Checks for sensitive data
     - Validates branch naming

3. **Setup Commit Message Hook**
   - Create a commit-msg hook that:
     - Enforces commit message format
     - Validates ticket references
     - Checks message length

## Best Practices

1. **Keep Hooks Lightweight**
   - Hooks should run quickly
   - Avoid heavy operations
   - Use caching when possible

2. **Provide Clear Feedback**
   - Explain what failed
   - Give instructions for fixing
   - Include relevant error messages

3. **Version Control Hooks**
   - Store hooks in project repository
   - Use a hooks directory
   - Document hook requirements

## Common Issues and Solutions

### Issue 1: Hook Not Executing
```bash
# Solution: Check permissions
chmod +x .git/hooks/pre-commit
```

### Issue 2: Hook Too Slow
```bash
# Solution: Add caching
if [ -f ".git/hooks/cache" ]; then
    # Use cached results
else
    # Run checks and cache results
fi
```

### Issue 3: Hook Breaking CI
```bash
# Solution: Skip hooks in CI
if [ "$CI" = "true" ]; then
    exit 0
fi
```

## Next Steps

In the next section, we'll learn about:
- Advanced Git workflows
- CI/CD integration
- Automated testing
- Deployment automation 