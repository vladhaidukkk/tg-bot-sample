from typing import Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class CounterMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, any]], Awaitable[any]],
        event: TelegramObject,
        data: dict[str, any],
    ) -> any:
        self.counter += 1
        data["counter"] = self.counter

        print(f"Before handler #{self.counter}")
        result = await handler(event, data)
        print(f"After handler #{self.counter}")

        return result
