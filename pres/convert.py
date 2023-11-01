import os

from PIL import Image

def gif_to_pngs(gif_path: str, save_dir: str = '.') -> None:
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)   
    im = Image.open(gif_path)
    path_end = os.path.basename(gif_path).split('.')[0]
    if not os.path.exists(os.path.join(save_dir, path_end)):
        os.makedirs(os.path.join(save_dir, path_end))
    i = 0
    while True:
        save_path = os.path.join(save_dir, path_end, f'{i}.png')
        if os.path.exists(save_path):
            break
        try:
            im.convert("RGBA")
            im.save(save_path)
            im.seek(im.tell()+1)
            i += 1
        except EOFError:
            break

import re
def update_frame_maxes() -> None:
    with open('pres.tex', 'r') as f:
        lines = f.readlines()
        newlines = []
        for line in lines:
            if 'animategraphics' in line:
                img_folder = re.findall(r'\\animategraphics.*{imgs/(.*)/}', line)
                total_frames = len(os.listdir(os.path.join('imgs', img_folder[0]))) - 1
                new_line = re.sub(r'\{0\}{\d+}', f'{{0}}{{{total_frames}}}', line)
                newlines.append(new_line)
            else:
                newlines.append(line)

    with open('pres.tex', 'w') as f:
        f.writelines(newlines)

def find_used_gif_names() -> list[str]:
    with open('pres.tex', 'r') as f:
        lines = f.readlines()
        figs = []
        for line in lines:
            if 'animategraphics' in line:
                img_folder = re.findall(r'\\animategraphics.*{imgs/(.*)/}', line)
                figs.append(f'{img_folder[0]}.gif')
    return figs



figs = find_used_gif_names()

homepath = '/Users/liamrobinson/Documents/PyLightCurves/docs/build/html/_images'
paths = [os.path.join(homepath, fig) for fig in figs]

for i,path in enumerate(paths):
    print(f'{i+1}/{len(paths)} Converting {path}')
    gif_to_pngs(path, 'imgs')
update_frame_maxes()
