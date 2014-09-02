from unittest import TestCase
import diamond

class TestDiamond(TestCase):
	
	def test_recebe_A_e_retorna_A(self):
		returned = diamond.diamond('A')

		expected = 'A'

		self.assertEquals(returned, expected)
	
	def test_recebe_B_e_retorna_um_diamante_com_A_e_B(self):
		returned = diamond.diamond('B')

		expected = ' A\nB B\n A'

		self.assertEquals(returned, expected)

	def test_recebe_C_e_retorna_diamante_com_A_B_C(self):
		returned = diamond.diamond('C')
		expected = '  A\n B B\nC   C\n B B\n  A'

		self.assertEquals(returned, expected)

	def test_recebe_D_e_retorna_diamante_com_A_B_C_D(self):
		returned = diamond.diamond('D')
		expected = '   A\n  B B\n C   C\nD     D\n C   C\n  B B\n   A'

		self.assertEquals(returned, expected)

