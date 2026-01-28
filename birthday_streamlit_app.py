# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:36:24 2026

@author: Sohail
"""

# happy_birthday_card_click_image.py

import streamlit as st
from streamlit.components.v1 import html

# ---- Page Config ----
st.set_page_config(
    page_title="🎉 Birthday Surprise 🎁",
    page_icon="🎂",
    layout="centered",
)

# ---- Page Theme ----
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #ffe6f0, #fff0f5);
        font-family: 'Comic Sans MS', cursive, sans-serif;
        overflow-x: hidden;
    }
    h1, h2, h3 {
        color: #d6336c;
        text-align: center;
    }
    .present-button {
        border: none;
        background: none;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .present-button:hover {
        transform: scale(1.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Hardcoded name ----
birthday_name = "Toni"

# ---- Session state to track if present opened ----
if "opened" not in st.session_state:
    st.session_state.opened = False

st.title("🎉❤️ A Special Present ❤️🎉")

# ---- Show present image wrapped in a button if not opened ----
if not st.session_state.opened:
    st.markdown(
        "<h3 style='text-align:center;'>Unwrap the present to see what you got!</h3>",
        unsafe_allow_html=True
    )

    # Hidden Streamlit button to trigger session_state
    clicked = st.button("Unwrap Me 🎁", key="present_button")

    # Centered present image as a clickable button
    st.markdown(
        """
        <div style='text-align:center; margin-top:20px;'>
            <form action="" method="get">
                <button type="submit" class="present-button">
                    <img src="https://cdn.pixabay.com/photo/2020/10/27/15/14/gift-5691042_1280.png"
                         style="width:250px; max-width:90%; height:auto;">
                </button>
            </form>
        </div>
        """,
        unsafe_allow_html=True
    )

    if clicked:
        st.session_state.opened = True

# ---- Once opened: show birthday message, balloons, and hearts ----
if st.session_state.opened:
    # Balloons animation
    st.balloons()

    # Birthday message
    st.markdown(
        f"<h1>Happy Birthday, {birthday_name}! 🥳💖<br>Have an amazing Birthday, with many more to come! ❤️</h1>",
        unsafe_allow_html=True
    )

    # Hearts animation
    html(
        """
        <div id="hearts-container"></div>
        <script>
        const container = document.getElementById('hearts-container');
        function createHeart() {
            const heart = document.createElement('div');
            const size = Math.random() * 25 + 25;
            heart.style.width = size + 'px';
            heart.style.height = size + 'px';
            heart.style.position = 'fixed';
            heart.style.left = Math.random() * window.innerWidth + 'px';
            heart.style.background = 'radial-gradient(circle at 50% 50%, #ff69b4, #ff1493)';
            heart.style.clipPath = 'polygon(50% 0%, 61% 14%, 75% 14%, 85% 25%, 85% 38%, 75% 50%, 50% 85%, 25% 50%, 15% 38%, 15% 25%, 25% 14%, 39% 14%)';
            heart.style.opacity = Math.random() * 0.7 + 0.3;
            heart.style.zIndex = 9999;
            container.appendChild(heart);
            let top = window.innerHeight;
            const floatUp = setInterval(() => {
                top -= 2;
                heart.style.top = top + 'px';
                if(top < -50) {
                    heart.remove();
                    clearInterval(floatUp);
                }
            }, 20);
        }
        setInterval(createHeart, 200);
        </script>
        """,
        height=600
    )

