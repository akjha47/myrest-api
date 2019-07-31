import pandas as pd
class TrieNode:
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False
        self.length = 0
        self.weight = 0
data = pd.read_csv('suggest_word/static/word_search.tsv', sep="\t", names=['word', "weight"], dtype={'word': object})
data['length'] = data.apply(lambda x: len(str(x['word'])), axis=1)

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def form_trie(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node = self.root
        for a in str(key[0]):
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True
        node.weight = key[1]
        node.length = key[2]

    def suggestions_rec(self, node, word):
        if node.last:
            self.word_list.append([word, node.length, -1 * node.weight])

        for a, n in node.children.items():
            self.suggestions_rec(n, word + a)

    def return_auto_suggestions(self, key):
        node = self.root
        not_found = False
        temp_word = ''

        for a in key:
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]
        if not_found:
            return 0
        elif node.last and not node.children:
            return -1
        self.word_list=[]
        self.suggestions_rec(node, temp_word)
        sorted_word_list = sorted(self.word_list, key=lambda x: (x[1], x[2]))
        word_suggestions_to_return=[]
        for words in sorted_word_list[:25]:
            word_suggestions_to_return.append(words[0])
        if len(word_suggestions_to_return)<24:
            in_between=data[(data['length'] > len(key)) & (data['word'].str.contains(key))].copy()
            in_between.sort_values(['length', 'weight'], ascending=[True, False], inplace=True)
            list_of_words_having_key=in_between.iloc[:, :].values.tolist()
            for words in list_of_words_having_key:
                if len(word_suggestions_to_return)>=24:
                    break
                if words[0] not in word_suggestions_to_return:
                    word_suggestions_to_return.append(words[0])
            del in_between
            del list_of_words_having_key
            return word_suggestions_to_return
        return word_suggestions_to_return

#print('Starting Server...')
words_tree = Trie()
words_tree.form_trie(data.iloc[:, :].values.tolist())
# del data
#print('Server Started....')
