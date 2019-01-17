import sqlite3
import os
import locale
import i18n

loc = locale.getlocale()
loc = str(loc[0])
loc = loc.split("_")

i18n.load_path.append("/usr/share/pokedit/")
i18n.set('locale', loc[0])
i18n.set('fallback', 'en')

try:
    u = os.path.expanduser("~")
    path = u + "/.config/pokedit/database.db"
    connexion = sqlite3.connect(path)
    cursor = connexion.cursor()
except Exception as e:
    print(i18n.t("strings.DatabaseError"))
    raise e