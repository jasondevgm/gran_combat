from rich.console import Console
from rich.table import Table
import inquirer
import random
import os
import time

# Fight phrases
class Phrases:
    attack = [
        '{} ataca con un {} y acierta el golpe',
        '{} lanza un golpe de {} y acierta!',
        '{} arremete con {} y da en el blanco'
    ]
    dodge = [
        '{} esquiva con un {} y no recibe daño',
        '{} bloquea el ataque con un {} y resulta ileso',
        '{} evita el golpe con un {} y no sufre daño'
    ]
    hit = [
        '{} recibe un ataque directo de {} causandole bastante daño',
        '{} no puede esquivar el golpe de {}, haciendole caer',
        '{} esquiva con un {} pero falla y recibe daño'
    ]
    fail = [
        '{} ataca pero falla el ataque',
        '{} lanza un gancho pero falla',
        '{} se precipita en el ataque y falla'
    ]
    finishing_move = [
        '{} UTILIZA SU ATAQUE MAS PODEROSO Y GOLPEA A SU ENEMIGO SIN PIEDAD!!!',
        '{} LANZA SU TECNICA DEFINITIVA Y DESTRUYE A SU CONTRINCANTE!!!',
        '{} CON SU ATAQUE FINAL DESTRUYE A SU ENEMIGO Y MEDIO CAMPO DE BATALLA!!!'
    ]
    winner = [
        '{} SE ALZA CON LA VICTORIA!!!',
        '{} GANA POR KO!!!',
        '{} ES QUIEN GANA LA BATALLA!!!',
        '{} CONSIGUE LA VICTORIA',
        '{} DERROTA DE MANERA APLASTANTE A SU CONTRINCANTE'
    ]

# these variables and constants
# are to control both the global elements

console = Console(width=400, color_system="auto")
style = "black on gray"
MAXPOWER = 72
lifeIncrement = 1

schoolsStats = "  Escuela del Ermitaño Tortuga: Técnica del Kame-Hame-Ha\n\n  Escuela del Cuervo Genial: Técnica de los mil puños \n\n  Escuela de Hoi-Poi: Técnica de la invisibilidad \n\n  Escuela de Namac: Técnica de la regeneración\n"

attackPhrasesSize = len(Phrases.attack)
dodgePhrasesSize = len(Phrases.dodge)
hitPhrasesSize = len(Phrases.hit)
finishPhrasesSize = len(Phrases.finishing_move)
winnerPhrasesSize = len(Phrases.winner)
failPhrasesSize = len(Phrases.fail)

# Selections inquirer

selectChoice = [
    inquirer.List("Choice", message="Quierer continuar?",
                  choices=["Si", "No"])
]
schoolChoice = [
    inquirer.List("Choice", message="Escoger escuela de procedencia",
                  choices=["Follet Tortuga", "Corb Genial", "Hoi-Poi", "Namac"]
                  )
]

figtherChoiceName = [
    inquirer.List("Choice", message="Selecciona tu personaje",
                  choices=["Son Goku", "Krillin", "Bulma", "Vegeta",
                           "Son Gohan", "Trunks", "Freezer", "Piccolo"]
                  )
]

figtherChoiceStatistics = [
    inquirer.List("Choice", message="Selecciona habilidad",
                  choices=["Fuerza", "Constitucion", "Tamaño",
                           "Habilidad", "Personalidad", "Salir"]
                  )
]

# Class for fighters

class Fighter():
    def __init__(self, fname, fpower, fphysique, fsize, fskill, fpersonality, fschool, nPlayer):
        self.nplayer = nPlayer
        self.school = fschool
        # FO (força)
        # CO (constitució)
        # TA (tamany)
        # DE (destresa)
        # PER (personalitat)

        self.name = fname
        self.power = fpower
        self.physique = fphysique
        self.size = fsize
        self.skill = fskill
        self.personality = fpersonality
