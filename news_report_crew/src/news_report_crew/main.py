from news_report_crew.crew import NewsReportCrew



def run():
    # define the inputs
    inputs = {'country': "India"}

    # creat crew obj
    crew = NewsReportCrew().crew()

    # run the crew
    output = crew.kickoff(inputs=inputs)


if __name__ == "__main__":
    run()