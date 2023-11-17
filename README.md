# Release Note Generator
## Simply drop in a commit history from Github or any other platform and create a nicely release not format

## Install SymbolicAI & Package

See more info at the original [Repository](https://github.com/ExtensityAI/symbolicai).

1. Install the SymbolicAI framework:
```bash
pip install symbolicai
```

2. Use the builtin `sympkg` to install the package
```bash
sympkg i ExtensityAI/releasenote
```
3. Create an alias for the `relese` command
```bash
symrun c release ExtensityAI/releasenote
```

## Usage:

Now simply call:
```bash
symrun release "<your commit history>"
```

Example:
```bash
symrun release "Commits on Nov 17, 2023
Update README.md

@Xpitfire
Xpitfire committed 6 minutes ago
Commits on Aug 5, 2023
switched instruction to yaml format

@futurisold
futurisold committed on Aug 5
Commits on Aug 3, 2023
fixed typo
..."
```
