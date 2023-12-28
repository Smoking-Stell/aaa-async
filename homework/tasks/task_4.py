import asyncio


async def task_1(i: int, cur: str):
    cur = cur + '1'
    if i == 0:
        return cur

    if i > 5:
        return await task_2(i // 2, cur)
    else:
        return await task_2(i - 1, cur)


async def task_2(i: int, cur: str):
    cur = cur + '2'
    if i == 0:
        return cur

    if i % 2 == 0:
        return await task_1(i // 2, cur)
    else:
        return await task_2(i - 1, cur)


async def coroutines_execution_order(i: int = 42) -> int:
    # Отследите порядок исполнения корутин при i = 42 и верните число, соответствующее ему.
    #
    # Когда поток управления входит в task_1 добавьте к результату цифру 1, а когда он входит в task_2,
    # добавьте цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212
    result = await task_1(i, '')

    return int(result)


answer_cons = asyncio.run(coroutines_execution_order())
print(answer_cons)
