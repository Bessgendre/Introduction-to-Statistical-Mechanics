import os
files = os.listdir('./')
del_suffix = ['toc', 'vrb', 'aux', 'log', 'nav', 'out', 'snm', 'synctex.gz','bbl','blg']
for file in files:
    for suffix in del_suffix:
        if file.endswith(suffix):
            os.remove(file)