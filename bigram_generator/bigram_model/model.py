from tqdm import tqdm


class BigramWordGeneration:
    def __init__(self):
        self.dictionary = {}

    def train(self, training_words: list):
        print("Initializing Bigram probability Dictionary")
        with tqdm(total=sum([len(word) for word in training_words]), desc="Processing chars") as pbar:
            for word in training_words:
                used_word = ['<s>'] + list(word) + ['</s>']
                for first_char, second_char in zip(used_word, used_word[1:]):
                    if first_char not in self.dictionary:
                        self.dictionary[first_char] = {second_char: 1}
                    else:
                        if second_char not in self.dictionary[first_char]:
                            self.dictionary[first_char][second_char] = 1
                        else:
                            self.dictionary[first_char][second_char] += 1
                pbar.update(len(word))

        for keys in self.dictionary.keys():
            total = sum(self.dictionary[keys].values())
            for second_keys in self.dictionary[keys].keys():
                self.dictionary[keys][second_keys] /= total

    def generate_char(self, first_char: str):
        import random
        char_list = []
        char_prob = []
        for second_char in self.dictionary[first_char].keys():
            char_list.append(second_char)
            char_prob.append(self.dictionary[first_char][second_char])
        return random.choices(char_list, char_prob, k=1)[0]

    def generate(self):
        word = ""
        first_char = "<s>"
        while True:
            second_char = self.generate_char(first_char)
            if second_char == "</s>":
                break
            word += second_char
            first_char = second_char
        return word
