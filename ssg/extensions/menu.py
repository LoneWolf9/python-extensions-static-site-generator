from ssg import hooks, parsers

files = []

@hooks.register("collect_files")
def collect_files(self, source, site_parsers):
    valid = lambda p : isinstance() not parsers.ResourceParser()