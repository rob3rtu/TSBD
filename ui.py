import streamlit as st
from main import OracleVectorManager

def similarity_from_distance(distance):
    return round(1 - float(distance), 3)

def highlight_keywords(text, query):
    words = [w.strip(".,?!:;()[]{}").lower() for w in query.split() if len(w) > 3]

    for word in words:
        text = text.replace(word, f"**{word}**")
        text = text.replace(word.capitalize(), f"**{word.capitalize()}**")

    return text
st.set_page_config(
    page_title="Semantic Search AI",
    page_icon="🔎",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a 0%, #111827 100%);
}
.block-container {
    padding-top: 2rem;
}
.search-card {
    background: rgba(255,255,255,0.06);
    padding: 24px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.12);
}
.result-card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 16px;
    border: 1px solid rgba(255,255,255,0.10);
}
.badge {
    background: #2563eb;
    color: white;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_manager():
    return OracleVectorManager()

manager = get_manager()

if "db_loaded" not in st.session_state:
    with st.spinner("Se încarcă documentele în baza de date..."):
        manager.load_and_sync_db('./docs/mutators/')
        st.session_state.db_loaded = True

st.title("🔎 Semantic Search peste documente text")
st.caption("Căutare semantică folosind Oracle AI Vector Search + embeddings")
st.info("""
Această aplicație folosește embeddings pentru a căuta după sens, nu doar după cuvinte exacte.
Întrebarea este transformată într-un vector, apoi comparată cu vectorii documentelor salvate în Oracle.
""")

st.markdown("### 🧪 Demo semantic")

col_a, col_b = st.columns(2)

with col_a:
    if st.button("Query direct"):
        st.session_state.query = "How to configure a custom mutator?"

with col_b:
    if st.button("Query reformulat"):
        st.session_state.query = "How can I modify a quadrille?"

with st.sidebar:
    st.header("⚙️ Setări")
    top_k = st.slider("Număr rezultate", 1, 10, 5)
    st.info("Documentele sunt împărțite în chunks, transformate în embeddings și căutate semantic în Oracle.")

col1, col2, col3 = st.columns(3)
col1.metric("Bază de date", "Oracle 23ai")
col2.metric("Model", "ALL_MINILM_L12_V2")
col3.metric("Vector Search", "Activ")

st.markdown("### Pune o întrebare")

example = st.selectbox(
    "Exemple rapide:",
    [
        "",
        "How to configure a custom mutator?",
        "What are mutator methods?",
        "How does fill work?",
        "How to replace values?"
    ]
)

if "query" not in st.session_state:
    st.session_state.query = ""

query = st.text_input(
    "Întrebarea ta:",
    value=st.session_state.query,
    placeholder="Ex: How to configure a custom mutator?"
)

search = st.button("🚀 Caută semantic", use_container_width=True)

if search and query.strip():
    with st.spinner("Se caută cele mai relevante fragmente..."):
        results = manager.search(query, limit=top_k)

    st.markdown("## Rezultate")

    if not results:
        st.warning("Nu s-au găsit rezultate.")
    else:
        for i, res in enumerate(results, 1):
            distance = round(float(res["score"]), 4)
            similarity = similarity_from_distance(distance)

            if i == 1:
                st.success("🔥 Cel mai relevant rezultat")

            with st.container():
                st.markdown(
                    f"""
                    <div class="result-card">
                        <span class="badge">Rezultat #{i}</span>
                        <p style="margin-top:12px;"><b>Distanță vectorială:</b> {distance}</p>
                        <p><b>Similarity score:</b> {similarity}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                with st.expander("Vezi fragmentul complet", expanded=(i == 1)):
                    st.markdown(highlight_keywords(res["content"], query))

elif search:
    st.warning("Scrie o întrebare înainte de căutare.")