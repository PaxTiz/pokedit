#!/usr/bin/env python

from database import Database
from args import Args

if __name__ == "__main__":
    db = Database()
    db.connect(".config/pokedit/database.db")
    db.generate()

    args = Args(db)
    args.parse()
    
    db.get_connexion().close()
