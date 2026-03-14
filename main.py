from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove
from PIL import Image
import io

app = FastAPI()

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    contents = await file.read()
    input_img = Image.open(io.BytesIO(contents))
    output_img = remove(input_img)
    
    buf = io.BytesIO()
    output_img.save(buf, format="PNG")
    
    return Response(
        content=buf.getvalue(),
        media_type="image/png"
    )