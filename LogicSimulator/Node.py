
class Node(object):

    def __init__(self):
        self._state = False
        self._listeners = set()

    def notify_listeners(self):
        pass

    