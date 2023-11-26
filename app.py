import streamlit as st


def main():
    st.title("SVG Viewer")

    # Replace 'output.svg' with the actual path to your SVG file
    svg_file_path = "output.svg"

    # Read the SVG file as text
    with open(svg_file_path, "r") as file:
        svg_content = file.read()

    # Add custom CSS styles to constrain the SVG within a box
    style = """
    <style>
        .svg-container {
            max-width: 500px;
            margin: auto;
        }
        .svg-content {
            width: 100%;
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


if __name__ == "__main__":
    main()