#############################################################

        # PR (punts de resistència) = CO+TA
        # PM (punts de mal) = (FO+TA)/4
        # PA (% probabilitat d’atac) = DE+FO+CO
        # PE (% probabilitat d’esquivar) = DEx3

    def skillsFromSchool(self):
        if self.school == "Follet Tortuga":
            # Escola del Follet Tortuga: Tècnica del Kame-Hame-Ha especialitzada en el mal
            # PM = (FOR+TAM+PER)/4
            print("Follet Tortuga")
            self.PR = (self.physique + self.size) + lifeIncrement
            self.PM = (self.power + self.size + self.personality) / 4
            self.PA = self.skill + self.power + self.physique
            self.PE = self.skill * 3
        elif self.school == "Corb Genial":
            # Escola del Corb Genial: Tècnica dels mil punys especialitzada en l’atac
            # PA (%) = DES+FOR+CON+PER
            print("Corb Genial")
            self.PR = (self.physique + self.size) + lifeIncrement
            self.PM = (self.power + self.size) / 4
            self.PA = self.skill + self.power + self.physique + self.personality
            self.PE = self.skill * 3
        elif self.school == "Hoi-Poi":
            # Escola de Hoi-Poi: Tècnica de la invisibilitat especialitzada en l’esquiva
            # PE (%) = DESx3+PER
            print("Hoi-Poi")
            self.PR = (self.physique + self.size) + lifeIncrement
            self.PM = (self.power + self.size) / 4
            self.PA = self.skill + self.power + self.physique
            self.PE = self.skill * 3 + self.personality
        elif self.school == "Namac":
            # Escola de Namac: Tècnica de la regeneració especialitzada en la resistència
            # PR = CON+TAM+PER
            print("Namac")
            self.PR = (self.physique + self.size + self.personality) + lifeIncrement
            self.PM = (self.power + self.size) / 4
            self.PA = self.skill + self.power + self.physique
            self.PE = self.skill * 3
        else:
            print("Sin escuela")
            self.PR = (self.physique + self.size) + lifeIncrement
            self.PM = (self.power + self.size) / 4
            self.PA = self.skill + self.power + self.physique
            self.PE = self.skill * 3

        # tableStats for show stats 
    def callSkillsFromSchool(self):
        return self.skillsFromSchool()

    def tableStats(self):
        print("\n################################################")
        fstatistics = "Fuerza: {}\nConstitucion: {}\nTamaño: {}\nHabilidad: {}\nPersonalidad: {}\nP. resistencia: {}\nP. daño: {}\n% de ataque: {}\n% de esquivar: {}\n".format(
            self.power, self.physique, self.size, self.skill, self.personality, self.PR, self.PM, self.PA, self.PE)
        table = Table(title="\nGran combate")

        table.add_column("Personaje", style="cyan", justify="center")
        table.add_column("Estadisticas", style="cyan", justify="center")
        table.add_column("Escuela", style="cyan", justify="center")

        table.add_row(self.name, fstatistics, self.school)
        console.print(table)

def firstPlayerCreation(nPlayer):
    """
    Functions to define the first player

    """
    os.system('cls')
    print("\n########################################################\n")
    print('\t\033[0;36m Primer jugador\033[0m\n')
    firstFigtherName = inquirer.prompt(figtherChoiceName)

    os.system('cls')
    print("\n########################################################\n")
    print('\t\033[0;36m Primer jugador\033[0m\n')
    print(schoolsStats)
    firstFigtherschool = inquirer.prompt(schoolChoice)

    fighterFunction72(firstFigtherName, firstFigtherschool, nPlayer)
    print("\n########################################################\n")

def secondPlayerCreation(nPlayer):
    """
    Functions to define the second player

    """
    os.system('cls')
    print("\n########################################################\n")
    print("\t\033[0;36mSegundo jugador\033[0m\n")
    secondFigtherName = inquirer.prompt(figtherChoiceName)

    os.system('cls')
    print("\n########################################################\n")
    print("\t\033[0;36mSegundo jugador\033[0m\n")
    print(schoolsStats)
    secondFigtherschool = inquirer.prompt(schoolChoice)

    fighterFunction72(secondFigtherName, secondFigtherschool, nPlayer)
    print("\n########################################################\n")

# the player instances of fighters 
 
Player1Figther: Fighter
Player2Figther: Fighter


def inputValidator(ability):
    while True:
        DragonFighterAbility = input("{}: ".format(ability))
        if DragonFighterAbility.isdigit():
            DragonFighterAbility = int(DragonFighterAbility)
            if DragonFighterAbility > 18:
                print("Maximo 18 puntos por habilidad")
                continue
            elif DragonFighterAbility < 0:
                print("Añade puntos positivos a tu personaje")
                continue
            elif DragonFighterAbility == '':
                print("Añade puntos positivos a tu personaje")
                continue
            else:
                return DragonFighterAbility
        else:
            print("Debes de introducir un numero.")

# Function to create fighters
def createFighter(fname, *args):
    DragonFighter = Fighter(fname, *args)
    return DragonFighter


def fighterFunction72(fighterName, fighterSchool, nPlayer):
    fName = list(fighterName.values())[0]
    fSchool = list(fighterSchool.values())[0]
    functionStatsForFighter(fName, 0, 0, 0, 0, 0, fSchool, nPlayer)


