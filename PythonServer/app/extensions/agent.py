# -*- coding: utf-8 -*-

# project imports
from ..ks.models import EDirection, ECell

def get_position(self):
    return (self.x, self.y)


def calculate_new_position(self):

    self._convert_dir_to_pos = {
        EDirection.Up.name: (0, -1),
        EDirection.Down.name: (0, +1),
        EDirection.Right.name: (+1, 0),
        EDirection.Left.name: (-1, 0)
    }

    return(self._convert_dir_to_pos[self.direction.name][0] + self.x,
           self._convert_dir_to_pos[self.direction.name][1] + self.y)


def can_move(self, world, position):
    return world.board[(position[1])][(position[0])] != ECell.Wall


def recover(self):
    self.x = self.init_x
    self.y = self.init_y
    self.direction = self.init_direction
