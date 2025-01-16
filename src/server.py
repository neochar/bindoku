import json

import pika
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pika.credentials import PlainCredentials
from starlette.requests import Request

from game.generator import Generator
from game.puzzler import Puzzler
from game.solver import Solver
from game.validator import Validator

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/get-board/{sidelen}")
def get_board(sidelen: int, seed: int = 1, prepare: bool = False):
    validator = Validator()
    solver = Solver(validator=validator)
    generator = Generator(validator=validator, seed=seed)
    field = generator.generate(sidelen)
    generator.set_puzzleizer(Puzzler(solver=solver))
    puzzle = generator.puzzleize()

    return {
        'field': _prepare_for_app(field) if prepare else field,
        'puzzle': _prepare_for_app(puzzle) if prepare else puzzle,
    }


@app.post("/api/send-event")
async def send_event(request: Request):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='10.100.0.1',
            port=45672,
            credentials=PlainCredentials(
                'admin',
                'admin'
            )
        )
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='events')

    message = await request.json()

    channel.basic_publish(exchange='', routing_key='events', body=json.dumps(message))

    connection.close()

    return 200


def _prepare_for_app(field: list[list[int or None]]) -> list[list[int or None]]:
    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col == 0:
                field[y][x] = None
            else:
                field[y][x] = col - 1

    return field
