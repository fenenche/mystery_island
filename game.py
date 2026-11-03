def create_player(name):
    """Create a new player."""

    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False,
        "searched_wreckage": False
    }


def move_to_jungle(player, search):
    """Move from Beach to Jungle."""

    if player["location"] != "Beach":
        return False

    if not player["searched_wreckage"]:

        if search == "yes":
            player["energy"] -= 1
            player["energy"] += 2

        elif search != "no":
            return False

        player["searched_wreckage"] = True

    player["location"] = "Jungle"
    player["energy"] -= 1

    if "rope" not in player["inventory"]:
        player["inventory"].append("rope")

    return True


def move_to_cave(player, path, search):
    """Move from Jungle to Cave."""

    if player["location"] != "Jungle":
        return False

    if path not in ["1", "2"]:
        return False

    if search not in ["1", "2"]:
        return False

    if path == "1":
        player["energy"] -= 1
    else:
        player["energy"] -= 2

    player["location"] = "Cave"

    if search == "1":
        player["energy"] -= 1
    else:
        player["energy"] -= 2

    if "lantern" not in player["inventory"]:
        player["inventory"].append("lantern")

    return True


def cross_bridge(player):
    """Cross the Old Bridge using a rope."""

    if player["location"] == "Cave" and "rope" in player["inventory"]:

        player["location"] = "Old Bridge"
        player["energy"] -= 1

        return True

    return False


def restore_lighthouse(player):
    """Restore the Lighthouse using a lantern."""

    if player["location"] == "Old Bridge" and "lantern" in player["inventory"]:

        player["location"] = "Lighthouse"
        player["energy"] -= 1
        player["won"] = True
        player["game_over"] = True

        return True

    return False


def check_energy(player):
    """Check whether the player has energy remaining."""

    if player["energy"] <= 0 and not player["won"]:

        player["game_over"] = True
        return False

    return True