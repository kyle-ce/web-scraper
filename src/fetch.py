import asyncio
import aiohttp


async def fetch_all_requests(urls):
    async with aiohttp.ClientSession() as session:
        data = await fetch_all_pages(session, urls)
        return data


async def fetch_all_pages(session, urls):
    task_list = []
    for url in urls:
        print(f"{url} sent")
        task = asyncio.create_task(fetch_page(session, url))
        task_list.append(task)

        # * packs excess positional arguments into a tuple
    results = await asyncio.gather(*task_list)
    print(f"results received: {len(results)}")
    return results


async def fetch_page(session, url):
    try:
        async with session.get(url) as response:
            return await response.read()
    except aiohttp.client_exceptions.ClientConnectorError as err:
        print("Server not responding: resending request...")
        fetch_page(session, url)
