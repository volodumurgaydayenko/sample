from game_objects import InanimateThing


class Coin(InanimateThing):
    pass


class Building(InanimateThing):
    pass


class Flag(InanimateThing):
    pass


class Pipe(InanimateThing):
    pass


class Pit(InanimateThing):
    pass


class Block(InanimateThing):
    pass


class EmptyBlock(Block):
    pass


class CoinBlock(Block):
    pass


class PowerupBlock(Block):
    pass
