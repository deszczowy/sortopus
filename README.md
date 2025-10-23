# The Octosort: Unstoppable photos sorting machine!
<img align="right" src="src/gfx/oct.png"> The weapon of choice for everyone who is flooded with photos. Gather all files, configure the tool, then make yourself confortable and just sort it out. It is version 0.01, so go easy on me. It works, that's important! Application will present You all your pictures, one by one, each with options to leave it where it is, delete it, or move into one of two optional directories.

## Configuration

Create a config file named `config.json` next to `sortopus.py` and fill it before running application with data shown below. It is version 0.01, remember? All paths chould be absolute.

```
{
  "main_dir": "/main/photo/search/directory",
  "deleted_dir": "/directory/to/store/deleted/files",
  "defer1_dir": "/first/custom/move/directory",
  "defer1_label": "First Custom Action Button Label",
  "defer2_dir": "/second/custom/move/directory",
  "defer2_label": "Second Custom Action Button Label"
}
```

`main_dir` - this is the root path to all your photos directory. Searching is recursive, so do not worry. 

`deleted_dir` - You don't want to literaly remove those photos from dist, aren't You? "Deleting" will move files into diroctory given in this parameter.

### Rest is optional

Define `defer1_dir` and `defer2_dir` if You want others options for moving files. For example create directory for Portraits or Landscapes, put the words "Portrait" and "Landscape" into `defer1_label` and `defer2_label` fields respectively and You will get two labeled buttons! Now You can leave a photo, move to portraits, move to landscapes or delete!

## How it works

Program will read root path recursively looking for `*jpg` files. All necessary data will be stored into `list.txt` file in root folder. On startup You will start with first unsorted photo. If You want to restart all process just remove `list.txt` from root directory. Restarting will not restore moved photos - what is done, is done.

## How to run

Download source code, configure, and type

`python sortopus.py`

That is it.

## Plans?

Plenty, but unscheduled!
