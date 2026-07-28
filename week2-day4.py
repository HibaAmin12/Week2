##SEQUENTIAL EXECUTION

# import time

# def task(name):
#     print(f"{name} started")
#     time.sleep(2)
#     print(f"{name} finished")


# start = time.time()

# task("Task 1")
# task("Task 2")
# task("Task 3")

# end = time.time()

# print(f"Total time: {end - start:.2f} seconds")

## Concurrency using Threading
# import time
# from concurrent.futures import ThreadPoolExecutor


# def task(name):
#     print(f"{name} started")
#     time.sleep(2)
#     print(f"{name} finished")


# start = time.time()

# with ThreadPoolExecutor(max_workers=2) as executor:
#     executor.map(
#         task,
#         ["Task 1", "Task 2", "Task 3"]
#     )


# end = time.time()

# print(f"Total time: {end - start:.2f} seconds")


## True Parallelism using Multiprocessing

# from concurrent.futures import ProcessPoolExecutor
# import time


# def cpu_task(n):
#     total = 0

#     for i in range(n):
#         total += i * i

#     return total


# numbers = [20_000_000, 20_000_000, 20_000_000]


# start = time.time()

# with ProcessPoolExecutor(max_workers=3) as executor:
#     results = executor.map(cpu_task, numbers)


# end = time.time()

# print(list(results))
# print(f"Time: {end-start:.2f} seconds")

##ASYNC IO
# import asyncio
# import time


# async def task(name):
#     print(f"{name} started")

#     await asyncio.sleep(2)

#     print(f"{name} finished")


# async def main():

#     start = time.time()

#     await asyncio.gather(
#         task("Task 1"),
#         task("Task 2"),
#         task("Task 3")
#     )

#     end = time.time()

#     print(f"Total time: {end-start:.2f} seconds")


# asyncio.run(main())


# import time
# from concurrent.futures import ThreadPoolExecutor


# def download_file(file):
#     start = time.time()

#     print(f"Downloading {file}...")

#     # Simulating file download (I/O waiting)
#     time.sleep(2)

#     print(f"{file} downloaded.")

#     end = time.time()

#     print(f"Time taken for {file}: {end - start:.2f} seconds")


# files = [
#     "file1.txt",
#     "file2.txt",
#     "file3.txt",
#     "file4.txt"
# ]


# # Overall execution start time
# overall_start = time.time()


# with ThreadPoolExecutor(max_workers=3) as executor:
    
#     # Run download_file concurrently on multiple threads
#     list(executor.map(download_file, files))


# # Overall execution end time
# overall_end = time.time()


# print("----------------------------")
# print(f"All files downloaded.")
# print(f"Total execution time: {overall_end - overall_start:.2f} seconds")


# import time
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# def cpu_task(n):
#     total = 0

#     for i in range(n):
#         total += i * i

#     return total


# numbers = [
#     20_000_000,
#     20_000_000,
#     20_000_000
# ]


# # -------------------------------
# # 1. Sequential Execution
# # -------------------------------

# start = time.time()

# for number in numbers:
#     cpu_task(number)

# end = time.time()

# print(f"Sequential time: {end-start:.2f} seconds")



# # -------------------------------
# # 2. ThreadPoolExecutor
# # -------------------------------

# start = time.time()

# with ThreadPoolExecutor(max_workers=3) as executor:
#     list(executor.map(cpu_task, numbers))

# end = time.time()

# print(f"Threading time: {end-start:.2f} seconds")



# # -------------------------------
# # 3. ProcessPoolExecutor
# # -------------------------------

# start = time.time()

# with ProcessPoolExecutor(max_workers=3) as executor:
#     list(executor.map(cpu_task, numbers))

# end = time.time()

# print(f"Multiprocessing time: {end-start:.2f} seconds")


# import time
# from concurrent.futures import ThreadPoolExecutor

# def download(file):
#     print(f"Downloading {file}...")
#     time.sleep(2)      # Simulating network waiting
#     print(f"{file} downloaded")

# files = ["A", "B", "C", "D"]

# # Sequential
# start = time.time()

# for file in files:
#     download(file)

# end = time.time()

# print(f"\nSequential Time: {end-start:.2f} seconds")


# # Threading
# start = time.time()

# with ThreadPoolExecutor(max_workers=4) as executor:
#     list(executor.map(download, files))

# end = time.time()

# print(f"Threading Time: {end-start:.2f} seconds")


# import asyncio

# async def work(name):
#     print(f"{name} Start")
#     await asyncio.sleep(2)
#     print(f"{name} End")

# async def main():
#     await asyncio.gather(
#         work("A"),
#         work("B"),
#         work("C")
#     )

# asyncio.run(main())

# import requests

# response = requests.get("https://api.github.com")

# print(response)
# print(response.status_code)

# print(response.headers)

# print(response.text)

# print(response.json())

# import requests

# response = requests.get("https://api.github.com")

# data = response.json()

# print(data["current_user_url"])


# import requests

# response = requests.get("https://api.github.com")

# if response.status_code == 200:

#     data = response.json()

#     print(data["current_user_url"])

# else:

#     print("Request Failed")

import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("Current User URL:", data["current_user_url"])
    print("Current User Authorizations URL:", data["authorizations_url"])
    print("Repository URL:", data["repository_url"])
    print("Rate Limit URL:", data["rate_limit_url"])
else:
    print("Request Failed!")
