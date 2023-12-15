PG_DOCS_INDEX_NAME = "LangChain_index_docs"

# Indexing + Record Management db url
RECORD_MANAGER_DB_URL = "postgresql+psycopg2://postgres@192.168.201.74:5433/chat_langchain"

# Embedding db url. database name: "chatbot_vector"
EMBEDDING_DB_URL = "postgresql+psycopg2://postgres@192.168.201.74:5433/chat_langchain"

# colection name is a field name in table generated "langchain_pg_collection"
COLLECTION_NAME = "chatbot"
