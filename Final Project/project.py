import random
import sys

def main():
    name = input("What is your name, miner? ")
    player = {
        "name": name,
        "hp": 100,
        "gold": 50,
        "mine_power": 5,
        "pickaxe_level": 0,
        "potion": 2,
        "apple": 1,
        "flashlight": False,
        "final_pickaxe": False
    }
    print(f"\nWelcome, {name}, to Shattered by Stone.")
    travel(player)

def travel(player):
    while True:
        print("\n1. Mine\n2. Shop\n3. Stats & Items\n4. Quit (progress does not save)")
        choice = input("")
        if choice == "1":
            mine(player)
        elif choice == "2":
            shop(player)
        elif choice == "3":
            stats(player)
        elif choice == "4":
            print("Thanks for playing!")
            sys.exit(0)


def stats(player):
    print("\nStats & Items:")
    print(f"Name: {player["name"]}")
    print(f"HP: {player["hp"]}")
    print(f"Gold: {player["gold"]}")
    print(f"Mine Power: {player["mine_power"]}")
    print(f"Pickaxe level: {player["pickaxe_level"]}")
    print(f"Potions: {player["potion"]}")
    print(f"Apples: {player["apple"]}")
    print(f"Flashlight Owned: {player["flashlight"]}")

def shop(player):
    pickaxes = [
        ("Starter Pickaxe", 5, 0),
        ("Iron Pickaxe", 10, 50),
        ("Diamond Pickaxe", 20, 120),
        ("Mythical Pickaxe", 30, 250)
    ]
    while True:
        print("\nShop:")
        print(f"Gold: {player["gold"]}")
        print("Pickaxes:")
        i=0
        while i < len(pickaxes):
            name, power, price = pickaxes[i]
            if i <= player["pickaxe_level"]:
                print(f"{i}. {name} (owned)")
            else:
                print(f"{i}. {name}: {price} Gold")
            i+=1
        print("Gears: ")
        print("a. Potion (+40HP): 20 Gold")
        print("b. Apple (+5 Mine Power During Battle, Stackable): 35 Gold")
        print("c. Flashlight (Permanent, Identifies Rock Rarity During Fight): 25 Gold")
        print("d. Leave")
        choice = input("")
        if choice == "d":
            return
        if choice.isdigit():
            pick = int(choice)
            if pick < 0 or pick >= len(pickaxes):
                print("Invalid choice.")
                continue
            if pick <= player["pickaxe_level"]:
                print("You already own this pickaxe.")
                continue
            name, power, price = pickaxes[pick]
            if player["gold"] < price:
                print("Insufficient funds.")
                continue
            player["gold"] -= price
            player["pickaxe_level"] = pick
            player["mine_power"] = power
            print(f"{name} acquired!!!")
            if pick == len(pickaxes) - 1:
                player["final_pickaxe"] = True
            continue

        if choice == "a":
            if player["gold"] >= 20:
                player["gold"] -= 20
                player["potion"] += 1
                print("Potion acquired!!!")
            else:
                print("Insufficient funds.")
        elif choice == "b":
            if player["gold"] >= 35:
                player["gold"] -= 35
                player["apple"] += 1
                print("Apple acquired!!!")
            else:
                print("Insufficient funds.")
        elif choice == "c":
            if player["flashlight"]:
                print("You already own a flashlight. It's permanent!")
            elif player["gold"] >= 25:
                player["gold"] -= 25
                player["flashlight"] = True
                print("Flashlight acquired (and it has infinite battery)!!!")
            else:
                print("Insufficient funds.")

def mine(player):
    if player["final_pickaxe"]:
        print("\nYou can tell that this is the last time you'll enter the mines.")
        pickaxeium(player)
        return
    else:
        print("\nYou enter the cold, desolate mines. Despite all the gray, you sense opportunity.")
        if random.random() < 0.05:
            print("You feel the sturdy ground tremble underneath your feet... A LEGENDARY Pickaxeium appears with ??? HP! You think that this is your chance, but the rock laughs at your puny pickaxe and vanishes.")
            return
    rarity = choose_rarity()
    rock = generate_rock(rarity)
    print(f"A rock appears with {rock["hp"]} HP!")
    battle(player, rock, rarity)

def choose_rarity():
    roll = random.randint(1, 100)
    if roll <= 60:
        return "common"
    elif roll <= 90:
        return "rare"
    else:
        return "epic"

