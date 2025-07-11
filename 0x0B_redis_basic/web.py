#!/usr/bin/env python3
"""
A module for implementing an expiring web cache and tracker.
"""

import redis
import requests
from typing import Callable
from functools import wraps

# Initialize a Redis client connection
redis_client = redis.Redis()


def cache_and_track(method: Callable) -> Callable:
    """
    Decorator that caches the output of a function with a 10-second
    expiration and tracks the number of calls for a given URL.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        The wrapper function for the decorator.
        """
        # Define the key for tracking the URL access count
        count_key = f"count:{url}"
        # Define the key for caching the result
        result_key = f"cached:{url}"

        # Increment the access count for the URL
        redis_client.incr(count_key)

        # Check if the result is already cached
        cached_result = redis_client.get(result_key)
        if cached_result:
            return cached_result.decode('utf-8')

            # If not cached, call the original function to get the result
        result = method(url)

        # Cache the result with an expiration of 10 seconds
        redis_client.setex(result_key, 10, result)

        return result

    return wrapper


@cache_and_track
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL using the requests module.
    This function is decorated to cache its output and track access count.

    Args:
        url: The URL to fetch.

    Returns:
        The HTML content of the page as a string.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"


if __name__ == "__main__":
    # Example usage:
    slow_url = (
        "http://slowwly.robertomurray.co.uk/delay/5000/url/"
        "http://www.google.com"
    )

    print(f"Fetching {slow_url}...")
    print(get_page(slow_url))
    print("\nFetching again (should be cached)...")
    print(get_page(slow_url))
