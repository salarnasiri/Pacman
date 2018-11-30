# -*- coding: utf-8 -*-

# python imports
from __future__ import division
import math

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection
from ks.commands import ECommandDirection
from gui_events import GuiEventType


class GuiHandler():

    def __init__(self, world, sides, canvas):

        self._world = world
        self._sides = sides
        self._canvas = canvas


    def initialize(self, config):

        self._angle = {
            EDirection.Up.name:        90,
            EDirection.Right.name:     0,
            EDirection.Down.name:      -90,
            EDirection.Left.name:      180,
        }
       
        self._config(config)
        self._draw_board()
        self._draw_players()


    def _config(self, config):

        # self._scale_factor = (self._canvas.width - config['statuses_width']) / (self._world.width * config['cell_size'])
        # self._scale_percent = math.ceil(self._scale_factor * 100)
        # self._cell_size = math.ceil(config['cell_size'] * self._scale_factor)
        # self._font_size = self._cell_size // 2
        self._cell_size = 150


    def _draw_board(self):

        for y in range(self._world.height):
            for x in range(self._world.width):
                cell = self._world.board[y][x]
                if cell == ECell.Wall and (y == self._world.height - 1 or y == 0 or x == self._world.width - 1 or x == 0):
                    self._canvas.create_image('RoundWall', x * self._cell_size, y * self._cell_size, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)

                elif cell == ECell.Wall:
                    self._canvas.create_image('InterWall', x * self._cell_size, y * self._cell_size, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)

                elif cell == ECell.Empty:
                    self._canvas.create_image('Empty', x * self._cell_size, y * self._cell_size, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)

                elif cell == ECell.Food:
                    img_ref = self._canvas.create_image('Food', x * self._cell_size, y * self._cell_size, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)

                elif cell == ECell.SuperFood:
                    self._canvas.create_image('SuperFood', x * self._cell_size, y * self._cell_size, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)


    def _draw_players(self):

        self._pacman_img_ref = self._canvas.create_image('Pacman', self._world.pacman.x * self._cell_size + self._cell_size/2, self._world.pacman.y * self._cell_size + self._cell_size/2, center_origin=True,
                                scale_type=ScaleType.ScaleToWidth,
                                scale_value=self._cell_size)


    def update(self, events):

        for event in events:
            if event != None:
                
                # move
                if event.type == GuiEventType.MovePacman:

                    pacman_pos = self._get_canvas_position(event.extra_properties["new_pos"][0], event.extra_properties["new_pos"][1])
                    self._canvas.edit_image(self._pacman_img_ref, pacman_pos['x'], pacman_pos['y'])

                # change direction
                if event.type == GuiEventType.ChangePacmanDirection:

                    pacman_dir = self._angle[event.payload["direction"]]
                    pacman_pos = self._get_canvas_position(self._world.pacman.x, self._world.pacman.y)    
                    self._canvas.edit_image(self._pacman_img_ref, pacman_pos['x'], pacman_pos['y'], angle=pacman_dir)


    def _get_canvas_position(self, x, y, center_origin=False):

        addition = self.cell_size // 2 if center_origin else 0
        return {
            'x': x * self.cell_size + addition,
            'y': y * self.cell_size + addition
        }
