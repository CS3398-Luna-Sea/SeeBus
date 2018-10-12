import time


class Tracker:
    def __init__(self):
        print('Tracker.__init__')
        self.value = 0

    def update_value(self):
        time.sleep(3)
        self.value += 1
        print('Value set to {}'.format(self.value))

    def get_value(self):
        return self.value


class Displayer:
    def __init__(self):
        print('Displayer.__init__')
        self.tracker = Tracker()
        print(self.tracker.update_value())

    def run(self):
        while True:
            self.tracker.update_value()
            print(self.tracker.get_value())


if __name__ == '__main__':
    d = Displayer()
    d.run()
