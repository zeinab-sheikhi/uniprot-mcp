import json
import logging
from typing import Any, Dict, List

from uniprot_mcp.tools.models import UniProtSearchResponse
from uniprot_mcp.utils.http import request_api, RequestError

BASE_URL = "https://rest.uniprot.org/uniprotkb"
logger = logging.getLogger(__name__)


async def search_uniprot(
    query: str,
    fields: List[str] | None = None,
    sort: str | None = None,
    include_isoform: bool | None = None,
    size: int | None = 1,
) -> str:
    """
    Search UniProtKB for protein entries matching the specified query and parameters.

    Args:
        query: Search criteria for UniProtKB entries.
        fields: Optional list of fields to include in the response.
        sort: Optional sort order for results.
        include_isoform: Whether to include isoform data.
        size: Number of results to return.

    Returns:
        JSON string of results or an error dictionary.
    """

    url = f"{BASE_URL}/search"
    params = {
        "query": query,
        "size": size,
    }

    if fields:
        params["fields"] = ",".join(fields)

    if include_isoform is not None:
        params["includeIsoform"] = str(include_isoform).lower()
    
    parsed_data: Dict[str, Any] | None
    error_obj: RequestError | None

    parsed_data, error_obj = await request_api(
        url=url,
        method="GET",
        response_model_type=UniProtSearchResponse,
        request=params,
    )

    logger.info(f"Parsed data: {parsed_data}")

    data_to_return: Dict[str, Any]

    if error_obj:
        logger.error(f"Error: {error_obj.message}")
        data_to_return = {
            "error": f"API Error {error_obj.code}",
            "details": error_obj.message,
        }
    elif parsed_data:
        data_to_return = {
            "results": [entry.model_dump_json(exclude_none=True) for entry in parsed_data.results],
        }
    else:
        data_to_return = {
            "error": "No results found",
        }
    
    return json.dumps(data_to_return)
