from sanic import Sanic
from sanic.response import *
import ujson

app=Sanic(__name__)

@app.websocket("/ws")
async def websocket(request, ws):
    while True:
        msg=await ws.recv()
        data=ujson.loads(msg)
        if data["type"] == "captcha:
            rjson={
                "type": "captcha",
                "userid": data["userid"],
                "guildid": data["guildid"]
            }
            await ws.send(rjson)
