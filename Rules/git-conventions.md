# Git Conventions

## Branches
Branch names MUST follow the format `<group>/<branch-name>` where the group is one from the specification below.

- `develop` The primary branch
- `main/master` The production branch

- `fix/` A bugfix or hotfix for the user, not a fix to a build script
- `wip/` Long term work in progress not yet suited for the development branch 
- `docs/` Documentation changes; no production code change  
- `chore/` Updating grunt tasks etc; no production code change
- `style/` Formatting, missing semi colons, etc; no production code change
- `feature/` New feature for the user, not a new feature for build script
- `refactor/` Refactoring production code, eg. renaming a variable; no functional change

- `release/` MUST be a stale branch (read-only) for a specific release, prefer using tagging if possible

Example:
`feature/add-new-view`

## Commits
Commit messages MUST be written in english, in present tense and be capitalized. A commit message MUST clearly state the changes made in about 75 characters per row. A commit title SHOULD not exceed 50 characters.

Code that is commited (or by other means used in a project) MUST be taken ownership for by the author of that commit. It is their responsibility to understand how and why it functions in a certain way. If asked by a colleague to commit code on their behalf it MUST be clearly stated in the message of that commit.

## Readme
All projects MUST have a readme that at least summarizes the project, it SHOULD also specify how to setup up a local development environment.

## Changelog
Projects MAY specify a file called CHANGELOG.md if approporiate based on the project's size and scope. The file MUST follow the Keepachangelog format. All versions specified should follow the semver format.

## Attribution
Never add attribution to git-commits such as "Co-Authored-By: <ai-name>" or "Co-Authored by: <ai-name>"

## Versioning
MUST follow the semver (Semantic Versioning) specification.

## Tagging
All released versions MUST be tagged with a tagname matching the version with a prepended v.

Example:
- Version `1.0.1-beta.1` → Tagname `v1.0.1-beta.1`
