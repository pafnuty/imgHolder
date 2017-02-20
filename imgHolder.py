import sublime, sublime_plugin, re

def pos(view, pos):
    point = view.sel()[0].begin()
    return view.substr(sublime.Region(point - pos, point))

def curText(view, location):
    lineLocation = view.line(location)
    return view.substr(sublime.Region(lineLocation.a, location))


def isTrigger(text, syntax):
    text = text.lower()
    syntax = syntax.lower()

    if syntax.find(u'html'):
        search = re.search(r"(?:(?:^|\s))(?:src|poster|srcset)=[\"\']?$", text)
        if (search):
            return True

    for s in (u'html', u'css', u'less', u'sass', u'scss', u'stylus'):
        if syntax.find(s):
            search = re.search(r"(?:(?:^|\s))url\([\"\']?$", text)
            if (search):
                return True

    for s in (u'markdown', u'multimarkdown'):
        if syntax.find(s):
            search = re.search(r"(?:(?:^|\s))\!\[(.*?)\]\(?$", text)
            if (search):
                return True

    return False

class imgHolder(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        syntax = view.settings().get('syntax')
        settings = sublime.load_settings('imgHolder.sublime-settings')
        # syntax = settings.get('syntax')

        imgholders = settings.get('imgholders')
        url_prefix = 'https://imgholder.ru/'
        completions = [(url_prefix + ih, url_prefix + ih) for ih in imgholders]
        
        curTxt = curText(view, locations[0])

        del completions[:]
        for ih in imgholders:
            completions.append(
                ('imgholder.ru/' + ih, url_prefix + ih)
            )

        if isTrigger(curTxt, syntax):
            print(completions)
            return (completions, sublime.INHIBIT_EXPLICIT_COMPLETIONS)
        return