import sublime, sublime_plugin, re


class imgHolder(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        syntax = view.settings().get('syntax')
        settings = sublime.load_settings("imgHolder.sublime-settings")
        imgholders = settings.get("imgholders")

        def pos(pos):
            point = view.sel()[0].begin()
            return view.substr(sublime.Region(point - pos, point))


        url_prefix = 'https://imgholder.ru/'
        showCompletions = []

        attr = pos(5)

        for s in (u'html', u'css', u'less', u'sass', u'scss'):
            if syntax.lower().find(s):
                if attr.find('src=') != -1 or attr.find('url(') != -1:
                    showCompletions = [(url_prefix + ih, url_prefix + ih) for ih in imgholders]
            return showCompletions
        return
