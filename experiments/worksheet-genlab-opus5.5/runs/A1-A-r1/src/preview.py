import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from tri import *


def show(ax, region, title='', pieces=None, holes=()):
    for t in region:
        pts = [cart(v) for v in verts(t)]
        ax.add_patch(Polygon(pts, closed=True, fc='white', ec='0.7', lw=0.5))
    for t in holes:
        pts = [cart(v) for v in verts(t)]
        ax.add_patch(Polygon(pts, closed=True, fc='0.5', ec='0.7', lw=0.5))
    for e in boundary_edges(frozenset(region) | frozenset(holes)):
        a, b = [cart(v) for v in e]
        ax.plot([a[0], b[0]], [a[1], b[1]], 'k-', lw=1.5)
    if pieces:
        cols = {'G': 'green', 'B': 'royalblue', 'R': 'red', 'Y': 'gold', 'P': 'purple'}
        for name, s in pieces:
            for t in s:
                pts = [cart(v) for v in verts(t)]
                ax.add_patch(Polygon(pts, closed=True, fc=cols[name], alpha=0.4, ec='none'))
            for e in boundary_edges(s):
                a, b = [cart(v) for v in e]
                ax.plot([a[0], b[0]], [a[1], b[1]], 'k-', lw=1)
    for t in region:
        c = centroid(t)
    ax.set_aspect('equal')
    ax.autoscale()
    ax.set_title(title, fontsize=8)
    ax.axis('off')


def grid(items, fname, cols=3):
    rows = (len(items) + cols - 1) // cols
    fig, axs = plt.subplots(rows, cols, figsize=(4 * cols, 3.5 * rows))
    axs = axs.flatten() if hasattr(axs, 'flatten') else [axs]
    for ax, it in zip(axs, items):
        show(ax, **it)
    for ax in axs[len(items):]:
        ax.axis('off')
    fig.tight_layout()
    fig.savefig(fname, dpi=60)
