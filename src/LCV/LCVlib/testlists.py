
def JSONPathList():
    JSONPath = list()
    # hope-boot is license compliant
    JSONPath.append('json/hope-boot.json')

    # spotify-docker-maven-plugin uses only Apache 2.0, so it is compliant
    JSONPath.append('json/spotify-docker-maven-plugin.json')

    # spotify:dockerfile-maven-plugin uses only Apache 2.0, so it is compliant
    JSONPath.append('json/dockerfile-maven.json')

    # ffabric8io-docker-maven-plugin uses only Apache 2.0, so it is compliant
    JSONPath.append('json/fabric8io-docker-maven-plugin.json')
    # emptyJSON
    # JSONPath.append('json/webdrivermanager.json')

    # This project does not specify correctly an SPDX id for its oubound license
    JSONPath.append('json/javacv.json')

    # This project does not specify correctly an SPDX id for its oubound license
    JSONPath.append('json/javacpp.json')

    # GPL-3.0-or-later is not supported, because 'or later' notation.
    JSONPath.append('json/TelegramBots.json')

    # 1 above 3 licenses found are compatible.
    JSONPath.append('json/git-commit-id-maven-plugin.json')

    # An UNKNOWN license has been found within the project. This cannot reveal license incompatibility
    JSONPath.append('json/teamspeak3.json')

    # 9
    # outbound Apache2.0 https://github.com/dzikoysk/reposilite
    JSONPath.append('json/org.panda-lang:reposilite.json')

    # policeman-tools/forbidden-apis
    # outbound Apache2.0 https://api.github.com/repos/policeman-tools/forbidden-apis/license

    # 10 https://github.com/mojohaus/versions-maven-plugin
    # JSONPath.append('json/policeman-tools-forbidden-apis.json')
    JSONPath.append('json/org.codehaus.mojo:versions-maven-plugin.json')

    # 11  https://github.com/revelc/formatter-maven-plugin
    JSONPath.append(
        'json/net.revelc.code.formatter:formatter-maven-plugin.json')

    return JSONPath


def GitHubURLList():
    GitHubURL = list()

    GitHubURL.append('https://api.github.com/repos/hope-for/hope-boot/license')
    GitHubURL.append(
        'https://api.github.com/repos/spotify/docker-maven-plugin/license')
    GitHubURL.append(
        'https://api.github.com/repos/spotify/dockerfile-maven/license')
    # Inbound: GPL3.0 or later
    GitHubURL.append(
        'https://api.github.com/repos/fabric8io/docker-maven-plugin/license')
    # links to do https://github.com/bonigarcia/webdrivermanager
    # Error 2021/03/10 11:02:13 Received a message: gooooo!!!!!
    # 2021/03/10 11:02:14 FASTEN reporter failed: couldn't get FileNodes, rpc error: code = Unavailable desc = connection error: desc = "transport: Error while dialing dial tcp 10.20.13.51:9080: connect: connection refused"
    # GitHubURL.append('https://api.github.com/repos/bonigarcia/webdrivermanager/license')

    # https://github.com/git-commit-id/git-commit-id-maven-plugin
    GitHubURL.append('https://api.github.com/repos/bytedeco/javacv/license')
    GitHubURL.append('https://api.github.com/repos/bytedeco/javacpp/license')
    GitHubURL.append(
        'https://api.github.com/repos/rubenlagus/TelegramBots/license')
    GitHubURL.append(
        'https://api.github.com/repos/git-commit-id/git-commit-id-maven-plugin/license')
    GitHubURL.append(
        'https://api.github.com/repos/TheHolyWaffle/TeamSpeak-3-Java-API/license')
    # https://github.com/dzikoysk/reposilite
    GitHubURL.append(
        'https://api.github.com/repos/dzikoysk/reposilite/license')
    # https://github.com/policeman-tools/forbidden-apis
    # GitHubURL.append(
    #     'https://api.github.com/repos/policeman-tools/forbidden-apis/license')
    # GitHubURL.append(
    #     'https://api.github.com/repos/eclipse/jkube/license')
    GitHubURL.append(
        'https://api.github.com/repos/revelc/formatter-maven-plugin/license')
    GitHubURL.append(
        'https://api.github.com/repos/mojohaus/versions-maven-plugin/license')

    return GitHubURL
