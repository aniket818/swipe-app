import streamlit as st
from data_manager import DataManager
from ui_components import render_content_card, render_action_buttons, render_statistics
from styles import apply_card_styling
from content_data import SAMPLE_CONTENT

def main():
    st.set_page_config(
        page_title="Content Swiper",
        page_icon="🎯",
        layout="centered"
    )
    
    # Apply custom styling
    st.markdown(apply_card_styling(), unsafe_allow_html=True)
    
    # Initialize session state
    DataManager.initialize_session_state()
    
    # App title
    st.title("Content Swiper 🎯")
    
    # Category filter
    categories = ["All"] + list(set(content["category"] for content in SAMPLE_CONTENT))
    selected_category = st.selectbox("Filter by category", categories)
    
    # Get current content
    current_content = DataManager.get_current_content()
    
    if current_content:
        # Render content card
        render_content_card(current_content)
        
        # Render action buttons
        dislike, superlike, like = render_action_buttons()
        
        # Handle button actions
        if like:
            DataManager.handle_action("like")
            st.experimental_rerun()
        elif superlike:
            DataManager.handle_action("super_like")
            st.experimental_rerun()
        elif dislike:
            DataManager.handle_action("dislike")
            st.experimental_rerun()
    else:
        st.info("You've seen all available content! Check back later for more.")
    
    # Show statistics
    st.markdown("---")
    render_statistics(DataManager.get_stats())
    
    # Mobile-friendly instructions
    with st.expander("How to use"):
        st.markdown("""
        - 👎 Swipe left or click "Nope" to skip
        - ❤️ Swipe right or click "Like" to save
        - ⭐ Click "Super" for content you love
        - Filter content by category using the dropdown above
        """)

if __name__ == "__main__":
    main()
