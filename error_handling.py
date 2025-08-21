# Error Handling Lab 🧪

def read_file_with_error_handling():
    filename = input("Enter the filename: ")

    try:
        with open(filename, "r") as f:
            content = f.read()
            print("\n📄 File Content:\n")
            print(content)
    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("⚠️ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the function
read_file_with_error_handling()