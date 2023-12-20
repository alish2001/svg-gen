Some things to do in no particular order to package this up:

# ~~Chatbot~~

-> Modify chatbot so that conversation history is no longer kept (every time a new message is received, the conversation history is cleared) ✅ done
-> cleaner generations
-> can be done by getting rid of conversationid

# Embeddings

-> Figure out how embeddings are getting RAG'd and if it is ACTUALLY based on title or not
-> Make sure they are based on titles ✅ done
-> Experiment a little bit with different titles ("SVG code for <insert>") maybe ✅ done

-> Save embeddings to a file so that they can be loaded in the future
-> dont generate everytime

ref for saving and restoring: https://github.com/nmslib/hnswlib

# async

-> Convert all requests to async request using co.AsyncClient()
