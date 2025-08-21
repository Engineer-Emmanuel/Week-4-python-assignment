# File Read & Write Challenge 🖋️

def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            content = f.read()
        
        # Example modification: convert to uppercase
        modified_content = content.upper()

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ File has been modified and saved as '{output_file}'")

    except FileNotFoundError:
        print("❌ Error: The input file does not exist.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Example use
modify_file("input.txt", "output.txt")