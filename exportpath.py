import os

root_dir = '/'

paths = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    paths.append(dirpath)

with open(os.path.expanduser('~/.zshrc'), 'w') as f:
    for path in paths:
        f.write(f'export PATH="{path}:$PATH"\n')

print("Tüm yollar .zshrc dosyasına eklendi.")
