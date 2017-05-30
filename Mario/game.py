from living_things import Hero, HeroBall
from inanimate_things import Building, Pipe
from enemies import EvilMushroom, TurtleDragon, TurtleDuck, FlyingTurtleDuck


def play_hero_enemy_creation():
    mario = Hero()
    print(mario)
    assert mario.health == 1

    em1 = EvilMushroom()
    assert em1.health == 1

    tdr1 = TurtleDragon()
    print(tdr1)
    assert tdr1.health == 10

    td1 = TurtleDuck()
    assert td1.health == 2

    ftd1 = FlyingTurtleDuck()
    assert ftd1.health == 1


def play_hero_emit_heroball():
    luigi = Hero()

    heroball = luigi.fire_heroball('right')
    assert heroball is None

    luigi.levelup()
    luigi.levelup()
    assert luigi.health == 3

    heroball = luigi.fire_heroball('right')
    assert heroball.health == 1


def play_hero_interacts_with_enemy():
    mario = Hero()

    em1 = EvilMushroom()
    em2 = EvilMushroom()

    mario.contacts_with(em1, 'right')
    assert mario.health == 0
    assert em1.health == 1

    luigi = Hero()

    luigi.contacts_with(em1, 'bottom')
    assert luigi.health == 1
    assert em1.health == 0

    luigi.levelup()
    assert luigi.health == 2

    luigi.contacts_with(em2, 'right')
    assert luigi.health == 1
    assert em2.health == 1


def play_hero_fires_heroball_to_enemy():
    mario = Hero()
    mario.levelup()
    mario.levelup()

    em1 = EvilMushroom()

    heroball = mario.fire_heroball('right')
    heroball.contacts_with(em1, 'right')
    assert heroball.health == 0
    assert em1.health == 0

def play_hero_turtuldragon():
    mario = Hero()
    mario.levelup()
    mario.levelup()

    tdr = TurtleDragon()

    heroball = mario.fire_heroball('right')
    heroball.contacts_with(tdr, 'right')
    assert heroball.health == 0
    assert tdr.health == 9


def play_hero_eats_powerup():
    pass
    # build1 = Building()
    # heroball = mario.fire_heroball('right')
    # heroball.contacts_with(build1, 'right')
    # assert heroball.health == 0
    #
    # pipe1 = Pipe()
    # heroball = mario.fire_heroball('left')
    # heroball.contacts_with(pipe1, 'left')
    # assert heroball.health == 0

def main():
    play_hero_enemy_creation()
    play_hero_emit_heroball()
    play_hero_interacts_with_enemy()
    play_hero_fires_heroball_to_enemy()
    play_hero_turtuldragon()




if __name__ == '__main__':
    main()
