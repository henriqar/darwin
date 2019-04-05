

from type import MappingProxyType

class Map(MappingProxyType):

    def __init__(self, data):

        try:
            iterator = iter(data)
        except TypeError:
            pass
        else:
            pass

    def generate_uniform_random_number(self):
        pass

    def generate_gaussian_random_number(self):
        pass

    def generate_cauchy_random_number(self):
        pass

    def generate_levy_distribution(self):
        pass

    def euclidean_distance(self):
        pass

    def get_perpendicular_vector(self):
        pass

    def normalize_vector(self):
        pass

    def sort_agent(self):
        pass

    def sort_data_by_val(self):
        pass

    def waive_comment(self):
        pass

    def read_searchspace_from_file(self):
        pass

    def get_FUNCTION_id(self):
        pass

    def roulette_selection(self):
        pass

    def roultte_selection_ga(self):
        pass


