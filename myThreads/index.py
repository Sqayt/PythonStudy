import time
import asyncio


async def fun_1(x):
    print(x ** 2)
    await asyncio.sleep(3)
    print('fun_1 is completed')


async def fun_2(x):
    print(x ** 0.5)
    await asyncio.sleep(3)
    print('fun_2 is completed')


async def main():
    # task_1 = asyncio.create_task(fun_1(4))
    # task_2 = asyncio.create_task(fun_2(4))
    #
    # await task_1
    # await task_2

    loop = asyncio.get_event_loop()
    task_1 = loop.create_task(fun_1(4))
    task_2 = loop.create_task(fun_2(4))
    loop.run_until_complete(asyncio.wait([task_1, task_2]))


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print("%.2f" % (end_time - start_time), 'seconds')