def generate_rock(rarity):
    if rarity == "common":
        return {"hp": random.randint(20, 35), "dmg": (1, 5), "gold": (10, 20)}
    if rarity == "rare":
        return {"hp": random.randint(35, 55), "dmg": (3, 10), "gold": (20, 35)}
    if rarity == "epic":
        return {"hp": random.randint(55, 80), "dmg": (8, 15), "gold": (35, 60)}

def battle(player, rock, rarity):
    power_up = 0

    while rock["hp"]>0 and player["hp"]>0:
        print(f"HP: {player["hp"]}")
        print(f"Rock HP: {rock["hp"]}")
        print(f"Mine Power: {player["mine_power"] + power_up}")
        print("Actions: Mine, Run, Potion, Apple, Flashlight")
        action = input("").lower()

        if action == "run":
            print("You escape the fight.")
            return
        if action == "potion":
            if player["potion"] > 0:
                player["potion"] -=1
                player["hp"] = min(100, player["hp"] + 40)
                print("+40 HP!!!")
            continue
        if action == "apple":
            if player["apple"] > 0:
                player["apple"] -= 1
                power_up += 5
                print("Temporary +5 PWR!!!")
            continue
        if action == "flashlight":
            if player["flashlight"]:
                print("You used Flashlight!!!")
                print(f"This rock is {rarity.upper()}!!!")
            else:
                print("You, uh... don't have a flashlight...")
            continue
        if action == "mine":
            dmg = player["mine_power"] + power_up
            rock["hp"] -= dmg
            print(f"You deal {dmg} DMG!!!")
        if rock["hp"] <= 0:
            break
        rock_dmg = random.randint(*rock["dmg"])
        player["hp"] -= rock_dmg
        print(f"The rock deals {rock_dmg} to you!!!")
    if player["hp"] <= 0:
        print("You were mined by the rock... maybe consider buying better gear from the shop next time.")
        sys.exit(0)
    gold = random.randint(*rock["gold"])
    player["gold"] += gold
    print(f"+{gold} gold!!!")

def pickaxeium(player):
    print("\nYou feel the sturdy ground tremble in fear underneath your feet...")
    print("A LEGENDARY Pickaxeium appears with 300 HP!!!")
    hp = 300
    while hp > 0 and player["hp"] > 0:
        print(f"\n Your HP: {player["hp"]}")
        print(f"Pickaxeium HP: {hp}")
        print("Actions: Mine, Potion, Apple")
        action = input("").lower()
        if action == "potion":
            if player["potion"] > 0:
                player["potion"] -=1
                player["hp"] = min(100, player["hp"] + 40)
                print("+40 HP!!!")
            continue
        if action == "apple":
            if player["apple"] > 0:
                player["apple"] -= 1
                player["mine_power"] += 5
                print("Temporary +5 PWR!!!")
            continue
        if action == "mine":
            hp -= player["mine_power"]
            print(f"You strike Pickaxeium for {player["mine_power"]} DMG!!!")
        if hp <= 0:
            break
        dmg = random.randint(15, 30)
        player["hp"] -= dmg
        print(f"Pickaxeium swings back for {dmg}!!!")

    if player["hp"] > 0:
        print("\nYou defeated Pickaxeium, the ultimate elusive ore!!!")
        print("You forge a new pickaxe made of Pickaxeium, creating the strongest pickaxe. The town deems you The Greatest Miner in the World.")
        print("However, the thrill of the battle with Pickaxeium pushes you to travel around the world searching for another vein of the elusive ore.")
        print("You grow old doing so, but as you continue to search, your craving for battle only grows.")
        print("Eventually, you decide to throw your pickaxe back into the mines, hoping that some other miner will experience that same euphoria you once had.")
        print("\nThanks for playing Shattered by Stone!")
        sys.exit(0)
    else:
        print("\nYou fought hard, but Pickaxeium defeated you...")
        print("The rock steals your body and name and returns to the town as an imposter, claiming that it defeated Pickaxeium.")
        print("As a result of your hard training in the mines, your body grew strong enough to be a vessel for the rock.")
        print("Pickaxeium takes the opportunity to mine the Earth itself and become the one and only rock, ultimately destroying the world in the process.")
        print("You watch from the eyes of your own body as Pickaxeium uses it to destroy the last piece of stone in the world, unable to move, cry, or even scream.")
        print('But a glimmer of hope in the form of text flashes in front of your somehow persisting conciousness. "Run the project again to fight for another ending?"')
        print("\nThanks for playing Shattered by Stone!")
        sys.exit(0)
if __name__ == "__main__":
    main()
