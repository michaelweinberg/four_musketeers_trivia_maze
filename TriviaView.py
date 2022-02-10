from map import Map


class TriviaView:
    def print_map(self, map):
        map.generate_map()
        map.print_map()

    def print_question(self, question):
        print("question:" + question)