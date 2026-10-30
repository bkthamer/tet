from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from bd import get_db,moteurbd,SessionLocal,Base
from models import Tache

ipo = FastAPI(title="")


Base.metadata.create_all(bind=moteurbd)

@ipo.get("/")
def bien():
    return {'hello'}

@ipo.get("/listall")
def aff(db : Session = Depends(get_db)):
    return db.query(Tache).all()


@ipo.post("/lll")
def ajout(titre : str , description : str ="", db : Session = Depends(get_db)):
    tache = Tache(titre = titre, description = description)
    db.add(tache)
    db.commit()
    db.refresh(tache)
    return tache

@ipo.get("/hehghe/{id}")
def aff1 (idc : int , db : Session = Depends(get_db)):
   tache = db.query(Tache).filter(id == idc).first
   if tache is None:
       raise HTTPException(status_code=404)
   else :
       return tache


@ipo.delete("/hehe/{id}")
def del1 (idcc : int , db : Session = Depends(get_db)):
    tache = db.query(Tache).filter(id == idcc).first
    if tache is None:

        raise HTTPException(status_code=404)
 
    db.delete(tache)





