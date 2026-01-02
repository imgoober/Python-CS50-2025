from project import travel
from project import mine
from project import shop
from project import pickaxeium
from project import stats
from project import generate_rock
from project import choose_rarity
from project import battle

dummy = {
    "name": "test",
    "hp": 100,
    "gold": 50,
    "mine_power": 5,
    "pickaxe_level": 0,
    "potion": 2,
    "apple": 1,
    "flashlight": False,
    "final_pickaxe": False
}

# travel(), mine(), shop(), pickaxeium(), battle(), and stats() use input() so they need to be tested manually
# the most i can do with these functions is check if they are callable

def test_travel():
    assert callable(travel)

def test_mine():
    assert callable(mine)

def test_shop():
    assert callable(shop)

def test_pickaxeium():
    assert callable(pickaxeium)

def test_battle():
    assert callable(battle)

def test_stats():
    assert callable(stats)

def test_generate_rock():
    rock = generate_rock("common")
    assert "hp" in rock
    assert "dmg" in rock
    assert "gold" in rock

def test_choose_rarity():
    rarity = choose_rarity()
    assert (rarity == "common" or rarity == "rare" or rarity == "epic") == True


