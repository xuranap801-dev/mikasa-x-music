from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client("MikasaAss1", api_id=config.API_ID, api_hash=config.API_HASH,
                          session_string=config.STRING1, no_updates=True)
        self.two = Client("MikasaAss2", api_id=config.API_ID, api_hash=config.API_HASH,
                          session_string=config.STRING2, no_updates=True)
        self.three = Client("MikasaAss3", api_id=config.API_ID, api_hash=config.API_HASH,
                            session_string=config.STRING3, no_updates=True)
        self.four = Client("MikasaAss4", api_id=config.API_ID, api_hash=config.API_HASH,
                           session_string=config.STRING4, no_updates=True)
        self.five = Client("MikasaAss5", api_id=config.API_ID, api_hash=config.API_HASH,
                           session_string=config.STRING5, no_updates=True)

    async def _start_assistant(self, client, number, label):
        await client.start()
        assistants.append(number)
        client.id = client.me.id
        client.name = client.me.mention
        client.username = client.me.username
        assistantids.append(client.id)
        if config.LOG_GROUP_ID:
            try:
                await client.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except Exception as exc:
                LOGGER(__name__).warning(
                    f"{label} could not write to LOG_GROUP_ID; continuing without log notification: {exc}"
                )
        LOGGER(__name__).info(f"{label} started as {client.name}")

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")
        clients = (
            (self.one, config.STRING1, 1, "Assistant 1"),
            (self.two, config.STRING2, 2, "Assistant 2"),
            (self.three, config.STRING3, 3, "Assistant 3"),
            (self.four, config.STRING4, 4, "Assistant 4"),
            (self.five, config.STRING5, 5, "Assistant 5"),
        )
        for client, session, number, label in clients:
            if session:
                await self._start_assistant(client, number, label)

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        for client, session in (
            (self.one, config.STRING1),
            (self.two, config.STRING2),
            (self.three, config.STRING3),
            (self.four, config.STRING4),
            (self.five, config.STRING5),
        ):
            if session:
                try:
                    await client.stop()
                except Exception:
                    pass
