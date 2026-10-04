"""Put rendered page PNGs side by side for viewing: python3 sheet.py out.png a.png b.png ..."""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
out, files = sys.argv[1], sys.argv[2:]
imgs = [mpimg.imread(f) for f in files]
h = max(i.shape[0] for i in imgs)
w = sum(i.shape[1] for i in imgs)
fig = plt.figure(figsize=(w / 100, h / 100), dpi=100)
x = 0
for im in imgs:
    ax = fig.add_axes([x / w, 0, im.shape[1] / w, im.shape[0] / h])
    ax.imshow(im)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_edgecolor('red')
    x += im.shape[1]
fig.savefig(out, dpi=100)
