#!/usr/bin/env python


def save(obj, db):
    # adds a valid instance to the session
    try:
        db.session.add(obj)
        db.session.commit()
        return True
    except Exception:
        db.session.rollback()
        return False
