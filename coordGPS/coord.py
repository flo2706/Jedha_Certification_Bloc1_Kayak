import aiohttp
import asyncio
import json
import logging
from typing import Tuple, Dict, Union
import os

# Configuration 
BASE_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(BASE_DIR, "cities.json")

OUTPUT_FILE = "coordinates.json"
HEADERS = {
    "User-Agent": os.getenv("USER_AGENT", "MyScript/1.0 (your_email@example.com)")
}
MAX_CONCURRENT_REQUESTS = 5  # Limit concurrent requests
RETRIES = 3  # Number of attempts per request

# Logger Setup 
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Main function to fetch coordinates 
async def get_coordinates(session: aiohttp.ClientSession, city: str, semaphore: asyncio.Semaphore) -> Tuple[str, Dict[str, Union[str, None]]]:
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}

    async with semaphore:
        for attempt in range(RETRIES):
            try:
                async with session.get(url, params=params, headers=HEADERS) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data:
                            return city, {"latitude": data[0]["lat"], "longitude": data[0]["lon"]}
                        else:
                            return city, {"latitude": None, "longitude": None}
                    elif response.status == 429:
                        retry_after = int(response.headers.get("Retry-After", 5))
                        logger.warning(f"{city} - Too many requests. Waiting {retry_after} seconds.")
                        await asyncio.sleep(retry_after)
                    else:
                        return city, {"error": f"HTTP Error {response.status}"}
            except Exception as e:
                logger.error(f"{city} - Exception: {e}")
                await asyncio.sleep(1)  # Small delay before retrying

    return city, {"error": "Failed after multiple attempts"}

# Load cities from a JSON file 
def load_cities(filepath: str) -> list:
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Save results to a JSON file 
def save_results(filepath: str, data: dict):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    logger.info(f"\nData saved to {filepath}")

# Main routine to process all cities
async def fetch_all_coordinates(cities: list[str]) -> dict:
    results = {}
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    async with aiohttp.ClientSession() as session:
        tasks = [get_coordinates(session, city, semaphore) for city in cities]
        for future in asyncio.as_completed(tasks):
            city, coords = await future
            results[city] = coords
            logger.info(f"{city} → {coords}")
    return results

# Entry point 
async def main():
    cities = load_cities(INPUT_FILE)
    coordinates = await fetch_all_coordinates(cities)
    save_results(OUTPUT_FILE, coordinates)

if __name__ == "__main__":
    asyncio.run(main())