def functionStatsForFighter(fight3r, pwer, physiq, siz, skll, personalty, fschool, nPlayer):
    power = pwer
    physique = physiq
    size = siz
    skill = skll
    personality = personalty
    school = fschool
    sumAllPowers = (MAXPOWER - (power + physique + size + skill + personality))
    statistics = "Fuerza: {}\nConstitucion: {}\nTamaño: {}\nHabilidad: {}\nPersonalidad: {}".format(
        power, physique, size, skill, personality)

    if sumAllPowers != 0:
        os.system('cls')
        print("\n###################################################")
        print('\n\t{}'.format(fight3r))
        table = Table(title="")
        table.add_column("Caracteristicas jugador",
                         style="cyan", justify="center")

        table.add_row(statistics)
        console.print(table)
        print("\nTienes \033[0;36m {}\033[0m puntos a repartir entre \033[0;36m5 habilidades\033[0m\ncada habilidad solo puede tener un maximo de \033[0;36m18 puntos\033[0m.\n".format(sumAllPowers))

        figtherAbility = inquirer.prompt(figtherChoiceStatistics)
        abilityName = list(figtherAbility.values())[0]
        if (abilityName == "Fuerza"):
            powerValue = inputValidator(abilityName)
            functionStatsForFighter(fight3r, powerValue,
                                    physique, size, skill, personality, school, nPlayer)
        elif (list(figtherAbility.values())[0] == "Constitucion"):
            physiqueValue = inputValidator(abilityName)
            functionStatsForFighter(fight3r, power,
                                    physiqueValue, size, skill, personality, school, nPlayer)
        elif (list(figtherAbility.values())[0] == "Tamaño"):
            sizeValue = inputValidator(abilityName)
            functionStatsForFighter(fight3r, power,
                                    physique, sizeValue, skill, personality, school, nPlayer)
        elif (list(figtherAbility.values())[0] == "Habilidad"):
            skillValue = inputValidator(abilityName)
            functionStatsForFighter(fight3r, power,
                                    physique, size, skillValue, personality, school, nPlayer)
        elif (list(figtherAbility.values())[0] == "Personalidad"):
            personalityValue = inputValidator(abilityName)
            functionStatsForFighter(fight3r, power,
                                    physique, size, skill, personalityValue, school, nPlayer)
    else:
        print('\n')
        selection = inquirer.prompt(selectChoice)
        if list(selection.values())[0] == "No":
            if nPlayer == 1:
                firstPlayerCreation(1)
            else:
                secondPlayerCreation(2)
        else:
            if nPlayer == 1:
                global Player1Figther
                Player1Figther = createFighter(
                    fight3r, power, physique, size, skill, personality, school, nPlayer)
                Player1Figther.callSkillsFromSchool()
            else:
                global Player2Figther
                Player2Figther = createFighter(
                    fight3r, power, physique, size, skill, personality, school, nPlayer)
                Player2Figther.callSkillsFromSchool()


def fightInit(p1, p2):

    randomAttackPhrase = random.randint(0, (attackPhrasesSize-1))
    attackPhrase = Phrases.attack[randomAttackPhrase]

    randomDodgePhrase = random.randint(0, (dodgePhrasesSize-1))
    dodgePhrase = Phrases.dodge[randomDodgePhrase]

    randomHitPhrase = random.randint(0, (hitPhrasesSize-1))
    hitPhrase = Phrases.hit[randomHitPhrase]

    randomFailPhrase = random.randint(0, (failPhrasesSize-1))
    failPhrase = Phrases.fail[randomFailPhrase]

    # finish attack

    randomFinishPhrase = random.randint(0, (finishPhrasesSize-1))
    finishPhrase = Phrases.finishing_move[randomFinishPhrase]
    
    # This variable is used to determine the probability
    # of a critic attack, use with care
    lowProbability = 0.99
    randomNumber3 = random.uniform(0, 1)

    randomNumber1 = random.uniform(0, 1)
    randomNumber2 = random.uniform(0, 1)

    hitProbability = p1.PA / 100
    dodgeProbability = p2.PE / 100

    #print("\n  Player 1 Attack= {} \n  Player 2 Dodge= {} \n  Random number= {}\n  hit probability= {} ".format(p1.PA, p2.PE,  randomNumber1, hitProbability))

    if randomNumber1 <= hitProbability:
        if randomNumber2 <= dodgeProbability:
            time.sleep(1)
            p2.PR = p2.PR - Player1Figther.PM 
            print(" - ", attackPhrase.format(p1.name, hitProbability))
            if p2.PR < 0.30:
                if randomNumber3 <= lowProbability:
                    print("########################################################################")
                    p2.PR = p2.PR - 100 
                    print(finishPhrase.format(p1.name))
                    print("########################################################################")
                else:
                    False
        else:
            time.sleep(1)
            print(" - ", dodgePhrase.format(p2.name, dodgeProbability))
    else:
        time.sleep(1)
        print(" - ", failPhrase.format(p1.name))

def combatField():
    
    os.system('cls')
    Player1Figther.tableStats()
    Player2Figther.tableStats()
    
    print("\n")
    
    time.sleep(3)
    randomWinnerPhrase = random.randint(0, (winnerPhrasesSize-1))
    winnerPhrase = Phrases.winner[randomWinnerPhrase]
    print("           EL COMBATE COMIENZA!!\n")

    while Player1Figther.PR > 0 and Player2Figther.PR > 0:
        if random.randint(0, 1) == 0:
            #print("\n\tEl jugador uno empieza el juego")
            fightInit(Player1Figther, Player2Figther)
        else:
            #print("\n\tEl jugador dos empieza el juego")
            fightInit(Player2Figther, Player1Figther)

    Player1Figther.tableStats()
    Player2Figther.tableStats()
    #print("size of random winner phrases: ", randomWinnerPhrase)
    winner = Player1Figther.name if Player1Figther.PR > Player2Figther.PR else Player2Figther.name
    print("\n         ", winnerPhrase.format(winner))

def _main_():
    firstPlayerCreation(1)
    secondPlayerCreation(2)
    combatField()

_main_()
