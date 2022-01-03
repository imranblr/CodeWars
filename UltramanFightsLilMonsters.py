from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """战者"""

    # Use __slots__ magic to limit the member variables


    __slots__ = ('_name', '_hp')


    def __init__(self, name, hp):
        """initialization method

       :param name: name
       :param hp: life value
       """


        self._name = name
        self._hp = hp


    @property
    def name(self):
        return self._name


    @property
    def hp(self):
        return self._hp


    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0


    @property
    def alive(self):
        return self._hp > 0


    @abstractmethod
    def attack(self, other):
        """ attack

       :param other: the object being attacked
       """


        pass


class Ultraman(Fighter):
    """Ultraman"""


    __slots__ = ('_name', '_hp', '_mp')


    def __init__(self, name, hp, mp):
        """initialization method

       :param name: name
       : param hp: life value
       : param mp: magic value
       """


        super().__init__(name, hp)
        self._mp = mp


    def attack(self, other):
        other.hp -= randint(15, 25)


    def huge_attack(self, other):
        """ Ultimate nirvana (kill at least 50 points or three-quarters of the opponent's blood)

       :param other: the object being attacked

       :return: If successful, return True otherwise return False
       """


        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False


    def magic_attack(self, others):
        """Magic attack

       :param others: the group being attacked

       :return: Use magic to successfully return True otherwise return False
       """


        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False


    def resume(self):
        """Restore magic value"""


        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point


    def __str__(self):
        return '~~~%s Ultraman~~~ \n ' % self._name + \
               'Health: %d \n ' % self._hp + \
               'Magic value: %d \ n ' % self._mp


class Monster(Fighter):
    """Little Monster"""


    __slots__ = ('_name', '_hp')


    def attack(self, other):
        other.hp -= randint(10, 20)


    def __str__(self):
        return '~~~%s Little Monster~~~ \n ' % self._name + \
               'Health: %d \n ' % self._hp


def is_any_alive(monsters):
    """ Determine if there are any monsters alive"""


    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """Select a small living monster"""


    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """Display information about Ultraman and little monsters"""


    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('Luo Hao', 1000, 120)
    m1 = Monster('Di Renjie', 250)
    m2 = Monster('Bai Yuanfang', 500)
    m3 = Monster('Lil Fen', 750)
    ms = [m1, m2, m3]
    fight_round = 1


    while u.alive and is_any_alive(ms):
        print('======== Round %02d ========' % fight_round)
        m = select_alive_one(ms)  # Select a little monster
        skill = randint(1, 10)  # Choose which skill to use by random numbers
        if skill <= 6:  # 60% probability of using normal attack
            print('%s used normal attack to hit %s.' % (u.name, m.name))
            u.attack(m)
            print('%s mana restored % d points.' % (u.name, u.resume()))
        elif skill <= 9:  # 30% probability of using magic attack (possibly failed due to lack of mana)
            if u.magic_attack(ms):
                print('%s uses a magic attack.' % u.name)
            else:
                print('%s to use magic failed.' % u.name)
        else:  # 10% probability of using the ultimate special move (if the mana is insufficient, use a normal attack)
            if u.huge_attack(m):
                print('%s abused %s with the ultimate  attack . ' % (u.name, m.name))
            else:
                print('%s used a normal attack to hit %s.' % (u.name, m.name))
                print('%s mana was restored %s d point.'  % ( u. name , u . resume ()))
        if m.alive > 0:  # If the selected little monster is not dead, hit back Ultraman
            print('%s hit back %s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # Display information about Ultraman and little monsters after each round
        fight_round += 1
    print ( ' \n ========The battle is over!= =======  \n' )
    if u.alive > 0:
        print('%s Ultraman  wins!' % u.name)
    else:
        print('Little monster wins!')

if __name__ == "__main__":
    main()