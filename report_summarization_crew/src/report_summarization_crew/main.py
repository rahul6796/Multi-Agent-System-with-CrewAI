
from report_summarization_crew.crew import ReportSummarizationCrew



def run():
    """
    Its run the report summarization
    """
    # define the input
    inputs = {'field': "Education"}

    # create the crew object = 
    my_crew = ReportSummarizationCrew().crew()


    # pass the input to the crew and execute the crew.
    result = my_crew.kickoff(inputs = inputs)


if __name__ == "__main__":
    run()
