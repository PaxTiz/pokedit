import sqlite3
import os

class Database():
    def create_table_pokemons(self):
        self.cursor.execute("""
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

    def create_table_attacks(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS attacks (                                    
                id INTEGER PRIMARY KEY AUTOINCREMENT,                               
                name VARCHAR(255) NOT NULL,                                         
                power INTEGER NOT NULL,                                             
                pokemon_id INTEGER,                                                 
                FOREIGN KEY(pokemon_id) REFERENCES pokemon(id)                      
            ) 
        """)

    def create_table_team(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS team(
                poke1 VARCHAR(255) DEFAULT NULL,
                poke2 VARCHAR(255) DEFAULT NULL,
                poke3 VARCHAR(255) DEFAULT NULL,
                poke4 VARCHAR(255) DEFAULT NULL,
                poke5 VARCHAR(255) DEFAULT NULL,
                poke6 VARCHAR(255) DEFAULT NULL
            )
        """)

    def create_table_pokedex(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokedex (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_fr VARCHAR(255) NOT NULL,
                name_en VARCHAR(255) NOT NULL,
                generation INTEGER NOT NULL
            )
        """)

    def create_table_natures(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS natures(
                id INTEGER PRIMARY KEY AUTOINCREMENT,                               
                name_fr VARCHAR(255) NOT NULL,
                name_en VARCHAR(255) NOT NULL
            )
        """)

    def create_table_nat_pokemon(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS nat_poke (
                id_poke INTEGER NOT NULL,
                id_nat INTEGER NOT NULL,
                FOREIGN KEY(id_poke) REFERENCES pokedex(id),
                FOREIGN KEY(id_nat) REFERENCES natures(id)
            )
        """)

    def insert_datas(self):
        self.cursor.execute("""
            INSERT INTO team(poke1, poke2, poke3, poke4, poke5, poke6) VALUES (" ", " ", " ", " ", " ", " ")
        """)

        self.cursor.execute("""
            INSERT INTO natures(name_fr, name_en) VALUES
                ("acier", "steel"),
                ("combat", "fight"),
                ("dragon", "dragon"),
                ("eau", "water"),
                ("électrik", "electrik"),
                ("fée", "fairy"),
                ("feu", "fire"),
                ("glace", "ice"),
                ("insecte", "bug"),
                ("normal", "normal"),
                ("plante", "grass"),
                ("poison", "poison"),
                ("psy", "psychic"),
                ("roche", "rock"),
                ("sol", "ground"),
                ("spectre", "ghost"),
                ("ténèbres", "dark"),
                ("vol", "flying")
        """)

    def connect(self, way):
        try:
            u = os.path.expanduser("~")
            path = u + "/" + way
            self.connexion = sqlite3.connect(path)
            self.cursor = self.connexion.cursor()
        except Exception as e:
            print(i18n.t("strings.DatabaseError"))
            raise e

    def get_connexion(self):
        return self.connexion

    def get_cursor(self):
        return self.cursor

    def generate(self):
        self.create_table_pokedex()
        self.create_table_pokemons()
        self.create_table_team()
        self.create_table_attacks()
        self.create_table_natures()
        self.create_table_nat_pokemon()

        self.insert_datas()

        self.connexion.commit()
