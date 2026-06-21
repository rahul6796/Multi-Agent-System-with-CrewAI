#!/usr/bin/env python

from blog_generation_crew.crew import BlogGenerationCrew



def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Need for experimentation in Data Science',
    }

    try:
        result = BlogGenerationCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

