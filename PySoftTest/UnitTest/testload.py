import unittest

suit = unittest.defaultTestLoader.discover("case", '*.py')

unittest.TextTestRunner().run(suit)
