class Node:
    """
    Класс, представляющий узел бинарного дерева.

    Attributes:
        value: Значение, хранимое в узле.
        left (Node): Ссылка на левого потомка узла.
        right (Node): Ссылка на правого потомка узла.
    """

    def __init__(self, value):
        """
        Инициализация нового узла с заданным значением.

        Args:
            value: Значение, которое будет храниться в узле.
        """
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """
        Возвращает строковое представление узла.

        Returns:
            str: Строковое представление узла, включая его значение и значения левого и правого потомков (если они есть).
        """
        res = f'Значение узла: {self.value}'
        if self.left:
            res += f', Левый потомок: {self.left.value}'
        if self.right:
            res += f', Правый потомок: {self.right.value}'
        return res

class BinaryTree:
    """
    Класс для представления бинарного дерева.

    Attributes:
        root (Node): Корневой узел дерева.

    Methods:
        add(value): Добавляет новый узел с заданным значением в дерево.
        search(node, value, parent=None): Рекурсивно ищет узел с заданным значением в дереве и возвращает его и его родителя.
        count_elements(node=None): Рекурсивно подсчитывает количество элементов в дереве.
        print_tree(node=None): Рекурсивно выводит все элементы дерева на экран.
        delete(value): Удаляет элемент с заданным значением из дерева.
    """

    def __init__(self, root_value):
        """
        Инициализация нового бинарного дерева с корневым значением.

        Args:
            root_value: Значение корневого узла.
        """
        self.root = Node(root_value)

    def add(self, value):
        """
        Добавляет новый узел с заданным значением в дерево.

        Args:
            value: Значение, которое нужно добавить в дерево.
        """
        result, parent = self.search(self.root, value)

        if result is None:
            new_node = Node(value)
            if value > parent.value:
                parent.right = new_node
            else:
                parent.left = new_node
        else:
            print("Узел с таким значением уже существует.")

    def search(self, node, value, parent=None):
        """
        Рекурсивно ищет узел с заданным значением в дереве.

        Args:
            node (Node): Текущий узел, с которого начинается поиск.
            value: Значение, которое нужно найти.
            parent (Node, optional): Родительский узел текущего узла.

        Returns:
            Tuple[Node, Node]: Возвращает кортеж, содержащий найденный узел и его родителя.
        """
        if node is None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)

    def count_elements(self, node=None):
        """
        Рекурсивно подсчитывает количество элементов в дереве.

        Args:
            node (Node, optional): Текущий узел, с которого начинается подсчет. Если не указан, начинает с корневого узла.

        Returns:
            int: Количество элементов в дереве.
        """
        if node is None:
            return 0  # Базовый случай: если узел равен None, возвращаем 0

        return 1 + self.count_elements(node.left) + self.count_elements(node.right)

    def print_tree(self):
        """
        Выводит все элементы дерева в консоль.

        """
        self._print_tree(self.root)

    def _print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left is not None or node.right is not None:
                self._print_tree(node.left, level + 1, "L--- ")
                self._print_tree(node.right, level + 1, "R--- ")

    def delete(self, value):
        """
        Удаляет элемент с заданным значением из дерева.

        Args:
            value: Значение элемента, который нужно удалить.
        """
        self.root, _ = self._delete(self.root, value)

    def _delete(self, node, value):
        """
        Рекурсивно удаляет узел с заданным значением из дерева.

        Args:
            node (Node): Текущий узел, с которого начинается удаление.
            value: Значение элемента, который нужно удалить.

        Returns:
            Tuple[Node, bool]: Возвращает кортеж, содержащий обновленный узел и флаг, указывающий, был ли элемент удален.
        """
        if node is None:
            return node, False

        if value == node.value:
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True

            min_value = self.find_min(node.right)
            node.value = min_value
            node.right, _ = self._delete(node.right, min_value)
            return node, True

        if value < node.value:
            node.left, deleted = self._delete(node.left, value)
            return node, deleted

        node.right, deleted = self._delete(node.right, value)
        return node, deleted

    def find_min(self, node):
        """
        Находит минимальное значение в правом поддереве заданного узла.

        Args:
            node (Node): Узел, с которого начинается поиск минимального значения.

        Returns:
            Any: Минимальное значение в правом поддереве.
        """
        while node.left is not None:
            node = node.left
        return node.value

# Создание экземпляра бинарного дерева
bt = BinaryTree(5)

# Добавление элементов
bt.add(10)
bt.add(15)
bt.add(3)
bt.add(4)
# Поиск элементов
result, parent = bt.search(bt.root, 10)

# Удаление элемента
bt.delete(10)

# Вывод всего дерева на экран
bt.print_tree()

# Подсчет количества элементов
#count = bt.count_elements()