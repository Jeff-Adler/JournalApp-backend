import logging
from fastapi import FastAPI
from pydantic import BaseModel

fake_notes_db = ["note_1", "note_2", "note_3"]

class Note(BaseModel):
	contents: str

# helper functions
def is_id_out_of_bounds(some_id: int, some_list: list) -> bool:
	return some_id > len(some_list) - 1 or some_id < 0

log = logging.getLogger("JournalApi")

app = FastAPI()

@app.get("/")
async def root():
	log.info("gar")
	return {"message" : "Welcome to the Journal App!"}

@app.get("/notes")
async def get_notes():
	return {"notes": (' ').join(fake_notes_db)}

@app.get("/notes/{note_id}")
async def get_note_by_id(note_id: int):
	log.info("gar")
	if is_id_out_of_bounds(note_id, fake_notes_db):
		return {"error" : "note_id out of bounds"}
	return {note_id: fake_notes_db[note_id]}

@app.post("/notes")
async def create_note(note: Note):
	fake_notes_db.append(note.contents)	
	return note.contents

# @app.delete("/notes/{note_id}")
# async def delete_note_by_id(note_id: int):
# 	if is_id_in_bounds(note_id, fake_notes_db):