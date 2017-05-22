from github import Github
from graphviz import Graph

users = ["kostaNew", "koshinus", "Genraim", "CLearERR", "gogoleff", "denchistyakov", "Zhigalov", "mokhov"]

def get_collaborations(users):
    github = Github()

    projects = []
    for user in users:
        repos = github.get_user(user).get_repos()
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


def render_collaborations(collaborations):
    dot = Graph(comment="Collaborations")

    for user in users:
        dot.node(user, user)

    dot.attr("node", style="filled", color="lightgrey")
    for key in collaborations:
        contributors = collaborations[key]
        dot.attr("node", group=key)
        dot.node(key, key)
        for contributor in contributors:
            dot.edge(contributor.login, key)

    dot.render('collaborations.gv', view=True)


collaborations = get_collaborations(users)
render_collaborations(collaborations)
