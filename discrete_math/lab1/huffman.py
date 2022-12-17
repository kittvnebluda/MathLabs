#!/usr/bin/python3
import pickle
import logging
import argparse

from collections import Counter


BYTES_SYMBOL = 7

class Node:
    def __init__(self, weight, depth):
        self.weight = weight
        self.depth = depth


class SingleNode(Node):
    def __init__(self, child: tuple):
        super().__init__(child[1], child[0])
        self.child = child[0]


class BinaryNode(Node):
    def __init__(self, node_left: Node, node_right: Node):
        super().__init__(node_left.weight + node_right.weight, (node_left.depth, node_right.depth))

        # print(node_left.depth, node_right.depth)

        self.child_left = node_left
        self.child_right = node_right

        self.leafs = {}

        # делаем имена для листьев слева
        if isinstance(node_left, SingleNode):
            self.leafs[node_left.child] = '0'
        elif isinstance(node_left, BinaryNode):
            for key in node_left.leafs.keys():
                self.leafs[key] = '0' + node_left.leafs[key]

        # делаем имена для листьев справа
        if isinstance(node_right, SingleNode):
            self.leafs[node_right.child] = '1'
        elif isinstance(node_right, BinaryNode):
            for key in node_right.leafs.keys():
                self.leafs[key] = '1' + node_right.leafs[key]


def make_dict(text: str) -> dict:
    logging.info('Создаю дерево')

    counter = Counter(text)

    assert len(counter) > 1

    nodes = sorted([SingleNode(x) for x in counter.items()], key=lambda x: x.weight, reverse=True)

    while len(nodes) > 1:
        # вытаскиваем последние узлы
        node_left, node_right = nodes.pop(), nodes.pop()
        # добавляем вместо них новый узел
        nodes.append(BinaryNode(node_left, node_right))
        # сортируем
        nodes.sort(key=lambda x: x.weight, reverse=True)

    logging.info(f'Результат построения дерева: {nodes[0].leafs}')

    return nodes[0].leafs


def encode(text, dict_):
    logging.info(f'Кодирую: {text if len(text) < 10000 else "слишком длинный текст для отображения"}')
    bin_res = ''
    for s in text:
        bin_res += dict_[s]

    res = ''
    for i in range(BYTES_SYMBOL, len(bin_res), BYTES_SYMBOL):
        res += chr(int(bin_res[i - BYTES_SYMBOL: i], 2))
    res += chr(int(bin_res[i:], 2))

    logging.info(f'Результат: {res if len(res) < 10000 else "слишком длинный текст для отображения"}')
    return res


def decode(text, dict_):
    logging.info(f'Декодирую: {text if len(text) < 10000 else "слишком длинный текст для отображения"}')

    bin_res = ''
    for s in text[:-1]:
        false_bin = bin(ord(s))[2:]
        bin_res += '0' * (BYTES_SYMBOL - len(false_bin)) + false_bin
    bin_res += bin(ord(text[-1]))[2:]

    new_dict = {value: key for (key, value) in dict_.items()}
    res = ''
    symbol = ''
    for s in bin_res:
        symbol += s
        if symbol in new_dict:
            res += new_dict[symbol]
            symbol = ''

    logging.info(f'Результат: {res if len(res) < 10000 else "слишком длинный текст для отображения"}')
    return res


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description='Realization of Huffman algorithm')
    parser.add_argument('mode', choices=['encode', 'decode'])
    parser.add_argument('-i', '--input_file', default='input_file.txt')
    parser.add_argument('-o', '--output_file', default='output_file.txt')

    args = parser.parse_args()

    if args.mode == 'encode':
        logging.info(f'Читаю файл {args.input_file}')
        with open(args.input_file, 'r', encoding='utf8') as f:
            text = f.read()
        dictionary = make_dict(text)

        encoded_text = encode(text, dictionary)
        logging.info(f'Записываю в файл {args.output_file}')
        with open(args.output_file, 'wb') as f:
            # pickle.dump(dictionary, f)
            pickle.dump(encoded_text, f)

    elif args.mode == 'decode':
        logging.info(f'Читаю файл {args.input_file}')
        with open(args.input_file, 'rb') as f:
            dictionary = pickle.load(f)
            text = pickle.load(f)

        decoded_text = decode(text, dictionary)
        logging.info(f'Записываю в файл {args.output_file}')
        with open(args.output_file, 'w', encoding='utf8') as f:
            f.write(decoded_text)
