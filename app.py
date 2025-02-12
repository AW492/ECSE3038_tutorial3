from fastapi import FastAPI, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field,ValidationError
from fastapi.responses import JSONResponse
from datetime import datetime
from uuid import UUID, uuid4

app = FastAPI()

Fruit_data = []

class Fruit(BaseModel):
	id: UUID = Field(default_factory=uuid4)
	name: str
	variety: str
	quantity: int
	supplier: str
	harvest_date: datetime
	creation_date: datetime = datetime.now()
	available: bool = True
	price: float

class Fruit_Update(BaseModel):
	quantity: int | None = None 
	available: bool | None = None 
	price: float | None = None 
   
	
@app.get("/api/fruits")
async def get_all_fruits():
	fruits_available = []
	for fruit_info in Fruit_data:
		if fruit_info.available == True:
			fruits_available.append(fruit_info)
	return fruits_available

@app.get("/api/fruits/{id}")
async def get_one_fruit(id: UUID):
	for fruit_info in Fruit_data:
		if fruit_info.id == id:
			return fruit_info
		else:
			raise HTTPException(status_code = 404, detail = "Fruit is not found")
	
@app.post("/api/fruits")
async def add_new_fruit(fruit_request:Fruit):
	if fruit_request.name and fruit_request.variety and fruit_request.quantity and fruit_request.supplier and fruit_request.harvest_date and fruit_request.price:
		Fruit_data.append(fruit_request)
		
	else:
		raise HTTPException(status_code=400, detail = "Missing required fields")
	
	fruit_json = jsonable_encoder(fruit_request)
	return JSONResponse(fruit_json, status_code=201)

@app.patch("/api/fruits/{id}")
async def update_fruit(id:UUID, fruit_update:Fruit_Update):
	for i,fruit_info in enumerate(Fruit_data):
		if fruit_info.id == id:
			fruit_update_dict = fruit_update.model_dump(exclude_unset=True)
			try:
				update_fruit = fruit_info.copy(update=fruit_update_dict)
				Fruit_data[i] = fruit_info.model_validate(update_fruit)
				json_updated_person = jsonable_encoder(update_fruit)
				return JSONResponse(json_updated_person,status_code=200)
			except ValidationError:
				raise HTTPException(status_code=400,detail="Fruit must be available , have a quantity and a price ")
	raise HTTPException(status_code=404, detail="Fruit not found")

@app.delete("/api/fruits/{id}")
async def delete_fruit(id: UUID):
	for fruit_info in Fruit_data:
		if fruit_info.id == id:
			fruit_info.available == False
			return Response(status_code=204)
	raise HTTPException(status_code=404, detail = "Fruit not found")
		