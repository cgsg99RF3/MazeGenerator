# Генератор Лабиринтов

**Цель:** написать генератор лабиринтов

**Функционал:** 
1) Генерация с помощью DFS или минимального остовного дерева
2) Возможность выбрать вариант генерации через командную строку
3) Возможность задать размеры лабиринта через командную строку
4) Отображение лабиринта в консоле
4) Сохранение/загрузка лвбиринта в/из файлов
5) Решение лабиринтов и отображение пути

**Архитектура:**

**1) Class Params** 

self.width  # Высота лабиринта

self.height  # Ширина лабиринта

self.type  # Тип генерации - DFS(1)/MST(2)

def __init__(self, width, height, type)

**2) Class Cell**

self.x # Позиция x

self.y # Позиция y

self.is_checked # Флаг, был ли алгоритм в клетке 

self.walls # List([bool]) - лист, показывает есть стена или нет

def __init__(self, x : int, y : int)

def get_neighbours(self) -> List[Cell] # Поиск соседей

def check(self) -> bool # Проверка, нужно ли идти в клетку

@staticmetod
def is_passage(first : Cell, second : Cell) # Проверка, есть ли путь между клетками

@staticmetod
def is_wall(first : Cell, second : Cell) # Проверка, есть ли стена между клетками

@staticmetod
def connect(first : Cell, second : Cell) # Удаление стены между клетками

def load(file : _io.TextIOWrapper) # Загрузка из файла

def save(file : _io.TextIOWrapper) # Сохранение в файл

**3) Class Maze**

self.params # Параметры лабиринта

self.grid # Поле лабиринта, List[width * height * cell()]

def __init__(self, params : Params) # Инициализация

@abstractmetod
def draw(self) # Отрисовка лабиринта

@abstractmetod
def generate(self) # Генерация лабиринта (абстрактный метод)

**4) Class DFS(Maze)**

def generate(self) # Реализация абстрактного метода

def draw(self) # Реализация абстрактного метода

**5) Class MST(Maze)**

def generate(self) # Реализация абстрактного метода

def draw(self) # Реализация абстрактного метода

**6) Class Path**

self.maze # Лабиринт, для которого ищется путь

self.path # List[Cell] - путь

def __init__(self, maze : Maze) # Инициализация

def find(self) # Поиск пути

def draw(self) # Отрисовка пути
