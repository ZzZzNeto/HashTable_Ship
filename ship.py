import random, os

class CrewMember:
    def __init__(self, name, birth, cpf):
        self.cpf = cpf
        self.name = name
        self.birth = birth

class Ship: 
    def __init__(self):
        self.crew = [[],[],[],[],[],[],[],[],[],[]]
        self.total = 0

    def get_hash(self, cpf):
        return int(cpf) % 10
    
    def join(self, crewmember : CrewMember):
        self.total += 1
        hash = self.get_hash(crewmember.cpf)
        self.crew[hash].append(crewmember)

    def list_crew(self):
        os.system("cls")
        print("Crew:\n")
        for line in self.crew:
            for member in line:
                print(f"{member.cpf} | {member.name} - {member.birth}")

    def find(self, cpf):
        hash = self.get_hash(cpf)
        for member in self.crew[hash]:
            if member.cpf == cpf:       
                return member
        return None

ship = Ship()

os.system("cls")
while True: 
    print("Welcome capitain!")
    print(f"Total crew members in the ship: {ship.total}\n")
    choice = input("1 - View crew list\n2 - Find crew member\n3 - Insert crew member\n4 - Sail\n\ninsert: ")
    os.system("cls")

    if choice == "1":
        if not ship.total == 0:
            ship.list_crew()
            x = input("\nPress any key to go back... ")
            os.system("cls")
        else:
            print("Ship is empty!\n")
            input("Press any key to go back... ")
            os.system("cls")

    elif choice == "2":
        if not ship.total == 0:
            cpf = int(input("Crew member cpf: "))
            member = ship.find(cpf)
            os.system("cls")

            if member:
                print("founded!\n")
                print(f"{member.cpf} | {member.name} - {member.birth}\n")
                input("Press any key to go back... ")
                os.system("cls")
            else:
                print("Crew Member not in the ship!\n")
                input("Press any key to go back... ")
                os.system("cls")
        else:
            print("Ship is empty!\n")
            input("Press any key to go back... ")
            os.system("cls")
    
    elif choice == "3":
        if ship.total < 50:
            name = input("Name: ")
            birth = input("Birth date: ")
            cpf = int(input("CPF: "))
            
            if not ship.find(cpf):
                member = CrewMember(name=name, birth=birth, cpf=cpf)
                ship.join(member)
                os.system("cls")
            else:
                os.system("cls")
                print("Crew member with that cpf already in the ship\n")
                input("Press any key to go back... ")
                os.system("cls")
        else: 
            print("Ship is full!\n")
            input("Press any key to go back... ")
            os.system("cls")
    
    elif choice == "4":
        break
    
    else:
        pass