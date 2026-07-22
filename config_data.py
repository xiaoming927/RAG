md5_path = "./md5.txt"


# Chroma
collection_name = "rag"
persist_directory = "./chroma_db"


# splitter
chunk_size = 1000
chunk_overlap = 100

separators = [
    "\n\n",
    "\n",
    "。",
    "！",
    "？",
    ".",
    "!",
    "?",
    " ",
    ""
]

max_split_char_number = 1000



similarity_threshold = 1   #这就是要求匹配的个数

embedding_model_name = "text-embedding-v4"
chat_model_name = 'qwen3-max'

session_config = {
    "configurable": {
        "session_id": "user_001",
    }
}

