# NMR 👾

A `node_modules/` remover 

## Goal

Safely remove all `node_modules/` in a set of node projects somewhere inside of Francisco's computer (LOL)

## Usage

`python3 nmr.py <folder0> <folder1> ...`

where:

- `folderN` is a folder containing ONE OR MORE node projects or folders (non node projects or node projects without `node_modules/` will be ignored).
Example (`folderN` should be `foo` and not `project1` or `project2`):
```
foo/
|
|
| project1/
    | node_modules/...
    | ...
| project2/
    | node_modules/...
    | ...
| ... 
```

## Some outputs

```
$ python3 nmr.py ~/Documents/github/
Allow nmr to delete the following folders? 
['/Users/XXXXX/Documents/github/XXXXX/node_modules/']
Type "yes" to confirm: yes
- /Users/XXXXX/Documents/github/XXXXX/node_modules/: deleted
--> 1 node_modules deleted.
```
