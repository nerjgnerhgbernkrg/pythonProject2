def git_search(query, language):
    url = 'https://api.github.com/search/repositories'
    params = {'q': query,
              'l': language}
    res = r.get(url, params=params).json()
    message = ''
    for repo in res['items']:
        message += f'<a href="{repo["svn_url"]}">{repo["name"]}</a>\n'
    return message