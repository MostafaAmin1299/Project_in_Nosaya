import pandas as pd
from datetime import datetime

class CollectData:
    def __init__(self):
        self.new_data = None 
        self.file_name = None

    def create_template(self):
        columns = ['Student Name', 'Student Grade']
        template_df = pd.DataFrame(columns=columns)

        time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f'Template_{time}.xlsx'
        template_df.to_excel(file_name, index=False)

        print(f"'{file_name}' has been created successfully.")

    def read_excel_file(self):
        file_path = input("Please enter the full file path: ")

        try:
            self.new_data = pd.read_excel(file_path)
            self.file_name = file_path

            print("File read successfully. Here's a preview:")
            print(self.new_data.head())

        except FileNotFoundError:
            print("File not found. Please check the path.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def run(self):
        while True:
            option = input("\n(1) Create Template\n(2) Read Excel File\nChoose (1 or 2): ")

            if option == "1":
                self.create_template()
                break

            elif option == "2":
                self.read_excel_file()
                break

            else:
                print(f"Invalid option: {option}. Please enter only 1 or 2.")
                
        print("Collect the data Done")

        return self.new_data, self.file_name



