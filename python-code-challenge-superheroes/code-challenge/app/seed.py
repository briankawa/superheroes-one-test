from app import app, db
from models import Hero


def see_heroes():
    with app.app_context():
        db.session.add(Hero(name="Clark Kent", super_name="Superman"))
        db.session.add(Hero(name="Doreen Green", super_name="Squirrel Girl"))
        db.session.add(Hero(name="Gwen Stacy", super_name="Spider-Gwen"))
        db.session.add(Hero(name="Janet Van Dyne", super_name="The Wasp"))
        db.session.add(Hero(name="Wanda Maximoff", super_name="Scarlet Witch"))
        db.session.add(Hero(name="Carol Danvers", super_name="Captain Marvel"))
        db.session.add(Hero(name="Jean Grey", super_name="Dark Phoenix"))
        db.session.add(Hero(name="Ororo Munroe", super_name="Storm"))
        db.session.add(Hero(name="Kitty Pryde", super_name="Shadowcat"))
        db.session.add(Hero(name="Elektra Natchios", super_name="Elektra"))
        db.session.commit()
    
    
# see_heroes()