#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    fill_cell()
    while wall_is_beneath()==False:
        move_down(1)
        fill_cell()
    while wall_is_on_the_right()==False:
        move_right(1)
        fill_cell()
    pass


if __name__ == '__main__':
    run_tasks()
