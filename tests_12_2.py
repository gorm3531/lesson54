import test
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = list()

    def setUp(self):
        self.run1 = test.Runner('Усэйн', 10)
        self.run2 = test.Runner('Андрей', 9)
        self.run3 = test.Runner('Ник', 3)

    def test_tournament1(self):
        tournament_1 = test.Tournament(90, self.run1, self.run3)
        TournamentTest.all_results.append(tournament_1.start())
        self.assertTrue(TournamentTest.all_results[-1][2] == self.run3)

    def test_tournament2(self):
        tournament_2 = test.Tournament(90, self.run2, self.run3)
        TournamentTest.all_results.append(tournament_2.start())
        self.assertTrue(TournamentTest.all_results[-1][2] == self.run3)

    def test_tournament3(self):
        tournament_3 = test.Tournament(90, self.run1, self.run2, self.run3)
        TournamentTest.all_results.append(tournament_3.start())
        self.assertTrue(TournamentTest.all_results[-1][3] == self.run3)




    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    if __name__ == "__main__":
        unittest.main()