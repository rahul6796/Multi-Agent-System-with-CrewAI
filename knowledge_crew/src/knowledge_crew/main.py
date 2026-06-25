#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from knowledge_crew.crew import KnowledgeCrew
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {'query': 'What are the different scoring functions used in the paper'}

    try:
        KnowledgeCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

