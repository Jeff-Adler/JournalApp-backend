from fastapi import FastAPI

fake_notes_db = ["note_1", "note_2", "note_3"]

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