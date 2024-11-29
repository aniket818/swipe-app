from typing import Dict, List
import streamlit as st
from content_data import SAMPLE_CONTENT

class DataManager:
    @staticmethod
    def initialize_session_state():
        if "current_index" not in st.session_state:
            st.session_state.current_index = 0
        if "stats" not in st.session_state:
            st.session_state.stats = {
                "likes": 0,
                "super_likes": 0,
                "dislikes": 0
            }
        if "viewed_content" not in st.session_state:
            st.session_state.viewed_content = set()

    @staticmethod
    def get_current_content() -> Dict:
        if st.session_state.current_index >= len(SAMPLE_CONTENT):
            return None
        return SAMPLE_CONTENT[st.session_state.current_index]

    @staticmethod
    def handle_action(action: str):
        if action == "like":
            st.session_state.stats["likes"] += 1
        elif action == "super_like":
            st.session_state.stats["super_likes"] += 1
        elif action == "dislike":
            st.session_state.stats["dislikes"] += 1

        current_content = DataManager.get_current_content()
        if current_content:
            st.session_state.viewed_content.add(current_content["id"])
        st.session_state.current_index += 1

    @staticmethod
    def get_stats() -> Dict[str, int]:
        return st.session_state.stats

    @staticmethod
    def filter_content(category: str = None) -> List[Dict]:
        if not category:
            return SAMPLE_CONTENT
        return [content for content in SAMPLE_CONTENT if content["category"].lower() == category.lower()]
