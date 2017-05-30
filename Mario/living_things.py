from game_objects import LivingThing


class PowerUp(LivingThing):
    pass


class Hero(LivingThing):
    MAXIMUM_HEALTH = 3
    ALLOW_HEROBALL_HEALTH = 3
    INCREMENT_HEALTH_ON_LEVELUP = 1

    def fire_heroball(self, direction):
        if self.health == self.ALLOW_HEROBALL_HEALTH:
            heroball = HeroBall()
        else:
            heroball = None
        return heroball

    def levelup(self):
        if self.health < self.MAXIMUM_HEALTH:
            self.health += self.INCREMENT_HEALTH_ON_LEVELUP

    def contacts_with(self, obj, direction):  # obj = em1 # direction = 'right'
        if isinstance(obj, Enemy):
            if direction in ['right', 'left', 'top']:
                self.reduce_health(obj.DAMAGE)
            else:
                obj.reduce_health(self.DAMAGE)

    def reduce_health(self, damage):
        super().reduce_health(damage)
        if self.health <= 0:
            print('GAME OVER!!!')


class Enemy(LivingThing):
    pass


class Projectile(LivingThing):
    REDUCES_HEALTH_TO = None

    def contacts_with(self, obj, direction):
        if isinstance(obj, self.REDUCES_HEALTH_TO):
            obj.reduce_health(self.DAMAGE)
            self.reduce_health(self.health)


class HeroBall(Projectile):
    REDUCES_HEALTH_TO = Enemy


class FireBall(Projectile):
    REDUCES_HEALTH_TO = Hero
