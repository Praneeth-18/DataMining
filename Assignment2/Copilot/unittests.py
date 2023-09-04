# write unit tests using only numbers for Dijsktras_Algorithm.py

import unittest
from Dijkstras_Algorithm import Graph

class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        g = Graph(9)
        g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                   [4, 0, 8, 0, 0, 0, 0, 11, 0],
                   [0, 8, 0, 7, 0, 4, 0, 0, 2],
                   [0, 0, 7, 0, 9, 14, 0, 0, 0],
                   [0, 0, 0, 9, 0, 10, 0, 0, 0],
                   [0, 0, 4, 14, 10, 0, 2, 0, 0],
                   [0, 0, 0, 0, 0, 2, 0, 1, 6],
                   [8, 11, 0, 0, 0, 0, 1, 0, 7],
                   [0, 0, 2, 0, 0, 0, 6, 7, 0]]
        self.assertEqual(g.dijkstra(0), 0)
        self.assertEqual(g.dijkstra(1), 4)
        self.assertEqual(g.dijkstra(2), 12)
        self.assertEqual(g.dijkstra(3), 19)
        self.assertEqual(g.dijkstra(4), 21)
        self.assertEqual(g.dijkstra(5), 11)
        self.assertEqual(g.dijkstra(6), 9)
        self.assertEqual(g.dijkstra(7), 8)
        self.assertEqual(g.dijkstra(8), 14)

if __name__ == '__main__':
    unittest.main()

    