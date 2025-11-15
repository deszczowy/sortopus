# The Sortopus: Unstoppable photos sorting machine!
<img align="right" src="src/gfx/octo.png" width="150"> version 0.03

The weapon of choice for everyone who is flooded with photos. Gather all files, configure the tool, then make yourself comfortable and just sort it out. It is early version, so go easy on me. It works, that's important! Application will present You all your pictures, one by one, each with options to leave it where it is, delete it, or move into one of two optional directories.

## Configuration

Create a config file named `config.json` next to `sortopus.py` and fill it before running application with data shown below. It is very early version, remember? All paths should be absolute.

```
{
  "main_dir": "/main/photo/search/directory",
  "deleted_dir": "/directory/to/store/deleted/files",
  "actions": [
    { "dir": "/first/custom/move/directory", "label": "First Custom Action Button Label" },
    { "dir": "/second/custom/move/directory", "label": "Second Custom Action Button Label" }
  ]
}
```

`main_dir` - this is the root path to all your photos directory. Searching is recursive, so do not worry. 

`deleted_dir` - You don't want to literaly remove those photos from disk, aren't You? "Deleting" will move files into directory given in this parameter.

### Rest is optional

Define `actions` list if You want other options for moving files. Every `actions` element is an object with path to move photos (`dir`) and a label (`label`) for custom button.

## How it works

Program will read root path recursively looking for `*.jpg` files. All necessary data will be stored into `list.txt` file in root folder. On startup You will start with first unsorted photo. If You want to restart all process just remove `list.txt` from root directory. Restarting will not restore moved photos - what is done, is done.

## Shortcuts

`Q` for leave photo where it is

`1`, `2`, `3` for moving photo into one of configured places

`Delete` sounds selfexplanatory

`Left arrow` and `Right arrow` swithes to previous or next photo

## How to run

Download source code, configure, and type command

`python sortopus.py`

That is it.

## Plans?

Plenty, but unscheduled!
