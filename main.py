from fastapi import FastAPI
from pydantic import BaseModel

fake_notes_db = ["note_1", "note_2", "note_3"]

class Note(BaseModel):
	contents: str

app = FastAPI()

@app.get("/")
async def root():
	return {"message" : "Welcome to the Journal App!"}

@app.get("/notes")
async def get_notes():
	return {"notes": (' ').join(fake_notes_db)}

@app.get("/notes/{note_id}")
async def get_note_by_id(note_id: int):
	if note_id > len(fake_notes_db) - 1 or note_id < 0:
		return {"error" : "note_id out of bounds"}
	return {note_id: fake_notes_db[note_id]}

@app.post("/notes")
async def create_note(note: Note):
	fake_notes_db.append(note.contents)	
	return note.contents