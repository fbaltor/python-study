# many_get.py
# make a whole pile of api calls and store
# their response objects in a list.
# Using the homogeneous-session.

import asks
import curio

path_list = ['a', 'list', 'of', '1000', 'paths']

retrieved_responses = []

s = asks.Session('https://example.org/',
                  connections=20)

async def grabber(a_path):
    r = await s.get(path=a_path)
    retrieved_responses.append(r)

async def main(path_list):
    for path in path_list:
        curio.spawn(grabber(path))

curio.run(main(path_list))

