import os

from PIL import Image

def gif_to_pngs(gif_path: str, save_dir: str = '.') -> None:
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)   
    im = Image.open(gif_path)
    path_end = os.path.basename(gif_path).split('.')[0]
    if not os.path.exists(os.path.join(save_dir, path_end[:-4])):
        os.makedirs(os.path.join(save_dir, path_end[:-4]))
    i = 0
    while True:
        save_path = os.path.join(save_dir, path_end[:-4], f'{i}.png')
        if os.path.exists(save_path):
            break
        try:
            im.convert("RGBA")
            im.save(save_path)
            im.seek(im.tell()+1)
            i += 1
        except EOFError:
            break

homepath = '/Users/liamrobinson/Documents/PyLightCurves/docs/build/html/_images'
figs = ['sphx_glr_plot_earth_001.gif',
        'sphx_glr_vis_attitude_motion_001.gif']
paths = [os.path.join(homepath, fig) for fig in figs]

for i,path in enumerate(paths):
    print(f'{i+1}/{len(paths)} Converting {path}')
    gif_to_pngs(path, 'imgs')