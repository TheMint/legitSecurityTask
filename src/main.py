from fastapi import FastAPI, Request
import json

app = FastAPI()


@app.post("/")
async def handle_post_request(request: Request):
    data = await request.json()
    # Process the received data here
    print(data)
    return {"message": "Data received successfully"}


@app.post("/github-event")
async def handle_github_event(request: Request):
    data = await request.json()
    # Process the received data here
    print(json.dumps(data, indent=4))
    return {"message": "Data received successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000)
