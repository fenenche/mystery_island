import unittest

from game import (
    create_player,
    move_to_jungle,
    move_to_cave,
    cross_bridge,
    restore_lighthouse,
    check_energy
)


class TestMysteryIsland(unittest.TestCase):

    def test_create_player(self):
        player = create_player("Favour")

        self.assertEqual(player["name"], "Favour")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["inventory"], [])
        self.assertFalse(player["game_over"])
        self.assertFalse(player["won"])

    def test_move_to_jungle(self):
        player = create_player("Favour")

        result = move_to_jungle(player, "no")

        self.assertTrue(result)
        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)
        self.assertIn("rope", player["inventory"])

    def test_search_wreckage_gives_energy(self):
        player = create_player("Favour")

        move_to_jungle(player, "yes")

        self.assertEqual(player["energy"], 5)

    def test_invalid_wreckage_answer(self):
        player = create_player("Favour")

        result = move_to_jungle(player, "maybe")

        self.assertFalse(result)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    def test_invalid_cave_path(self):
        player = create_player("Favour")
        move_to_jungle(player, "no")

        result = move_to_cave(player, "3", "1")

        self.assertFalse(result)
        self.assertEqual(player["location"], "Jungle")

    def test_cannot_enter_cave_from_beach(self):
        player = create_player("Favour")
        original_energy = player["energy"]

        result = move_to_cave(player, "1", "1")

        self.assertFalse(result)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], original_energy)
        self.assertNotIn("lantern", player["inventory"])

    def test_invalid_cave_search(self):
        player = create_player("Favour")
        move_to_jungle(player, "no")

        result = move_to_cave(player, "1", "3")

        self.assertFalse(result)
        self.assertEqual(player["location"], "Jungle")

    def test_move_to_cave(self):
        player = create_player("Favour")
        move_to_jungle(player, "no")

        result = move_to_cave(player, "1", "1")

        self.assertTrue(result)
        self.assertEqual(player["location"], "Cave")
        self.assertEqual(player["energy"], 2)
        self.assertIn("lantern", player["inventory"])

    def test_cannot_cross_bridge_without_rope(self):
        player = create_player("Favour")
        player["location"] = "Cave"

        result = cross_bridge(player)

        self.assertFalse(result)
        self.assertEqual(player["location"], "Cave")

    def test_cannot_cross_bridge_from_beach(self):
        player = create_player("Favour")
        original_energy = player["energy"]

        result = cross_bridge(player)

        self.assertFalse(result)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], original_energy)

    def test_cross_bridge(self):
        player = create_player("Favour")
        player["location"] = "Cave"
        player["inventory"].append("rope")

        result = cross_bridge(player)

        self.assertTrue(result)
        self.assertEqual(player["location"], "Old Bridge")

    def test_cannot_restore_lighthouse_without_lantern(self):
        player = create_player("Favour")
        player["location"] = "Old Bridge"

        result = restore_lighthouse(player)

        self.assertFalse(result)
        self.assertFalse(player["won"])

    def test_restore_lighthouse(self):
        player = create_player("Favour")
        player["location"] = "Old Bridge"
        player["inventory"].append("lantern")

        result = restore_lighthouse(player)

        self.assertTrue(result)
        self.assertEqual(player["location"], "Lighthouse")
        self.assertTrue(player["won"])
        self.assertTrue(player["game_over"])

    def test_energy_runs_out(self):
        player = create_player("Favour")
        player["energy"] = 0

        result = check_energy(player)

        self.assertFalse(result)
        self.assertTrue(player["game_over"])

    def test_winner_does_not_lose(self):
        player = create_player("Favour")
        player["energy"] = 0
        player["won"] = True

        result = check_energy(player)

        self.assertTrue(result)
        self.assertFalse(player["game_over"])


if __name__ == "__main__":
    unittest.main()