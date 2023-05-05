def issue_to_check(issue_title):
    titles = ['OAS directory not found :robot: :warning:',
              'OAS file not found :robot: :warning:']
    return any(title == issue_title for title in titles)