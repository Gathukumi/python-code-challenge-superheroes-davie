from app import app, db
from models import Hero, Power, HeroPower

def seed_heroes(heroes_data):
    print(":female_superhero: Seeding heroes...")
    for hero_data in heroes_data:
        hero = Hero(**hero_data)
        db.session.add(hero)
        db.session.commit()
    print("Hero seeding completed.")

def seed_powers(powers_data):
    print(":female_superhero: Seeding powers...")
    for power_data in powers_data:
        power = Power(**power_data)
        db.session.add(power)
    db.session.commit()
    print("Power seeding completed.")

def seed_hero_powers(hero_power_data ):
    print(":female_superhero: Seeding hero_powers...")
    for hero_power_data in heroes_power_data:
        hero_power_data = HeroPower(**hero_power_data)
        db.session.add(hero_power_data)
        db.session.commit()
        print("HeroPower seeding completed.")

if __name__ == '__main__':
    # 30 Heroes
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jessica Drew", "super_name": "Spider-Woman"},
        {"name": "Natasha Romanoff", "super_name": "Black Widow"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Jean Grey", "super_name": "Phoenix"},
        {"name": "Peter Parker", "super_name": "Spider-Man"},
        {"name": "Tony Stark", "super_name": "Iron Man"},
        {"name": "Bruce Banner", "super_name": "Hulk"},
        {"name": "Thor Odinson", "super_name": "Thor"},
        {"name": "Steve Rogers", "super_name": "Captain America"},
        {"name": "Matt Murdock", "super_name": "Daredevil"},
        {"name": "Wade Wilson", "super_name": "Deadpool"},
        {"name": "Scott Summers", "super_name": "Cyclops"},
        {"name": "Logan Howlett", "super_name": "Wolverine"},
        {"name": "Rogue", "super_name": "Rogue"},
        {"name": "Hank McCoy", "super_name": "Beast"},
        {"name": "Bobby Drake", "super_name": "Iceman"},
        {"name": "Emma Frost", "super_name": "Emma Frost"},
        {"name": "Kurt Wagner", "super_name": "Nightcrawler"},
        {"name": "Piotr Rasputin", "super_name": "Colossus"},
        {"name": "Remy LeBeau", "super_name": "Gambit"},
        {"name": "Jean-Paul Beaubier", "super_name": "Northstar"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Illyana Rasputin", "super_name": "Magik"},
        {"name": "Betsy Braddock", "super_name": "Psylocke"},
    ]
    
    # Rest of the code remains unchanged
# 30 Powers
powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"},
    {"name": "telekinesis", "description": "move objects with the mind"},
    {"name": "weather manipulation", "description": "control and manipulate the weather"},
    {"name": "telepathy", "description": "read and control minds"},
    {"name": "energy projection", "description": "emit and control various forms of energy"},
    {"name": "invisibility", "description": "render oneself unseen by the naked eye"},
    {"name": "teleportation", "description": "instantaneous travel from one location to another"},
    {"name": "time manipulation", "description": "control and manipulate time"},
    {"name": "regeneration", "description": "ability to heal rapidly from any physical injury"},
    {"name": "shape-shifting", "description": "ability to change appearance at will"},
    {"name": "intangibility", "description": "pass through solid objects"},
    {"name": "force fields", "description": "create protective shields of energy"},
    {"name": "mind control", "description": "control the thoughts and actions of others"},
    {"name": "super speed", "description": "move at incredible speeds"},
    {"name": "sonic scream", "description": "emit powerful sonic waves through the mouth"},
    {"name": "size manipulation", "description": "change one's size at will"},
    {"name": "gravity manipulation", "description": "control the force of gravity"},
    {"name": "pyrokinesis", "description": "create and control fire with the mind"},
    {"name": "cryokinesis", "description": "create and control ice with the mind"},
    {"name": "mind reading", "description": "read the thoughts of others"},
    {"name": "immortality", "description": "live forever without aging"},
    {"name": "energy absorption", "description": "absorb and manipulate various forms of energy"},
    {"name": "phasing", "description": "pass through solid objects"},
    {"name": "probability manipulation", "description": "alter the likelihood of events"},
    {"name": "super agility", "description": "move with incredible agility and reflexes"},
    {"name": "enhanced durability", "description": "withstand damage beyond normal human limits"},
]

# 30 Hero Power combinations
# ... (previous code remains unchanged)

# 30 Hero Power combinations
heroes_power_data = [
    {'strength': 'Average', 'hero_id': 1, 'power_id': 1},
    {'strength': 'Strong', 'hero_id': 2, 'power_id': 2},
    {'strength': 'Weak', 'hero_id': 3, 'power_id': 3},
    {'strength': 'Average', 'hero_id': 4, 'power_id': 4},
    {'strength': 'Strong', 'hero_id': 5, 'power_id': 5},
    {'strength': 'Weak', 'hero_id': 6, 'power_id': 6},
    {'strength': 'Average', 'hero_id': 7, 'power_id': 7},
    {'strength': 'Strong', 'hero_id': 8, 'power_id': 8},
    {'strength': 'Weak', 'hero_id': 9, 'power_id': 9},
    {'strength': 'Average', 'hero_id': 10, 'power_id': 10},
    {'strength': 'Strong', 'hero_id': 11, 'power_id': 11},
    {'strength': 'Weak', 'hero_id': 12, 'power_id': 12},
    {'strength': 'Average', 'hero_id': 13, 'power_id': 13},
    {'strength': 'Strong', 'hero_id': 14, 'power_id': 14},
    {'strength': 'Weak', 'hero_id': 15, 'power_id': 15},
    {'strength': 'Average', 'hero_id': 16, 'power_id': 16},
    {'strength': 'Strong', 'hero_id': 17, 'power_id': 17},
    {'strength': 'Weak', 'hero_id': 18, 'power_id': 18},
    {'strength': 'Average', 'hero_id': 19, 'power_id': 19},
    # Continue adding more hero power data entries as needed
]

with app.app_context():
    seed_heroes(heroes_data)
    seed_powers(powers_data)
    seed_hero_powers(heroes_power_data)
