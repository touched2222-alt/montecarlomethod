import random
import matplotlib.pyplot as plt

# 1. 設定：試行回数（点の数）
total_points = 3000  # ここを増やすと精度が上がります

# 2. 変数の準備
inside_circle = 0
x_inside, y_inside = [], []
x_outside, y_outside = [], []

# 3. シミュレーション開始
print(f"--- {total_points}回のシミュレーションを開始します ---")

for _ in range(total_points):
    # 0から1の間でランダムなx, y座標を作成
    x = random.random()
    y = random.random()

    # 原点(0,0)からの距離を計算（三平方の定理：x^2 + y^2）
    distance = x**2 + y**2

    # 距離が1以下なら「円の内側」
    if distance <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

# 4. 円周率の計算
# エリアの面積比は (円の面積 / 正方形の面積) = π/4 なので、結果を4倍する
pi_estimate = 4 * inside_circle / total_points

print(f"シミュレーション結果の円周率: {pi_estimate}")
print(f"実際の円周率（参考） : 3.141592...")

# 5. グラフで可視化（ここからお絵かき）
plt.figure(figsize=(6, 6))
plt.scatter(x_inside, y_inside, color='red', s=1, label='Inside Circle')
plt.scatter(x_outside, y_outside, color='blue', s=1, label='Outside')
plt.title(f'Monte Carlo Simulation (Points: {total_points})')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="upper right")
plt.axis('equal') # 縦横比を同じにする
plt.show()