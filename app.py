import streamlit as st
import random
import matplotlib.pyplot as plt

# --- ここからStreamlit用の設定 ---
st.title("モンテカルロ法で円周率を計算")
st.write("ボタンを押すたびにシミュレーションを再実行します。")

# 1. 設定：試行回数（スライダーで変更できるように進化！）
total_points = st.slider("試行回数（点の数）", 100, 10000, 3000)

# 2. 変数の準備
inside_circle = 0
x_inside, y_inside = [], []
x_outside, y_outside = [], []

# 3. シミュレーション開始
# プログレスバーを表示
progress_bar = st.progress(0)

for i in range(total_points):
    x = random.random()
    y = random.random()
    distance = x**2 + y**2

    if distance <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)
    
    # プログレスバーを更新（重くなるので100回に1回だけ更新）
    if i % 100 == 0:
        progress_bar.progress((i + 1) / total_points)

progress_bar.progress(1.0) # 完了

# 4. 円周率の計算
pi_estimate = 4 * inside_circle / total_points

# 結果を大きく表示
st.metric(label="シミュレーション結果の円周率", value=f"{pi_estimate:.5f}")
st.write(f"実際の円周率（参考） : 3.141592...")

# 5. グラフで可視化
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x_inside, y_inside, color='red', s=1, label='Inside Circle')
ax.scatter(x_outside, y_outside, color='blue', s=1, label='Outside')
ax.set_title(f'Monte Carlo Simulation (Points: {total_points})')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc="upper right")
ax.axis('equal')

# ★ここが重要：Streamlitにグラフを渡す命令
st.pyplot(fig)
