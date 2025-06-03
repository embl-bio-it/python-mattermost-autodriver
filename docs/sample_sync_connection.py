from mattermostautodriver import TypedDriver
from multiprocessing import Process
import time


async def my_event_handler(message):
    print(repr(message))


class Handler:
    def __init__(self):
        self.driver = TypedDriver({
            "url": "127.0.0.1",
            "token": "e691u15hajdebcnqpfdceqihcc",
            "scheme": 'http',
            "port": 8065,
            "verify": False,
            # "debug": True,
        })

    def login(self):
        print(">>> Login:", self.driver.login())

    def main(self):
        self.driver.init_websocket(my_event_handler)

    def requests(self):
        print(">>> Get Admin:", self.driver.users.get_user_by_username('admin'))

        print(">>> Get my own details:", self.driver.users.get_user(user_id='me'))

        print(">>> Get all teams:", self.driver.teams.get_all_teams())


def main(handler):
    handler.main()



handler = Handler()

handler.login()

p = Process(target=main, args=(handler,))
p.start()

handler.requests()

print("Websocket connected, closing main thread in 5 seconds")
time.sleep(5)
print("Disconnecting")

# Use `disconnect()` to disconnect the websocket
handler.driver.disconnect()

# Shutdown the handler process as gracefully as possible
# After disconnect the socket will eventually close bit needs to receive
# an event from the Mattermost server as the driver blocks listening for events

for signal in (p.terminate, p.kill):
    p.join(timeout=5)

    if p.is_alive():
        signal()
    else:
        break

p.close()

print("Disconnected")
