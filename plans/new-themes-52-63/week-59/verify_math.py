"""Independent support-function audit for the Week 59 research geometry.

An exact candidate-extremum calculation on the three arcs, rather than a
polygonal approximation, checks a finite orientation sample. The universal
width claim is proved geometrically in research.md, not by this sample.
"""
import json
from math import cos, sin, pi, sqrt, hypot
from pathlib import Path


def dot(p, u):
    return p[0] * u[0] + p[1] * u[1]


def support(vertices, w, u):
    candidates = list(vertices)
    # A linear maximum on a circular arc is at an endpoint or at center+w*u.
    # Keep a radial candidate only if it belongs to all three closed disks.
    for c in vertices:
        p = (c[0] + w * u[0], c[1] + w * u[1])
        if all(hypot(p[0] - d[0], p[1] - d[1]) <= w + 1e-9 for d in vertices):
            candidates.append(p)
    return max(dot(p, u) for p in candidates)


def audit():
    w = 60.0
    h = sqrt(3) * w / 2
    vertices = [(0.0, 0.0), (w, 0.0), (w / 2, h)]
    centroid = (w / 2, h / 3)
    assert all(abs(hypot(vertices[i][0] - vertices[j][0], vertices[i][1] - vertices[j][1]) - w) < 1e-9
               for i, j in [(0, 1), (1, 2), (2, 0)])
    widths, heights = [], []
    for k in range(1440):
        theta = 2 * pi * k / 1440
        u = (cos(theta), sin(theta))
        widths.append(support(vertices, w, u) + support(vertices, w, (-u[0], -u[1])))
        # Height of the centroid above the support line whose upward normal is u.
        heights.append(dot(centroid, u) + support(vertices, w, (-u[0], -u[1])))
    assert max(abs(x - w) for x in widths) < 1e-8
    assert abs(min(heights) - (w - w / sqrt(3))) < 1e-8
    assert abs(max(heights) - w / sqrt(3)) < 1e-8
    ellipse = [2 * sqrt(30 ** 2 * cos(2 * pi * k / 1440) ** 2 +
                        20 ** 2 * sin(2 * pi * k / 1440) ** 2) for k in range(1440)]
    assert abs(min(ellipse) - 40) < 1e-9 and abs(max(ellipse) - 60) < 1e-9
    triangle_widths = []
    for k in range(1440):
        u = (cos(2 * pi * k / 1440), sin(2 * pi * k / 1440))
        ps = [dot(v, u) for v in vertices]
        triangle_widths.append(max(ps) - min(ps))
    assert abs(min(triangle_widths) - h) < 1e-9
    assert abs(max(triangle_widths) - w) < 1e-9
    arc_angle = pi / 3
    perimeter = 3 * w * arc_angle
    assert abs(perimeter - pi * w) < 1e-9
    return {
        "scope": "Analytic arc-extremum calculation at finite directions; see research.md for universal proof.",
        "orientation_samples": 1440,
        "equilateral_side_and_reuleaux_width_mm": w,
        "reuleaux_width_min_max_mm": [min(widths), max(widths)],
        "max_width_error_mm": max(abs(x - w) for x in widths),
        "ellipse_full_axes_mm": [60, 40],
        "ellipse_width_min_max_mm": [min(ellipse), max(ellipse)],
        "equilateral_triangle_width_min_max_mm": [min(triangle_widths), max(triangle_widths)],
        "centroid_height_above_floor_min_max_mm": [min(heights), max(heights)],
        "centroid_radial_vertex_mm": w / sqrt(3),
        "centroid_radial_opposite_arc_midpoint_mm": w - w / sqrt(3),
        "circle_diameter_60_perimeter_mm": pi * w,
        "reuleaux_three_60_degree_arcs_perimeter_mm": perimeter,
        "physical_pretest": "unperformed",
    }


if __name__ == "__main__":
    result = audit()
    out = Path(__file__).with_name("math-checks.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
