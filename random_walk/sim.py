from random_walk.drunk import Drunk, UsualDrunk, ColdDrunk, EWDrunk
from random_walk.field import Field
from random_walk.location import Location
from random_walk.funcs import cv


def walk(f: Field, d: Drunk, num_steps: int):
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))


def sim_walks(num_steps: int, num_trials: int, d_class):
    """
    :param num_steps: assumed int >= 0
    :param num_trials: assumed int > 0
    :param d_class: assumed a subclass of Drunk
    """
    Homer = d_class('Homer')
    origin = Location(0.0, 0.0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(Homer, origin)
        distances.append(walk(f, Homer, num_steps))
    return distances


def drunk_test(walk_lengths, num_trials, d_class):
    for num_steps in walk_lengths:
        distances = sim_walks(num_steps, num_trials, d_class)
        print(d_class.__name__, 'random walk of', num_steps, 'steps')
        print(' Mean = ', sum(distances) / len(distances), ' CV = ', cv(distances))
        print(' Max =', max(distances), 'Min =', min(distances))
        print('')


def sim_all(drunk_kinds, walk_lengths, num_trials):
    for d_class in drunk_kinds:
        drunk_test(walk_lengths, num_trials, d_class)


sim_all((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)
