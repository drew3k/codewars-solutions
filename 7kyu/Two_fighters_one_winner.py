def declare_winner(fighter1, fighter2, first_attacker):
    while fighter1.health > 0 and fighter2.health > 0:
        if first_attacker == fighter1:
            while fighter1.health > 0 or fighter2.health > 0:
                fighter2.health -= fighter1.damage_per_attack
                fighter1.health -= fighter2.damage_per_attack
                if fighter2.health <= 0 and fighter1.health <= 0:
                    return first_attacker
                if fighter2.health <= 0:
                    return fighter1.name
                if fighter1.health <= 0:
                    return fighter2.name
        else:
            while fighter1.health > 0 or fighter2.health > 0:
                fighter1.health -= fighter2.damage_per_attack
                fighter2.health -= fighter1.damage_per_attack
                if fighter1.health <= 0 and fighter2.health <= 0:
                    return first_attacker
                if fighter2.health <= 0:
                    return fighter1.name
                if fighter1.health <= 0:
                    return fighter2.name