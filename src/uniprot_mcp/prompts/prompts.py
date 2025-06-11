from typing import Dict, List

from mcp.types import Prompt, PromptArgument, GetPromptResult, TextContent


PROMPTS = {
    "search_uniprot": Prompt(
        name="search_uniprot",
        description="Search Uniprot for a protein or a gene",
        arguments=[
            PromptArgument(name="protein_name", description="The name of the protein", required=True),
        ],
    ),
}


async def list_prompts() -> List[Prompt]:
    return [PROMPTS["protein_analysis"]] if "search_uniprot" in PROMPTS else []


async def get_prompt(name: str, args: Dict[str, str] | None = None) -> GetPromptResult:
    """Get a prompt for protein analysis."""
    
    if name != "protein_analysis":
        raise ValueError(f"prompt {name} not found.")
    
    prompt = PROMPTS[name]
    
    if args is None:
        raise ValueError(f"No arguments provided for {name} prompt.")
    for arg in prompt.arguments:
        if arg.required and (arg.name not in args or not args.get(arg.name)):
            raise ValueError(f"Missing required arguments for {name} prompt.")
        
    protein_name = args.get("protein_name")
    return GetPromptResult(
        prompt=TextContent(
            type="text",
            text=f"Search Uniprot for {protein_name}"
        )
    )
