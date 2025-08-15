from langchain_community.document_loaders import WebBaseLoader
import bs4

loader = WebBaseLoader(web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
                       bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                           class_= ("post-title","post-content","post-header")
                       ))
                       )


loader.load()
