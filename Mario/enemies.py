from living_things import Enemy


class EvilMushroom(Enemy):
    pass


class TurtleDuck(Enemy):
    INITIAL_HEALTH = 2


class FlyingTurtleDuck(TurtleDuck):
    INITIAL_HEALTH = 1


class TurtleDragon(Enemy):
    INITIAL_HEALTH = 10


class EvilFlower(Enemy):
    pass
