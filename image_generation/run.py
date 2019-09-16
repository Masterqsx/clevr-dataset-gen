import os

n = 1968
template = "blender --background --python render_images.py -- --use_gpu 1 --num_images %d --start_idx %d --split train  --max_retries 300 --save_blendfiles 1 --width 256 --height 256"
while n < 50000:
    n_images = min(50000 - n, 100)
    os.system(template % (n_images, n))
    n = n + n_images
