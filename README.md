# NMR 👾

A `node_modules/` remover 

## Goal

Safely remove all `node_modules/` in a set of node projects somewhere inside of Francisco's computer (LOL)

## Usage

`python3 nmr.py <folder0> <folder1> ...`

where:

- `folderN` is a folder containing node projects (non node projects or node projects without `node_modules/` will be ignored)

## Some outputs

```
$ python3 nmr.py ~/Documents/github/
Allow nmr to delete the following folders? 
['/Users/XXXXX/Documents/github/XXXXX/node_modules/']
Type "yes" to confirm: yes- /Users/XXXXX/Documents/github/XXXXX/node_modules/: deleted
--> 1 node_modules deleted.
```
