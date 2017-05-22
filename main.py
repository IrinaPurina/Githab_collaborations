from github import Github

# users = ["kostaNew", "koshinus", "arkaev", "Genraim", "CLearERR", "gogoleff", "denchistyakov", "Zhigalov", "trixartem", "mokhov"]
users = ["kostaNew", "koshinus"]

def get_collaborations(users):
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
        interesting_contributors = [contributor for contributor in contributors if users.count(contributor.login) > 0]
        if len(interesting_contributors) > 1:
            collaborations[project.full_name] = interesting_contributors

    return collaborations

collaborations = get_collaborations(users)

for key in collaborations:
    contributors = collaborations[key]
    print(key)
    for contributor in contributors:
        print(contributor.login)

