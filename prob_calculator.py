from random import randint
import copy
class Hat:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self._contents = []
        self._drawn = []
        self._values = [v for v in self.__dict__.values()][:-2]
        self._keys = [k for k in self.__dict__.keys()][:-3]

        for i in range(len(self._keys)):
            for j in range(int(self._values[i])):
                self._contents.append(self._keys[i])

    def draw(self, balls):
        contents = copy.deepcopy(self._contents)
        self._drawn = []
        drwanstring = ''

        if len(contents) > balls:
            for n in range(balls):
                myball = contents.pop(randint(0, len(contents)-1))
                self._drawn.append(myball)
                drwanstring += myball
        else: drwanstring = ''.join(contents)
        return drwanstring

    @property
    def drawn(self):
        return self._drawn

    def __str__(self):
        return '{} balls'.format(self._contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    mylist = []
    matched = 0
    num = num_experiments
    while num != 0:
        for k, v in expected_balls.items():
            for n in range(int(v)):
                mylist.append(k)

        hat.draw(num_balls_drawn)
        drawnlist = hat.drawn

        for item in drawnlist:
            for elem in mylist:
                if elem is item:
                    mylist.remove(elem)
                    drawnlist.remove(item)
        if len(mylist) == 0:
            matched +=1
        # print(drawnlist, " ===> ", mylist, matched)
        num -= 1
        mylist = []
    return matched/num_experiments

def main():
    hat1 = Hat(yellow=3, blue=2, green=6, black=1)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    print(f'The first hat contains -> {hat1} \nThe Second hat contains -> {hat2} \nThe Third hat contains -> {hat3}')
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat, expected_balls={"red": 2, "green": 1}, num_balls_drawn=5, num_experiments=5000)
    print(probability)

if __name__=='__main__':
    main()

