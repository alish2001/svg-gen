import os

# MODIFY THIS TO EMBED YOUR OWN SVGs!
svg_directory = "/Users/alish/Downloads/svgs"
def load_from_directory(directory):
    docs = []
    """
    Loads documents from the specified directory recursively.
    """
    print(f"Loading svgs from directory: {directory}")
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(".svg"):
                    file_path = os.path.join(root, file)
                    title = file  # Use the file name as the title
                    # # print(title)
                    # with open(file_path, "r") as file_content:
                    #     svg_content = file_content.read()

                    # Add the document to the 'docs' list
                    docs.append(
                        {
                            "title": title,
                            "file_path": file_path,
                            # "url": file_path,
                        }
                    )
    except Exception as e:
        print(f"Error loading documents from directory {directory}: {e}")

    return docs[:100]


if __name__ == "__main__":
    docs = load_from_directory(svg_directory)
    print(len(docs))
    for doc in docs:
        print(doc)
    # print all the files title names
