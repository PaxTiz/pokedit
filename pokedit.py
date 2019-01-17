#!/usr/bin/env python

import config
import sys
import i18n
import parser

def createTable():
    """
    Create tables used for pokemon storage system and team
    """
    config.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            level INT NOT NULL,
            type1 VARCHAR(255) NOT NULL,
            type2 VARCHAR(255) DEFAULT NULL,
            nature VARCHAR(255) NOT NULL,
            special_capacity VARCHAR(255) NOT NULL
        )
    """)

    config.cursor.execute("""
        CREATE TABLE IF NOT EXISTS attacks (                                    
            id INTEGER PRIMARY KEY AUTOINCREMENT,                               
            name VARCHAR(255) NOT NULL,                                         
            power INTEGER NOT NULL,                                             
            pokemon_id INTEGER,                                                 
            FOREIGN KEY(pokemon_id) REFERENCES pokemon(id)                      
        ) 
    """)

    config.cursor.execute("""
        CREATE TABLE IF NOT EXISTS team(
            poke1 VARCHAR(255) DEFAULT NULL,
            poke2 VARCHAR(255) DEFAULT NULL,
            poke3 VARCHAR(255) DEFAULT NULL,
            poke4 VARCHAR(255) DEFAULT NULL,
            poke5 VARCHAR(255) DEFAULT NULL,
            poke6 VARCHAR(255) DEFAULT NULL
        )
    """)

    config.cursor.execute("""
        INSERT INTO team(poke1, poke2, poke3, poke4, poke5, poke6) VALUES (" ", " ", " ", " ", " ", " ")
    """)

    config.connexion.commit()

def parseArgs(args):
    """
    Parse args for display return of command
    """
    if len(args) == 1:
        print(i18n.t("strings.usage.title"))
        print(" USAGE :")
        print("     -a <pokemon>                 ", i18n.t("strings.usage.add"))
        print("     -r <pokemon>                 ", i18n.t("strings.usage.remove"))
        print("     -l                           ", i18n.t("strings.usage.listAvaible"))
        print("     -t                           ", i18n.t("strings.usage.listTeam"))
        print("     -s <position> <pokemon>      ", i18n.t("strings.usage.setTeam"))         
    else:
        if args[1] == "-a":
            parser.addPokemon(args[2])
        elif args[1] == "-r":
            parser.removePokemon(args[2])
        elif args[1] == "-l":
            parser.listPokemons()
        elif args[1] == "-t":
            parser.listTeam()
        elif args[1] == "-s":
            parser.setTeam(args[2], args[3])
        else:
            print(i18n.t("strings.OptionError"))

def main():
    createTable()    
    parseArgs(sys.argv)
    config.connexion.close()


if __name__ == "__main__":
    main()
