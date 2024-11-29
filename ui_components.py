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
    col1, col2, col3 = st.columns(3)
    
    with col1:
        dislike = st.button("👎 Nope")
    with col2:
        superlike = st.button("⭐ Super")
    with col3:
        like = st.button("❤️ Like")
        
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
