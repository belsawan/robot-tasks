#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    i=0
    j=0
    while wall_is_on_the_right()==False:
        move_right(1)
        i=i+1
    while wall_is_on_the_left()==False:
        move_left(1)
    while wall_is_beneath()==False:
        move_down(1)
        j=j+1
    while wall_is_above()==False:
        move_up(1)
    move_down(1)
    for a in range (j-1):
       if a%2==0:
         for b in range (1,i):
          move_right(1)
          fill_cell()
       else:
           for b in range (1,i):
             move_left(1)
             if wall_is_on_the_left()==False:
               fill_cell()
       move_down(1)
       if wall_is_on_the_left()==False:
               fill_cell()
    move_right(1)
    pass


if __name__ == '__main__':
    run_tasks()
