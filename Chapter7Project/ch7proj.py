print("Welcome to Somthing Simulator")
print("By: Lawson F")

cavewhere = 1
investigate = 1
waterortree = 1
fightreason = 1
smartorforce = 1
getstone = 1
bookexplore = 1


print("\nYou're standing at the entrance of a mysterious cave. The air smells damp and fresh, and you hear faint sounds echoing from within. There are two paths ahead of you:")
print("\n1. A dark tunnel that seems to go deeper into the cave.")
print("2. A bright, glittering opening with sunlight streaming in.")
cavewhere1 = float(input('\nWould you like to continue with option 1 or option 2 (use "1" or "2"):'))

if cavewhere1 == 1:
    print("\nYou venture into the darkness, and the air grows colder as you go deeper. You see a faint light ahead.")
    print("\n1. Investigate the light.")
    print("2. Go back and continue exploring the cave")

    investigate = float(input('\nWould you like to continue with option 1 or option 2 (use "1" or "2"):'))

    if investigate == 1:
        print("\nYou approach the light cautiously, and you discover an underground crystal glowing with an otherworldly energy. As you reach out to touch it, the ground trembles, and a hidden door opens. Inside, you find an ancient treasure chest filled with gold coins and jewels! However, just as you begin to celebrate, a rumbling sound shakes the cave, and a shadowy figure emerges.")
        print("\n1. Fight the figure")
        print("2. Try to reason with the figure")

        fightreason = float(input('\nWould you like to continue with option 1 or option 2 (use "1" or "2"):'))

        if fightreason == 1:
            print("\nYou draw your weapon and prepare for battle. The figure is a stone golem, but with quick thinking, you manage to find a weak spot and defeat it. The treasure is now yours, and the golem crumbles into dust. You've won the treasure and the cave’s mysterious power!\n")

        elif fightreason == 2:
            print("\nYou try to speak to the figure, and to your surprise, it stops. It turns out that the golem is a guardian of the treasure, and if you show respect, it lets you take a portion of the treasure. The golem returns to its resting state, and you leave with gold and a newfound respect for the cave’s mysteries.\n")

        else:
            print("\nUR BAD PLEASE USE A 1 OR A 2, AND RESTART THE PROGRAM")

    elif investigate == 2:
        print("\nYou decide to press on further into the cave. As you continue, you come across an ancient stone doorway that seems to be sealed by a mysterious inscription. You can’t read it, but you sense a hidden mechanism. Do you:")
        print("\n1. Try to solve the riddle on the door")
        print("2. Push the door open with force")

        smartorforce = float(input('\nWould you like to continue with option 1 or option 2 (use "1" or "2"):'))

        if smartorforce == 1:
            print("\nAfter examining the symbols carefully, you realize the answer is something simple: “Light.” You set a nearby torch into a holder by the door, and it opens with a soft click. Inside, you find a hidden chamber filled with relics and a glowing orb that seems to pulse with life. The secrets of the cave are now yours!\n")

        elif smartorforce == 2:
            print("\nYou decide not to bother with the puzzle and try to force the door open. It creaks and groans as you push against it. The door eventually gives way, but not without triggering a trap! A cloud of dust bursts from the cracks, and you find yourself temporarily blinded, but after a few moments, the dust settles, and you see an underground river that leads to a mysterious cave system. While you avoid the trap, your sense of adventure grows even stronger.\n")

        else:
            print("\nUR BAD PLEASE USE A 1 OR A 2, AND RESTART THE PROGRAM")

    else:
        print("\nUR BAD PLEASE USE A 1 OR A 2, AND RESTART THE PROGRAM")


elif cavewhere1 == 2:
    print("\nYou step into the sunlight and find yourself standing in a lush, green valley. There are two paths before you.")
    print("\n1. Follow the path that leads to a shimmering waterfall.")
    print("2. Take the path that leads toward a large, ancient tree.")

    waterortree = float(input('\nWould you like to continue with option 1 or option 2 (use "1" or "2"):'))

    if waterortree == 1:
        print("You follow the sound of rushing water, and soon you find yourself standing before a beautiful, sparkling waterfall. Behind it, hidden in the rocks, is a secret cave. Inside, you find ancient drawings on the walls and a powerful artifact—a glowing, enchanted stone that hums with magical energy. However, as you reach out to grab the stone, the ground beneath you begins to shake.")
        print("\n1. Stand your ground and grab the stone")
        print("2. Leave the stone alone and exit the cave")

        getstone = float(input('\nWould you like to continue with option 1 or option 2 (use "1" or "2"):'))

        if getstone == 1:
            print("\nYou clutch the glowing stone, and the shaking stops. Suddenly, the waterfall reveals a hidden passage that leads to an underground chamber filled with treasure and ancient artifacts. You've uncovered an entire lost civilization’s secrets!\n")

        elif getstone == 2:
            print("\nYou decide not to risk disturbing the artifact. You turn and walk back to the valley. As you leave the cave, you feel a sense of calm and contentment. The treasure might have been tempting, but sometimes it’s best to leave things undisturbed.\n")

        else:
            print("\nUR BAD PLEASE USE A 1 OR A 2, AND RESTART THE PROGRAM")

    elif waterortree == 2:
        print("You wander down the path toward the tree, feeling its ancient energy. Upon reaching it, you notice a small door carved into its trunk. Inside, you find a cozy, hidden little room with books and scrolls. The tree is a guardian of knowledge, and you discover secrets about the world’s history and the trees that protect it.")
        print("\n1. Stay and read the books")
        print("2. Leave and explore further")
        
        bookexplore = float(input('\nWould you like to continue with option 1 or option 2 (use "1" or "2"):'))

        if bookexplore == 1:
            print("\nYou sit and absorb the wisdom contained in the ancient texts. Over time, you grow in knowledge and understanding of the world. The tree shares its secrets, and you become a wise scholar, forever bound to the ancient tree.\n")

        elif bookexplore == 2:
            print("\nYou thank the tree for its wisdom and leave the small room, venturing further into the valley. As you explore, you find more hidden treasures, but your mind stays focused on the lessons you learned from the tree. You now see the world through wiser eyes.\n")

        else:
            print("\nUR BAD PLEASE USE A 1 OR A 2, AND RESTART THE PROGRAM")

    else:
        print("\nUR BAD PLEASE USE A 1 OR A 2, AND RESTART THE PROGRAM")

else:
    print("\nUR BAD PLEASE USE A 1 OR A 2, AND RESTART THE PROGRAM")