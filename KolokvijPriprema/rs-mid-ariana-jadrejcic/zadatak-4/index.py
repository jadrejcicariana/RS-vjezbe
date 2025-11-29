import asyncio
from datetime import datetime
import random
from collections import defaultdict

async def get_camera_data(camera_id: int) -> dict:
    await asyncio.sleep(0.5)
    await asyncio.sleep(random.uniform(0.1, 5))
    rez = {
        "camera_id" : {camera_id},
        "timestamp" : datetime.now().isoformat(),
        "vehicle_count" : random.randint(5, 20)
    }
    return rez


async def main():
    vozila = defaultdict(list)
    
    for ciklus in range(1, 7):
        tasks = [asyncio.create_task(get_camera_data(i)) for i in range(1, 6)]

        rez = []

        for i, task in enumerate(tasks, 1):
            try:
                rez_kamera = await asyncio.wait_for(task, timeout = 3)
                rez.append(rez_kamera)
                vozila[i].append(rez_kamera["vehicle_count"])
            except asyncio.TimeoutError:
                print(f"Upozorenje: Dohvat podataka s kamere {i} je istekao.")

        timestamps = [datetime.fromisoformat(r["timestamp"]) for r in rez]
        prva = timestamps.index(min(timestamps))
        zadnja = timestamps.index(max(timestamps))

        print(f"Ciklus {ciklus}")
        print(f"Prva kamera: {rez[prva]['camera_id']} ({rez[prva]['timestamp']})")
        print(f"Posljednja kamera: {rez[zadnja]['camera_id']} ({rez[zadnja]['timestamp']})")
        print(f"Ukupan broj vozila: {sum(x['vehicle_count'] for x in rez)}\n")

    print("Prosječan broj vozila po kameri:")
    for kamera_id, counts in vozila.items():
        prosjek = sum(counts) / len(counts)
        print(f"Kamera {kamera_id}: {prosjek:.2f}")

asyncio.run(main())