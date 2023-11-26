# Step 1: Get simple rag working
import cohere
import os

import json
import uuid
from typing import List, Dict
from unstructured.partition.html import partition_html
from unstructured.chunking.title import chunk_by_title
import streamlit as st
from chatbot import Chatbot
from document import Documents


api_key = "fkAeCp5ZzmMiI4YBtkKUD6BanZVdk1vImBGZ5W0m"
co = cohere.Client(api_key)


class App:
    def __init__(self, chatbot: Chatbot):
        """
        Initializes an instance of the App class.

        Parameters:
        chatbot (Chatbot): An instance of the Chatbot class.

        """
        self.chatbot = chatbot

    def run(self):
        """
        Runs the chatbot application.

        """
        while True:
            # Get the user message
            message = input("User: ")

            # Typing "quit" ends the conversation
            if message.lower() == "quit":
                print("Ending chat.")
                break
            else:
                print(f"User: {message}")

            # Get the chatbot response
            response = self.chatbot.generate_response(message)

            # Print the chatbot response
            print("Chatbot:")
            flag = False
            for event in response:
                # Text
                if event.event_type == "text-generation":
                    print(event.text, end="")

                # Citations
                if event.event_type == "citation-generation":
                    if not flag:
                        print("\n\nCITATIONS:")
                        flag = True
                    print(event.citations)

            print(f"\n{'-'*100}\n")


# TODO: ADD SOURCE RETRIEVAL
# define sources
sources = [
    {"title": "1 SVG", "file_path": "./sample-svgs/1.svg"},
    {"title": "2 SVG", "file_path": "./sample-svgs/2.svg"},
    {"title": "3 SVG", "file_path": "./sample-svgs/3.svg"},
    {"title": "angle-up SVG", "file_path": "./sample-svgs/angle-up.svg"},
    {"title": "bed-empty SVG", "file_path": "./sample-svgs/bed-empty.svg"},
]


def main():
    st.title("SVG Viewer")

    # Replace 'output.svg' with the actual path to your SVG file
    svg_file_path = "output.svg"

    # Read the SVG file as text
    with open(svg_file_path, "r") as file:
        svg_content = file.read()

    # Add custom CSS styles to constrain and center the SVG within the screen
    style = """
    <style>
        .svg-container {
            display: flex;
            align-items: center;
            justify-content: center;
            max-width: 50%;
            max-height: 50vh;
            margin: auto;
        }
        .svg-content {
            width: 50%;
            height: auto;
        }
    </style>
    """

    # Display the SVG content using st.markdown with custom styles
    st.markdown(style, unsafe_allow_html=True)
    st.markdown(
        '<div class="svg-container"><div class="svg-content">{}</div></div>'.format(
            svg_content
        ),
        unsafe_allow_html=True,
    )


# Create an instance of the Documents class with the given sources
documents = Documents(sources)

# Create an instance of the Chatbot class with the Documents instance
chatbot = Chatbot(documents)

# Create an instance of the App class with the Chatbot instance
app = App(chatbot)

# Run the chatbot
app.run()

# TODO: UNCOMMENT TO RUN MAIN
# if __name__ == "__main__":
#     main()
