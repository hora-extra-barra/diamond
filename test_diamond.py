from unittest import TestCase
import diamond

class TestDiamond(TestCase):

	def test_receive_A_and_return_A(self):
		returned = diamond.diamond('A')

		expected = 'A'

		self.assertEquals(returned, expected)

	def test_receive_B_and_return_a_diamond_with_A_and_B(self):
		returned = diamond.diamond('B')

		expected = ' A\nB B\n A'

		self.assertEquals(returned, expected)

	def test_receive_C_and_return_diamond_with_A_B_C(self):
		returned = diamond.diamond('C')

		expected = '  A\n B B\nC   C\n B B\n  A'

		self.assertEquals(returned, expected)

	def test_receive_D_and_return_a_diamond_with_A_B_C_D(self):
		returned = diamond.diamond('D')

		expected = '   A\n  B B\n C   C\nD     D\n C   C\n  B B\n   A'

		self.assertEquals(returned, expected)

