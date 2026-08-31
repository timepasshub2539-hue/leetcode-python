from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(10) as ex:
    ex.map(download, urls)
