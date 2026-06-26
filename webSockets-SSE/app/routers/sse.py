from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

import asyncio
from datetime import datetime

router = APIRouter()


@router.get("/events")
async def stream_events():

    async def event_generator():

        while True:

            current_time = datetime.now().strftime("%H:%M:%S")

            yield {
                "data": f"Current Time: {current_time}"
            }

            await asyncio.sleep(1)

    return EventSourceResponse(event_generator())