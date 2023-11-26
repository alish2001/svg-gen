import os 

docs= []
def load_from_directory(directory):
        """
        Loads documents from the specified directory recursively.
        """
        print(f"Loading documents from directory: {directory}")
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith(".svg"):
                        file_path = os.path.join(root, file)
                        title = os.path.splitext(file)[0]  # Use the file name as the title
                       # print(title)
                        with open(file_path, "r") as file_content:
                            svg_content = file_content.read()

                        # Add the document to the 'docs' list
                        docs.append({
                            "title": title,
                            "text": svg_content,
                            "url": file_path,
                        })
                        

        except Exception as e:
            print(f"Error loading documents from directory {directory}: {e}")

svg_directory = "/Users/paniz/Desktop/svg"

if __name__ == "__main__":
    load_from_directory(svg_directory)
    print(len(docs))
    #print all the files title names
    