#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from crewai_ollama.crew import CrewaiOllama  # adjust this if you renamed the module

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.

def run():
    inputs = {
        "file_path": "data/sample_invoice.xlsx", 
        'schema_definition': """
            customer_name: Full name of the customer
            invoice_date: Date the invoice was issued
            invoice_number: Unique identifier for the invoice
            amount: Total invoice value (USD)
        """,
        "topic": "Schema Mapping",
        "current_year": str(datetime.now().year)
    }

    try:
        CrewaiOllama().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'file_path': 'data/sample_invoice.xlsx',
        'schema_definition': 'customer_name, invoice_date, invoice_number, amount'
    }
    try:
        CrewaiOllama().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewaiOllama().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'file_path': 'data/sample_invoice.xlsx',
        'schema_definition': 'customer_name, invoice_date, invoice_number, amount'
    }

    try:
        CrewaiOllama().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
