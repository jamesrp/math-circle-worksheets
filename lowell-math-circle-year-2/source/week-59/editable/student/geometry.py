"""Original millimetre geometry for Week 59; all pictures use equal x/y units."""
import math

H = 30 * math.sqrt(3)
VERTICES = ((0, 0), (60, 0), (30, H))
ARCS = ((0, 0, 0, 60), (60, 0, 120, 180), (30, H, 240, 300))


def transform(point, cx, cy, scale=1, angle=0, w=60):
    """Place the underlying equilateral centroid at (cx,cy)."""
    x = (point[0] - w / 2) * scale
    y = (point[1] - w * math.sqrt(3) / 6) * scale
    a = math.radians(angle)
    return (cx + x * math.cos(a) - y * math.sin(a),
            cy + x * math.sin(a) + y * math.cos(a))


def vertices(w=60):
    return ((0, 0), (w, 0), (w / 2, w * math.sqrt(3) / 2))


def arcs(w=60):
    return ((0, 0, 0, 60), (w, 0, 120, 180),
            (w / 2, w * math.sqrt(3) / 2, 240, 300))
