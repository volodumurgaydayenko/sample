class GameObject:
    pass


class LivingThing(GameObject):
    INITIAL_HEALTH = 1  # початкове життя
    DAMAGE = 1  # урон

    def __init__(self):
        self.health = self.INITIAL_HEALTH

    def __repr__(self):
        return '{0}: health={1}'.format(self.__class__.__name__, self.health)

    def contacts_with(self, obj, direction):
        return NotImplemented

    def reduce_health(self, damage):  # функція зменшення життя для обєкта
        self.health -= damage


class InanimateThing(GameObject):
    pass
