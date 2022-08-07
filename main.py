from fastapi import FastAPI

SAMPLE_NOTES = ["note_1", "note_2", "note_3", "note_4", "note_5"]

app = FastAPI()

@app.get("/")
async def root():
	return {"message" : "Welcome to the Journal App!"}

@app.get("/")
async def get_notes():
	return {"notes": "populate this with notes"}

@app.get("/")
async def get_notes():
	return {"notes": "populate this with notes"}	