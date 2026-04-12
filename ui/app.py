import streamlit as st
from dotenv import load_dotenv

from src.retrieval.index_storage import load_index
from src.retrieval.vector_retriever import retrieve_from_index
from src.llm.generate import generate_answer


def main():
    load_dotenv()

    st.set_page_config(page_title="RosieKnows", page_icon="🐶📖")
    st.title("🐶📖 RosieKnows")
    st.write("A simple multi-document RAG demo.")

    query = st.text_input("Ask a question")

    if st.button("Run") and query:
        with st.spinner("Loading index..."):
            index = load_index()

        with st.spinner("Retrieving context..."):
            top_results = retrieve_from_index(query, index, top_k=3)

        top_chunks = [
            f"[source: {item['source']} | chunk: {item['chunk_index']}]\n{item['text']}"
            for item, _ in top_results
        ]

        with st.spinner("Generating answer..."):
            answer = generate_answer(query, top_chunks)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")
        for item, score in top_results:
            st.write(
                f"{item['source']} | chunk {item['chunk_index']} | score={score:.4f}"
            )

        with st.expander("Retrieved Chunks"):
            for item, score in top_results:
                st.markdown(
                    f"**{item['source']}** | chunk {item['chunk_index']} | score={score:.4f}"
                )
                st.write(item["text"])


if __name__ == "__main__":
    main()