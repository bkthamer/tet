from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from bd import Base, moteurbd, get_db
from models import Tache

ipo = FastAPI(title="API de gestion des tâches")

Base.metadata.create_all(bind=moteurbd)


@ipo.get("/")
def accueil():
    return {"message": "Bienvenue dans mon API FastAPI"}


@ipo.get("/taches")
def lister_taches(db: Session = Depends(get_db)):
    return db.query(Tache).all()


@ipo.post("/taches")
def creer_tache(
    titre: str,
    description: str = "",
    db: Session = Depends(get_db)
):
    tache = Tache(titre=titre, description=description)
    db.add(tache)
    db.commit()
    db.refresh(tache)
    return tache


@ipo.get("/taches/{tache_id}")
def obtenir_tache(
    tache_id: int,
    db: Session = Depends(get_db)
):
    tache = db.query(Tache).filter(Tache.id == tache_id).first

    if tache is None:
        raise HTTPException(status_code=404, detail="Tâche introuvable")

    return tache


@ipo.delete("/taches/{tache_id}")
def supprimer_tache(
    tache_id: int,
    db: Session = Depends(get_db)
):
    tache = db.query(Tache).filter(Tache.id == tache_id).first()

    if tache is None:
        raise HTTPException(status_code=404, detail="Tâche introuvable")

    db.delete(tache)
    db.commit()

    return {"message": "Tâche supprimée"}