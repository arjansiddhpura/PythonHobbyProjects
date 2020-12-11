"""
Rounded rectangles in antialiased varieties.
"""

import pygame as pg

from pygame import gfxdraw

def aa_round_rect(surface, rect, color, rad=20, border=0, inside=(0,0,0)):
    """
    Draw an antialiased rounded rect on the target surface.  Alpha is not
    supported in this implementation but other than that usage is identical to
    round_rect.
    """
    rect = pg.Rect(rect)
    _aa_render_region(surface, rect, color, rad)
    if border:
        rect.inflate_ip(-2*border, -2*border)
        _aa_render_region(surface, rect, inside, rad)


def _aa_render_region(image, rect, color, rad):
    """Helper function for aa_round_rect."""
    corners = rect.inflate(-2*rad-1, -2*rad-1)
    for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
        x, y = getattr(corners, attribute)
        gfxdraw.aacircle(image, x, y, rad, color)
        gfxdraw.filled_circle(image, x, y, rad, color)
    image.fill(color, rect.inflate(-2*rad,0))
    image.fill(color, rect.inflate(0,-2*rad))