import os


class Searcher(object):
    def __init__(self):
        self.__results = []
        pass

    def search(self, start_path='D:\\', pattern=None):
        """
        Function will search files/images which match the provided pattern
        Will place results in self.results list
        :param start_path: Path from where to start recursive search
        :param pattern:
        :return: number of results
        """
        path_content = os.listdir(start_path)
        self.__results = path_content
        return len(path_content)

    def results(self):
        return self.__results


if __name__ == '__main__':
    searcher = Searcher()
    no_of_matches = searcher.search()
    print(searcher.results())
