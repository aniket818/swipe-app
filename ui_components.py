import streamlit as st
from typing import Dict, Any

def render_content_card(content: Dict[str, Any]):
    st.markdown(f"""
        <div class="content-card">
            <img src="{content['image']}" class="content-image" alt="{content['title']}">
            <h2>{content['title']}</h2>
            <p>{content['description']}</p>
            <div class="category-tag">{content['category']}</div>
        </div>
    """, unsafe_allow_html=True)

def render_action_buttons():
    # Create columns with more spacing
    col1, spacer1, col2, spacer2, col3 = st.columns([1, 0.5, 1, 0.5, 1])
    
    button_style = """
        <style>
        div[data-testid="stButton"] button {
            font-size: 1.2rem;
            padding: 0.75rem 1.5rem;
            border-radius: 25px;
            transition: all 0.3s ease;
        }
        div[data-testid="stButton"] button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)
    
    with col1:
        dislike = st.button("👎 Nope", use_container_width=True, type="secondary", help="Skip this content")
    with col2:
        superlike = st.button("⭐ Super", use_container_width=True, type="primary", help="Love this content!")
    with col3:
        like = st.button("❤️ Like", use_container_width=True, type="primary", help="Save this content")
        
    return dislike, superlike, like

def render_statistics(stats: Dict[str, int]):
    st.markdown("""
        <div class="stats-container">
            <h3>Your Activity</h3>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Likes", stats["likes"])
    with col2:
        st.metric("Super Likes", stats["super_likes"])
    with col3:
        st.metric("Dislikes", stats["dislikes"])
