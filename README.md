# backend

how to run in CLI

to run tadao.py: 
```cli
python tadao.py -i maze_metadata.json -o tadao.txt
```

to run top.py: 
```cli
python top.py -i maze_metadata.json -o top.txt
```

to run maze_updater.py
```cli
python maze_updater.py -i tadao.txt -i top.txt -o maze_metadata.json
```

If you are not provide the "-i" or "-o", the error will occour

After run, the file maze_render.json will be created (if not existed) or updated. This is an array of all step position of bot to get the coin
