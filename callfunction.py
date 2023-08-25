import pandas as pd

def update_csv_data(csv_data, user_index, field, new_value):
    if field in csv_data.columns:
        csv_data.loc[user_index, field] = new_value
        return True
    else:
        print(f"Field '{field}' not found in CSV columns.")
        return False

def main():
    csv_file = "dataofuser.csv"
    csv_data = pd.read_csv(csv_file)

    print("===================Original CSV data:=====================")
    print(csv_data)

    user_index = int(input("Enter the user index you want to update: "))
    field = input("Enter the field you want to update: ")
    new_value = input("Enter the new value: ")

    if update_csv_data(csv_data, user_index, field, new_value):
        csv_data.to_csv(csv_file, index=False)
        print("===========CSV data updated successfully!==============")
        print(csv_data)
    else:
        print("=================CSV data update failed.================")

if __name__ == "__main__":
    main()
