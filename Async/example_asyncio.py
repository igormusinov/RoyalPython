import asyncio

async def hear():
	while True:
		print("....")
		await asyncio.sleep(1)

async def say():
	while True:
		print("Hello im Peter")
		await asyncio.sleep(3)

async def main():
	e_list = [asyncio.create_task(hear()), asyncio.create_task(say())]
	while True:
		t = e_list.pop(0)
		await asyncio.gather(t)
		e_list.append(t)

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
	loop.close()
