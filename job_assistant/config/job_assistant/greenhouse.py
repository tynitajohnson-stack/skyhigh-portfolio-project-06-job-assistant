
import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from job_assistant.models import JobListing


def fetch_greenhouse_jobs(source):
    """Fetch listings from a configured public Greenhouse board."""
    token = source["board_token"]
    company = source["company"]
    url = (
        "https://boards-api.greenhouse.io/v1/boards/"
        f"{token}/jobs?content=true"
    )

    try:
        with urlopen(url, timeout=15) as response:
            data = json.load(response)
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        print(f"Greenhouse source unavailable ({company}): {exc}")
        return []

    jobs = []

    for item in data.get("jobs", []):
        jobs.append(
            JobListing(
                title=item.get("title", ""),
                company=company,
                location=item.get("location", {}).get("name", ""),
                url=item.get("absolute_url", ""),
                description=item.get("content", ""),
                posted_date=item.get("updated_at", ""),
                source=source["name"],
            )
        )

    return jobs
