import config
import i18n

def addPokemon(name):
    params = (name, 0, "null", "null", "null", "null")
    sql = 'INSERT INTO pokemons(name, level, type1, type2, nature, special_capacity) VALUES (?, ?, ?, ?, ?, ?)'
    
    config.cursor.execute(sql, params)
    config.connexion.commit()

    print(name, i18n.t("strings.parser.add"))

def removePokemon(name):
    sql = 'DELETE FROM pokemons WHERE name = ?'
    config.cursor.execute(sql, [name])
    config.connexion.commit()

    print(name, i18n.t("strings.parser.remove"))

def listPokemons():
    sql = 'SELECT name FROM pokemons'

    config.cursor.execute(sql)
    config.connexion.commit()

    pokemons = config.cursor.fetchall()

    for pokemon in pokemons:
        for p in pokemon:
            print(p)

def listTeam():
    sql = 'SELECT * FROM team'

    config.cursor.execute(sql)
    config.connexion.commit()

    pokemons = config.cursor.fetchone()

    for pokemon in pokemons:
        print("-", pokemon)

def setTeam(pos, name):
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

    config.cursor.execute(sql, [name])
    config.connexion.commit()

    print(i18n.t("strings.parser.set"))