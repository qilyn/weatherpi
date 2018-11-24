from abc import ABC


class Renderer(ABC):
    """
    Renderers are responsible for boring things like frame rate.
    """

    @abstractmethod
    def draw(self):
        """
        Given a renderer which has been set up in some way, draw the requested Frame on its Surface.
        :return:
        """


class Surface(ABC):
    """
    A Surface is the type of output that can be drawn on. It is used by Renderers to draw Frames.
    Rendering on a SenseHat is easy because it's only ever an 8x8 grid.
    """


class Frame(ABC):
    """
    A Frame is an abstract means of representing some drawable information.
    """
    DIMENSIONS = 8

    def __init__(self, grid):
        self._frame = grid

    @classmethod
    def get_grid(cls):
        return Frame([[None] * cls.DIMENSIONS] * cls.DIMENSIONS)

    def get_pixel(self, x, y):
        return self._frame[y][x]

    def set_pixel(self, x, y, colour):
        self._frame[y][x] = colour


def Colour:

    @classmethod
    def min(cls):
        return 0

    @classmethod
    def max(cls):
        return 255

    def decrease(self, percentage):
        assert 1 >= percentage > 0
        self._value = self._value * 0

    def increase(self, percentage):
        assert 1 >= percentage > 0
        self._value = self._value * (1 + percentage)


X = Colour.max()
O = Colour.min()


def Graphic:
    def __init__(self, shape):
        pass

    def get_axis(self):
        return self.axis

    def set_axis(self, x, y):
        self.axis = (x, y)


class Patterns:

    A = [
        [O, X, X, O],
        [X, O, O, X],
        [X, X, X, X],
        [X, O, O, X],
        [X, O, O, X],
    ]

    B = [
        [X, X, X, O],
        [X, O, O, X],
        [X, X, X, O],
        [X, O, O, X],
        [X, X, X, O]
    ]

    C = [
        [O, X, X, X],
        [X, O, O, O],
        [X, O, O, O],
        [X, O, O, O],
        [O, X, X, X],
    ]

    D = [
        [X, X, X, O],
        [X, O, O, X],
        [X, O, O, X],
        [X, O, O, X],
        [X, X, X, O]
    ]

    E = [
        [X, X, X, X],
        [X, O, O, O],
        [X, X, X, X],
        [X, O, O, O],
        [X, X, X, X],
    ]

    F = [
        [X, X, X, X],
        [X, O, O, O],
        [X, X, X, O],
        [X, O, O, O],
        [X, O, O, O],
    ]

    G = [
        [O, X, X, X],
        [X, O, O, O],
        [X, O, X, X],
        [X, O, O, X],
        [O, X, X, X],
    ]

    H = [
        [X, O, O, X],
        [X, O, O, X],
        [X, X, X, X],
        [X, O, O, X],
        [X, O, O, X],
    ]

    I = [
        [X, X, X],
        [O, X, O],
        [O, X, O],
        [O, X, O],
        [X, X, X],
    ]

    J = [
        [X, X, X, X],
        [O, O, X, O],
        [O, O, X, O],
        [X, O, X, O],
        [O, X, X, O],
    ]

    K = [
        [X, O, O, X],
        [X, O, X, O],
        [X, X, O, O],
        [X, O, X, O],
        [X, O, O, X],
    ]

    L = [
        [X, O, O, O],
        [X, O, O, O],
        [X, O, O, O],
        [X, O, O, O],
        [X, X, X, X],
    ]

    M = [
        [X, O, O, O, X],
        [X, X, O, X, X],
        [X, O, X, O, X],
        [X, O, O, O, X],
        [X, O, O, O, X],
    ]

    N = [
        [X, O, O, O, X],
        [X, X, O, O, X],
        [X, O, X, O, X],
        [X, O, O, X, X],
        [X, O, O, O, X]
    ]

    O = [
        [O, X, X, O],
        [X, O, O, X],
        [X, O, O, X],
        [X, O, O, X],
        [O, X, X, O],
    ]

    P = [
        [X, X, X, O],
        [X, O, O, X],
        [X, X, X, O],
        [X, O, O, O],
        [X, O, O, O]
    ]

    Q = [
        [O, X, X, X, O],
        [X, O, O, X, O],
        [X, O, X, X, X],
        [X, O, O, X, X],
        [O, X, X, O, X]
    ]

    R = [
        [X, X, X, O],
        [X, O, O, X],
        [X, X, X, O],
        [X, O, O, X],
        [X, O, O, X],
    ]

    S = [
        [O, X, X, X],
        [X, O, O, O],
        [O, X, X, O],
        [O, O, O, X],
        [X, X, X, O],
    ]

    T = [
        [X, X, X],
        [O, X, O],
        [O, X, O],
        [O, X, O],
        [O, X, O],
    ]

    U = [
        [X, O, X],
        [X, O, X],
        [X, O, X],
        [X, O, X],
        [X, X, X],
    ]

    V = [
        [X, O, X],
        [X, O, X],
        [X, O, X],
        [X, O, X],
        [O, X, O],
    ]

    W = [
        [X, O, O, O, X],
        [X, O, O, O, X],
        [X, O, X, O, X],
        [X, O, X, O, X],
        [O, X, O, X, O],
    ]

    X = [
        [X, O, X],
        [X, O, X],
        [O, X, O],
        [X, O, X],
        [X, O, X],
    ]

    Y = [
        [X, O, X],
        [X, O, X],
        [O, X, O],
        [O, X, O],
        [O, X, O],
    ]

    Z = [
        [X, X, X],
        [O, O, X],
        [O, X, O],
        [X, O, O],
        [X, X, X],
    ]

    ONE = [
        [X, X, O],
        [O, X, O],
        [O, X, O],
        [O, X, O],
        [X, X, X],
    ]

    TWO = [
        [X, X, X],
        [O, O, X],
        [X, X, X],
        [X, O, O],
        [X, X, X],
    ]

    THREE = [
        [X, X, X],
        [O, O, X],
        [X, X, X],
        [O, O, X],
        [X, X, X],
    ]

    FOUR = [
        [X, O, X],
        [X, O, X],
        [X, X, X],
        [O, O, X],
        [O, O, X],
    ]

    FIVE = [
        [X, X, X],
        [X, O, O],
        [X, X, X],
        [O, O, X],
        [X, X, X],
    ]

    SIX = [
        [X, X, X],
        [X, O, O],
        [X, X, X],
        [X, O, X],
        [X, X, X],
    ]

    SEVEN = [
        [X, X, X],
        [O, O, X],
        [O, X, O],
        [O, X, O],
        [O, X, O],
    ]

    EIGHT = [
        [X, X, X],
        [X, O, X],
        [X, X, X],
        [X, O, X],
        [X, X, X],
    ]

    NINE = [
        [X, X, X],
        [X, O, X],
        [X, X, X],
        [O, O, X],
        [O, O, X]
    ]

    ZERO = [
        [X, X, X],
        [X, O, X],
        [X, O, X],
        [X, O, X],
        [X, X, X],
    ]
