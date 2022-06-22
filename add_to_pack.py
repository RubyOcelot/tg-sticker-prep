import pathlib
import time
import argparse
from telethon import TelegramClient

lines=[]
with open('./api_hash.txt') as f:
    lines = f.read().splitlines()

api_id=int(lines[0])
api_hash=lines[1]
client = TelegramClient('anon', api_id, api_hash)


parser = argparse.ArgumentParser()
parser.add_argument('sticker_location')
parser.add_argument('sticker_name')

args = parser.parse_args()


async def create_sticker():
    await client.send_message('@Stickers', '/addsticker')
    time.sleep(1)
    await client.send_message('@Stickers', args.sticker_name)
    time.sleep(1)

    sticker_location = pathlib.Path(args.sticker_location)

    for sticker in sticker_location.glob('*.png'):
        print(sticker)
        await client.send_file('@Stickers', str(sticker), force_document=True)
        time.sleep(1)
        await client.send_message('@Stickers', '😀')
        time.sleep(1)

    for sticker in sticker_location.glob('*.webp'):
        print(sticker)
        await client.send_file('@Stickers', str(sticker), force_document=True)
        time.sleep(1)
        await client.send_message('@Stickers', '😀')
        time.sleep(1)

    await client.send_message('@Stickers', '/done')


with client:
    client.loop.run_until_complete(create_sticker())
