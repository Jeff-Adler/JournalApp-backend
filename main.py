import logging
from fastapi import FastAPI
from pydantic import BaseModel

# declare logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug("TESTING LOGGER")

fake_notes_db = ["note_1", "note_2", "note_3", "note_4", "note_5", "note_6", "note_7", "note_8", "note_9", "note_10"]

# Models: used to define request bodies
class Note(BaseModel):
	contents: str

# helper functions
def index_is_out_of_bounds(index: int, list: list) -> bool:
	return index > len(list) - 1 or index < 0

app = FastAPI()

@app.get("/")
async def root():
	return {"message" : "Welcome to the Journal App!"}

@app.get("/notes")
async def get_notes(skip: int = 0, limit: int = 3):
	if index_is_out_of_bounds(skip, fake_notes_db):
		return {"error" : "note_id out of bounds"}
	i = skip
	j = skip + limit if skip + limit < len(fake_notes_db) else len(fake_notes_db) - 1
	note_collection = ""
	for note in fake_notes_db[i:j]:
    	note_collection += note
	return {"notes": note_collection}

@app.get("/notes/{note_id}")
async def get_note_by_id(note_id: int):
	if index_is_out_of_bounds(note_id, fake_notes_db):
		return {"error" : "note_id out of bounds"}
	return {note_id: fake_notes_db[note_id]}

@app.post("/notes")
async def create_note(note: Note):
	fake_notes_db.append(note.contents)	
	return note.contents

@app.delete("/notes/{note_id}")
async def delete_note_by_id(note_id: int):
	if index_is_out_of_bounds(note_id, fake_notes_db):
		return {"error" : "note_id out of bounds"}
	return fake_notes_db.pop(note_id)

@app.patch("/notes/{note_id}")
async def patch_note(note_id: int, note: Note):
	if index_is_out_of_bounds(note_id, fake_notes_db):
		return {"error" : "note_id out of bounds"}
	fake_notes_db[note_id] = note.contents
	return fake_notes_db[note_id]





