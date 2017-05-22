from github import Github

users = ["kostaNew", "koshinus", "arkaev", "Genraim", "CLearERR", "gogoleff", "denchistyakov", "Zhigalov", "trixartem", "mokhov"]

gitHub = Github()

projects = []

for user in users:
    repos = gitHub.get_user(user).get_repos()
    for repo in repos:
        if repo.fork:
            projects.append(repo.source)
        else:
            projects.append(repo)

collaborations = {}

for project in projects:
    contributors = project.get_contributors()
    interestingContributors = [contributor for contributor in contributors if users.count(contributor.login) > 0]
    if len(interestingContributors) > 1:
        collaborations[project.full_name] = interestingContributors;
        print(project.full_name)
        print("----------------------")
        for contributor in contributors:
            print(contributor.login)