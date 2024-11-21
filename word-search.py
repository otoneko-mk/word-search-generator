import random
import csv

# 単語リスト
words = [
    "TICAD", "AU", "NEPAD", "EAC", "ECOWAS", "COMESA",
    "Sahara", "Nile", "Kilimanjaro", "Victoria", "Savanna",
    "Kenya", "Ghana", "Egypt", "Johannesburg", "AddisAbaba",
    "Ubuntu", "Zulu", "MansaMusa", "Pharaoh", "Kente",
    "Elephant", "Baobab", "Cheetah", "Giraffe", "Lion"
]

# グリッドサイズ
grid_size = 15
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# 方向（縦、横、斜め）
directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

# 単語をグリッドに配置する関数
def place_word(word):
    word_len = len(word)
    placed = False
    while not placed:
        # ランダムに方向と開始位置を選ぶ
        direction = random.choice(directions)
        start_row = random.randint(0, grid_size - 1)
        start_col = random.randint(0, grid_size - 1)
        end_row = start_row + direction[0] * (word_len - 1)
        end_col = start_col + direction[1] * (word_len - 1)

        # 配置可能かチェック
        if 0 <= end_row < grid_size and 0 <= end_col < grid_size:
            # 単語を配置
            temp_positions = []
            for i in range(word_len):
                new_row = start_row + direction[0] * i
                new_col = start_col + direction[1] * i
                if grid[new_row][new_col] in (' ', word[i]):
                    temp_positions.append((new_row, new_col))
                else:
                    break
            else:  # 配置可能
                for position, letter in zip(temp_positions, word):
                    grid[position[0]][position[1]] = letter
                placed = True

# 各単語を配置
for word in words:
    place_word(word.upper())

# 空白をランダムなアルファベットで埋める
for row in range(grid_size):
    for col in range(grid_size):
        if grid[row][col] == ' ':
            grid[row][col] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# CSVファイルにグリッドを出力する
csv_file_path = "word_search_africa.csv"
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(grid)

print(f"ワードサーチをCSV形式で出力しました: {csv_file_path}")
