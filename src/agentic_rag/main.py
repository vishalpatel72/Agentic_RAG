#!/usr/bin/env python
import sys
import os
from agentic_rag.crew import AgenticRagCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def ensure_output_directory():
    """Ensure the outputs directory exists."""
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def handle_code_output(result):
    """Handle code output from crew execution.
    
    Args:
        result: The result from crew execution
    """
    if isinstance(result, str) and result.startswith("```python"):
        code = result[9:].strip()
        if code.endswith("```"):
            code = code[:-3].strip()

        ensure_output_directory()
        with open("outputs/visualize.ipynb", "w") as f:
            f.write(code)


def run():
    """
    Run the crew.
    """
    inputs = {
        "query": "What was the year with the highest total expenses?",
        "company": "Coffee Co",
        "company_description": "Coffee Co is a aesthetic local coffee shop in San Francisco",
    }
    result = AgenticRagCrew().crew().kickoff(inputs=inputs)
    handle_code_output(result)


def train():
    """
    Train the crew for a given number of iterations.
    """
    if len(sys.argv) < 3:
        print("Usage: train <n_iterations> <filename>")
        sys.exit(1)
        
    inputs = {"query": "What was the year with the highest total expenses?"}
    try:
        result = (
            AgenticRagCrew()
            .crew()
            .train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
        )
        handle_code_output(result)

    except ValueError as e:
        raise Exception(f"Invalid arguments provided: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    if len(sys.argv) < 2:
        print("Usage: replay <task_id>")
        sys.exit(1)
        
    try:
        AgenticRagCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    if len(sys.argv) < 3:
        print("Usage: test <n_iterations> <openai_model_name>")
        sys.exit(1)
        
    inputs = {"query": "What was the year with the highest total expenses?"}
    try:
        result = (
            AgenticRagCrew()
            .crew()
            .test(
                n_iterations=int(sys.argv[1]),
                openai_model_name=sys.argv[2],
                inputs=inputs,
            )
        )
        handle_code_output(result)

    except ValueError as e:
        raise Exception(f"Invalid arguments provided: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
