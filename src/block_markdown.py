from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        block = block.strip()
        if len(block) != 0:
            new_blocks.append(block)
    return new_blocks

def block_to_block_type(markdown):
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    if markdown.startswith("#"):
        index = 0
        count = 0
        while index < len(markdown) and markdown[index] == "#":
            count += 1
            index += 1
        if 1 <= count <= 6 and index < len(markdown) and markdown[index] == " ":
            return BlockType.HEADING
    lines = markdown.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    true = 0
    for i, line in enumerate(lines, start=1):
        if line.startswith(f"{i}. "):
            true += 1
    if true == len(lines):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH