import streamlit as st

def apply_card_styling():
    return """
    <style>
    .content-card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    .content-image {
        width: 100%;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .action-buttons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
    }
    .stats-container {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """
