from mattermostautodriver import AsyncTypedDriver
import asyncio


async def my_event_handler(message):
    print(repr(message))


class Handler:
    def __init__(self):
        self.driver = AsyncTypedDriver({
            "url": "127.0.0.1",
            "token": "e691u15hajdebcnqpfdceqihcc",
            "scheme": 'http',
            "port": 8065,
            "verify": False,
            # "debug": True,
        })

    async def amain(self):
        print(">>> Login:", await self.driver.login())

        task = asyncio.create_task(self.driver.init_websocket(my_event_handler))

        print(">>> Get Admin:", await self.driver.users.get_user_by_username('admin'))

        print(">>> Get my own details:", await self.driver.users.get_user(user_id='me'))

        print(">>> Get all teams:", await self.driver.teams.get_all_teams())

        print("Websocket connected, closing main thread in 5 seconds")
        await asyncio.sleep(5)
        print("Disconnecting")

        self.driver.disconnect()

        # Will disconnect as soon as a message is sent by the Mattermost server
        # which can be a rather long time on a mostly inactive server
        # await task
        # alternatively use:
        task.cancel()


handler = Handler()

asyncio.run(handler.amain())

print("Disconnected")
