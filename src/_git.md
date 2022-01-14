# Git commands
## Set-up repro
- `git --version`
- `git init`
- `git status`
- `git diff { filename }` Shows differences since last commit
- `git show HEAD`
- `git checkout { commit }` Updates HEAD
- `git config --global user.name { username }`
- `git config --global user.email { email }`

## Commits
### Create a commit
- ` git add . ` Adds all files to the index. Index is a snapshot of the working tree.
[-> docs](https://git-scm.com/docs/git-add)
- ` git commit -m "Whitespaces. Capitalization. Imperative. No period" ` Saves content of current index.
[-> docs](https://git-scm.com/docs/git-commit)
- ` git commit -am " " ` Adds and commits in one command
- ` git rm { filename } ` Removes file from index. Not from directory
[-> docs](https://git-scm.com/docs/git-rm)

### Modify a commit
- `git reset .` : Unstage files from index. Rewrites history.
[-> docs](https://git-scm.com/docs/git-reset)
- `git revert .` : Undoes changes from previous commit. Creates new commit.
[-> docs](https://git-scm.com/docs/git-revert)
- `git stash` : Puts all uncommitted changes away. Creates a clean directory.
[-> docs](https://git-scm.com/docs/git-stash)
- `git commit --amend -m "Message"` : Rewrites last comment

## Remotes
- `git clone { url }` Creates new directory and clones repo
- `git clone https://$ {username }:${ password }@{ url }` Clones with personal pasword
- `git clone https://{ username }:{ token }@{ url }` Clones with personal token.
[-> docs](https://git-scm.com/docs/git-clone)
- `git fetch` Retrieves references from remote.
[-> docs](https://git-scm.com/docs/git-fetch)
- `git push` Updates remote with local references
- `git push --set-upstream origin { branch-name }` : Push branch to GitHub.
[-> docs](https://git-scm.com/docs/git-push)
- `git pull` Combines git fetch and git merge.
[-> docs](https://git-scm.com/docs/git-pull)
- `git remote` Returns name of remote
- `git remote add { name } { url }` : Add a remote with a specific name
- `git remote add origin { url }`

### Pull remote branch to local
1. `git checkout --track origin/{ branch-name }`

### Force pull to local branch
1. `git fetch --all`
2. `git reset --hard origin/{ branch-name }`
 
## Branches
- `git branch` Shows branches
- `git branch { branch-name }` Creates new branch
- `git checkout { branch-name }` Switches to branch
- `git checkout -b { branch-name }` Creates branch and switches
- `git branch -d { branch-name }`
- `git push { remote-name } --delete { branch-name }` delet branch on remote
- `git reflog` 
- `git log`
- `git reset --hard { commit }` Reset to that version
- `git reset --hard origin/master` Reset to its origin version from GitHub

## Merges
- `git merge { branch-name }` Merges branch-name in current branch. 
[-> docs](https://git-scm.com/docs/git-merge)

1. git merge
2. git add .
3. git commit
4. merge commit message pops up
5. enter commit message and edit with :wa
6. ESC and exi with :wq

## Tagging
- `git tag` Lists all tagss
- `git tag -a v1.0 -m "my version 1.0"` Creates a tag
- `git show v1.0` Shows detail information about specific tag
- `git -d v1.0` Deletes tag
[-> docs](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
