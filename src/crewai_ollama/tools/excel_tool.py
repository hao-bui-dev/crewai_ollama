from crewai.tools import BaseTool
from typing import Optional
import pandas as pd

class ExcelParseTool(BaseTool):
    name: str = "excel_parser"
    description: str = "Parses Excel files and extracts column headers and sample values"

    def _run(self, file_path: str) -> str:
        try:
            df = pd.read_excel(file_path, sheet_name=0, header=0)
            columns = df.columns.tolist()
            sample_values = df.head(2).values.tolist()

            parsed_output = [
                {
                    "Column Name": columns[i],
                    "Sample Values": [row[i] for row in sample_values if i < len(row)]
                }
                for i in range(len(columns))
            ]

            return str(parsed_output)
        except Exception as e:
            return f"Error parsing Excel file: {e}"
