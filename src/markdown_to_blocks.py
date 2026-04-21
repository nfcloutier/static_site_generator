
def markdown_to_blocks(markdown:str) -> list[str]:
    blocks = markdown.split("\n\n")
    return [item.strip() for item in blocks if item != ""]