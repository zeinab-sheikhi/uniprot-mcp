import asyncio
import json
import logging
from pathlib import Path


from uniprot_mcp.tools.search_uniprot import search_uniprot

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def main():
    """
    Main function to run a test search against the UniProt API.
    """
    query = "insulin"
    output_filename = "uniprot_insulin_results.json"
    output_path = Path(output_filename)

    print(f"--> Searching UniProt with query: '{query}'")

    try:
        # Call the async search function
        results_json_str = await search_uniprot(query=query, size=1)        
        parsed_data = json.loads(results_json_str)

        with output_path.open("w", encoding="utf-8") as f:
            json.dump(parsed_data, f, indent=2, ensure_ascii=False)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    # In Python 3.7+, asyncio.run() is the standard way to run an async main function.
    asyncio.run(main())
