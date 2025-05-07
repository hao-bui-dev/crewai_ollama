import os
import pandas as pd

def extract_table_from_excel(file_path: str):
    try:
        df = pd.read_excel(file_path, sheet_name=0, header=0)
        print("DEBUG HEADERS:", df.columns.tolist())  # 👈 Add this

        columns = df.columns.tolist()
        sample_values = df.head(2).values.tolist()

        parsed_output = [
            {
                "Column Name": columns[i],
                "Sample Values": [row[i] for row in sample_values if i < len(row)]
            }
            for i in range(len(columns))
        ]
        return parsed_output

    except Exception as e:
        return f"Error parsing Excel file: {e}"

def save_transformed_table(markdown_table: str, output_path="data/transformed_output.xlsx"):
    try:
        lines = markdown_table.strip().split("\n")
        header_line = lines[0]
        data_lines = [line for line in lines[2:] if line.strip()]

        # Convert markdown row to list
        headers = [h.strip() for h in header_line.strip("|").split("|")]
        rows = [[cell.strip() for cell in line.strip("|").split("|")] for line in data_lines]

        df = pd.DataFrame(rows, columns=headers)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_excel(output_path, index=False)
        print(f"✅ Transformed table saved to {output_path}")
    except Exception as e:
        print(f"❌ Error saving table: {e}")

