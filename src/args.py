import sys
import i18n

import config

class Args():
    def __init__(self, db):
        self.db = db


    def addPokemon(self, name):
        params = (name, 0, "null", "null", "null", "null")
        sql = 'INSERT INTO pokemons(name, level, type1, type2, nature, special_capacity) VALUES (?, ?, ?, ?, ?, ?)'
        
        self.db.get_cursor().execute(sql, params)
        self.db.get_connexion().commit()

        print(name, i18n.t("strings.parser.add"))


    def removePokemon(self, name):
        sql = 'DELETE FROM pokemons WHERE name = ?'
        self.db.get_cursor().execute(sql, [name])
        self.db.get_connexion().commit()

        print(name, i18n.t("strings.parser.remove"))


    def listPokemons(self):
        sql = 'SELECT name FROM pokemons'

        self.db.get_cursor().execute(sql)
        self.db.get_connexion().commit()

        pokemons = self.db.get_cursor().fetchall()

        for pokemon in pokemons:
            for p in pokemon:
                print(p)


    def listTeam(self):
        sql = 'SELECT * FROM team'

        self.db.get_cursor().execute(sql)
        self.db.get_connexion().commit()

        pokemons = self.db.get_cursor().fetchone()

        for pokemon in pokemons:
            print("-", pokemon)


    def setTeam(self, pos, name):
        pos = int(pos)
        if pos == 1:
            sql = 'UPDATE team SET poke1 = ?'
        elif pos == 2:
            sql = 'UPDATE team SET poke2 = ?'
        elif pos == 3:
            sql = 'UPDATE team SET poke3 = ?'
        elif pos == 4:
            sql = 'UPDATE team SET poke4 = ?'
        elif pos == 5:
            sql = 'UPDATE team SET poke5 = ?'
        elif pos == 6:
            sql = 'UPDATE team SET poke6 = ?'
        else:
            print("Unknown position")
            return 1

        self.db.get_cursor().execute(sql, [name])
        self.db.get_connexion().commit()

        print(i18n.t("strings.parser.set"))


    def parse(self):
        if len(sys.argv) == 1:
            print(i18n.t("strings.usage.title"))
            print(" USAGE :")
            print("     -a <pokemon>                 ", i18n.t("strings.usage.add"))
            print("     -r <pokemon>                 ", i18n.t("strings.usage.remove"))
            print("     -l                           ", i18n.t("strings.usage.listAvaible"))
            print("     -t                           ", i18n.t("strings.usage.listTeam"))
            print("     -s <position> <pokemon>      ", i18n.t("strings.usage.setTeam"))         
        else:
            if sys.argv[1] == "-a":
                self.addPokemon(sys.argv[2])
            elif sys.argv[1] == "-r":
                self.removePokemon(sys.argv[2])
            elif sys.argv[1] == "-l":
                self.listPokemons()
            elif sys.argv[1] == "-t":
                self.listTeam()
            elif sys.argv[1] == "-s":
                self.setTeam(sys.argv[2], sys.argv[3])
            else:
                print(i18n.t("strings.OptionError"))