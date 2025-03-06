# Introduction to Version Control and Git

## What is Version Control?

Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. It's like having a time machine for your code!

### Why Use Version Control?

1. **Track Changes**: See who made what changes and when
2. **Collaborate**: Work with others without overwriting each other's work
3. **Backup**: Keep your code safe and recover from mistakes
4. **Branching**: Work on new features without affecting the main code
5. **History**: Understand how and why your code evolved

## What is Git?

Git is a distributed version control system that:
- Tracks changes in any set of files
- Coordinates work among multiple people
- Provides a complete history of changes
- Enables branching and merging

## Basic Git Concepts

### Repository
A repository (or "repo") is a collection of files and their complete history.

### Working Directory
The directory where you make changes to your files.

### Staging Area
A temporary area where you prepare changes before committing them.

### Commit
A snapshot of your changes at a specific point in time.

## Hands-on Exercise: Your First Git Repository

1. Create a new directory for your project:
```bash
mkdir my-first-git-project
cd my-first-git-project
```

2. Initialize a new Git repository:
```bash
git init
```

3. Create a simple text file:
```bash
echo "Hello, Git!" > hello.txt
```

4. Check the status of your repository:
```bash
git status
```

5. Add your file to the staging area:
```bash
git add hello.txt
```

6. Commit your changes:
```bash
git commit -m "My first commit"
```

7. View your commit history:
```bash
git log
```

## Practice Tasks

1. Create a new file called `notes.txt` and add some text to it
2. Stage and commit this new file
3. Make a change to `hello.txt`
4. Stage and commit this change
5. View the history of your repository

## Next Steps

In the next section, we'll learn about:
- Basic Git commands in detail
- Working with files
- Understanding the Git workflow
- Common Git operations 