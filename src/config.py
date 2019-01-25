import locale
import i18n

loc = locale.getlocale()
loc = str(loc[0])
loc = loc.split("_")

i18n.load_path.append("/usr/share/pokedit/")
i18n.set('locale', loc[0])
i18n.set('fallback', 'en')

TYPES = {
    "acier": "steel",
    "combat": "fight",
    "dragon": "dragon",
    "eau": "water",
    "électrik": "electrik",
    "fée": "fairy",
    "feu": "fire",
    "glace": "ice",
    "insecte": "bug",
    "normal": "normal",
    "plante": "grass",
    "poison": "poison",
    "psy": "psychic",
    "roche": "rock",
    "sol": "ground",
    "spectre": "ghost",
    "ténèbres": "dark",
    "vol": "flying"
}