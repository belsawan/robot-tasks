#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
  def krestlevo():
        move_right(1)
        fill_cell()
        move_right(1)
        fill_cell()
        move_up(1)
        fill_cell()
        move_down(2)
        fill_cell()
        move_up(1)
        move_right(1)
        fill_cell()
  def krestpravo():
        move_left(1)
        fill_cell()
        move_left(1)
        fill_cell()
        move_up(1)
        fill_cell()
        move_down(2)
        fill_cell()
        move_up(1)
        move_left(1)
        fill_cell()
  move_down(1)
  for j in range (10):
      if j%2==0:
          fill_cell()
          move_right(1)
          fill_cell()
          move_up(1)
          fill_cell()
          move_down(2)
          fill_cell()
          move_up(1)
          move_right(1)
          fill_cell()
          move_right(1)
          for i in range(8):
             krestlevo()
             move_right(1)
          move_right(1)
          fill_cell()
          move_right(1)
          fill_cell()
          move_up(1)
          fill_cell()
          move_down(2)
          fill_cell()
          move_up(1)
          move_right(1)
          fill_cell()
      else:
          fill_cell()
          move_left(1)
          fill_cell()
          move_up(1)
          fill_cell()
          move_down(2)
          fill_cell()
          move_up(1)
          move_left(1)
          fill_cell()
          move_left(1)
          for i in range(8):
            krestpravo()
            move_left(1)
          move_left(1)
          fill_cell()
          move_left(1)
          fill_cell()
          move_up(1)
          fill_cell()
          move_down(2)
          fill_cell()
          move_up(1)
          move_left(1)
          fill_cell()
          for z in range(4):
            if wall_is_beneath()==False:
              move_down(1)
  move_up(2)


if __name__ == '__main__':
    run_tasks()
