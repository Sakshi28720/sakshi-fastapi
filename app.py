from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse 
from PIL import Image
import io
import base64
from main import segment_everything

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Image to BW Converter</title>
    </head>
    <body>
        <form action="/uploadfile/" enctype="multipart/form-data" method="post">
            <input name="file" type="file">
            <input type="submit">
        </form>
    </body>
</html>   
"""

@app.get("/")
async def main():
    return HTMLResponse(html)

@app.post("/uploadfile/")
async def convert_image(file: UploadFile = File(...)):
    contents = await file.read()
    
    pil_img = Image.open(io.BytesIO(contents))
    segmentation_result = segment_everything(pil_img)
    
    bw_bytes = io.BytesIO()
    segmentation_result.save(bw_bytes, format='PNG')

    html = "<h1> Original Image </h1> <br>"
    html += f'<img src="data:image/png;base64,{base64.b64encode(contents).decode("ascii")}">' 
    html += "<h1> Segmented Image </h1> <br>"  
    html += f'<img src="data:image/png;base64,{base64.b64encode(bw_bytes.getvalue()).decode("ascii")}">'

    return HTMLResponse(html)

   
