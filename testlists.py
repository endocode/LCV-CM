
def JSONPathList():
    JSONPath = list()
    JSONPath.append('json/hope-boot.json')
    JSONPath.append('json/spotify-docker-maven-plugin.json')
    JSONPath.append('json/dockerfile-maven.json')
    JSONPath.append('json/fabric8io-docker-maven-plugin.json')
    #emptyJSON
    #JSONPath.append('json/webdrivermanager.json')
    JSONPath.append('json/javacv.json')
    JSONPath.append('json/javacpp.json')
    JSONPath.append('json/TelegramBots.json')
    JSONPath.append('json/git-commit-id-maven-plugin.json')
    return JSONPath


def GitHubURLList():
    GitHubURL = list()

    GitHubURL.append('https://api.github.com/repos/hope-for/hope-boot/license')
    GitHubURL.append('https://api.github.com/repos/spotify/docker-maven-plugin/license')
    GitHubURL.append('https://api.github.com/repos/spotify/dockerfile-maven/license')
    #Inbound: GPL3.0 or later
    GitHubURL.append('https://api.github.com/repos/fabric8io/docker-maven-plugin/license')
    #links to do https://github.com/bonigarcia/webdrivermanager
    # Error 2021/03/10 11:02:13 Received a message: gooooo!!!!!
    # 2021/03/10 11:02:14 FASTEN reporter failed: couldn't get FileNodes, rpc error: code = Unavailable desc = connection error: desc = "transport: Error while dialing dial tcp 10.20.13.51:9080: connect: connection refused"
    #GitHubURL.append('https://api.github.com/repos/bonigarcia/webdrivermanager/license')

    #https://github.com/git-commit-id/git-commit-id-maven-plugin
    GitHubURL.append('https://api.github.com/repos/bytedeco/javacv/license')
    GitHubURL.append('https://api.github.com/repos/bytedeco/javacpp/license')
    GitHubURL.append('https://api.github.com/repos/rubenlagus/TelegramBots/license')
    GitHubURL.append('https://api.github.com/repos/git-commit-id/git-commit-id-maven-plugin/license')
    return GitHubURL
