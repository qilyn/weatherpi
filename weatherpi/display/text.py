from .base import Renderer


class TextRenderer(Renderer):

    def __init__(self, dimensions):
        """
        Create yourself a beautiful wee square text-based renderer.
        :param dimensions: Integer.
        """
        assert isinstance(int, dimensions)
        self.dimensions = dimensions

    def draw(self):
        grid = [
            ['']
        ]