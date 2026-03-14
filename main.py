from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def root():
    return {"status": "rembg API aktif"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    contents = await file.read()
    input_image = Image.open(io.BytesIO(contents))
    output_image = remove(input_image)
    
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")