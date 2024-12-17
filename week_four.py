def file_handling():
    try:
        input_filename= input("Enter File name:")
        
        with open(input_filename, "r") as infile:
            content=infile.read()
        output_filename= input("Enter output file name:")
        with open(output_filename, "w") as outfile:
            outfile.write(content.upper())
        print("File saved successfully")
    except FileNotFoundError:
        print("Error: File Not Found.")
    except Exception as e:
        print(f"Error: {e}")
file_handling()


        