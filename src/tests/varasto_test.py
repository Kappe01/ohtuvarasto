import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_nollatun_tilavuuden(self):
        varasto = Varasto(-2)
        self.assertEqual(varasto.tilavuus, 0)
    
    def test_konstruktori_luo_nollatun_varaston(self):
        varasto = Varasto(-2, alku_saldo=-2)
        self.assertEqual(varasto.saldo, 0)

    def test_lisaa_varastoon_liikaa(self):
        self.varasto.lisaa_varastoon(9999999999999)
        self.assertEqual(self.varasto.tilavuus, 10)

    def test_lisaa_varastoon_neg_maaran(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.tilavuus, 10)
    
    def test_ota_varastosta_neg(self):
        self.assertEqual(self.varasto.ota_varastosta(-1),0)
    
    def test_ota_varastosta_liikaa(self):
        self.varasto.lisaa_varastoon(10)
        self.assertEqual(self.varasto.saldo, 10)
        self.assertEqual(self.varasto.ota_varastosta(9999999), 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_str(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")
