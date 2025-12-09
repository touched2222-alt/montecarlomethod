import streamlit as st
import random
import matplotlib.pyplot as plt

# ページの設定
st.set_page_config(page_title="モンテカルロ法シミュレーター", layout="centered")

# --- 1. アプリのタイトルと解説 ---
st.title("🎯 モンテカルロ法で円周率を求めてみよう")

st.markdown("""
### モンテカルロ法とは？
「数打ちゃ当たる」戦法で、難しい値を確率的に予測する方法です。
ここでは、正方形の中にランダムに点を打ち、**「円の中に入った点の割合」**から円周率（$\pi$）を計算します。

#### 仕組み
1. 正方形の中に、デタラメに点を打ちます。
2. **「円の内側（赤）」**と**「外側（青）」**の数を数えます。
3. 全体の点数に対する「赤の点」の割合を4倍すると、円周率に近づきます。
""")

# --- 2. 実験のやり方 ---
st.info("""
### 🧪 実験のやり方
下のスライダーを動かして、**「試行回数（点の数）」**を変えてみてください。
回数を**100,000回**に増やすと、計算に少し時間がかかりますが、より正確な値（3.1415...）に近づく様子が観察できます。
""")

st.divider()

# --- 3. シミュレーション設定 ---
st.subheader("🛠️ シミュレーション開始")

# ★ここを変更しました：max_valueを100,000にアップ！
total_points = st.slider("点の数を選んでください", min_value=100, max_value=100000, value=3000, step=100)

# --- 4. 計算処理 ---
inside_circle = 0
x_inside, y_inside = [], []
x_outside, y_outside = [], []

# プログレスバーの準備
progress_text = "計算中... 少々お待ちください"
my_bar = st.progress(0, text=progress_text)

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
    
    # ★変更点：回数が多いので、バーの更新頻度を減らして高速化（1000回に1回更新）
    if i % 1000 == 0:
        progress_per = (i + 1) / total_points
        my_bar.progress(progress_per, text=progress_text)

my_bar.empty() # バーを消す

# 円周率の計算
pi_estimate = 4 * inside_circle / total_points

# --- 5. 結果の表示 ---
col1, col2 = st.columns(2)

with col1:
    st.metric(label="シミュレーション結果", value=f"{pi_estimate:.5f}")

with col2:
    st.metric(label="実際の円周率", value="3.14159...")

# 誤差を表示
diff = abs(pi_estimate - 3.1415926535)
st.write(f"誤差: {diff:.5f}")

# --- 6. グラフの描画 ---
# 10万個の点を描画するのは重いので、少し工夫します
st.write("グラフを描画中...") 

fig, ax = plt.subplots(figsize=(6, 6))

# 点のサイズ調整（数が多いときは、点を極小サイズにする）
if total_points > 10000:
    point_size = 0.1  # 10万回のときはさらに小さく
    alpha_val = 0.5   # 少し透明にして重なりを見やすく
else:
    point_size = 1
    alpha_val = 1.0

ax.scatter(x_inside, y_inside, color='red', s=point_size, alpha=alpha_val, label='円の内側')
ax.scatter(x_outside, y_outside, color='blue', s=point_size, alpha=alpha_val, label='外側')

ax.set_title(f'Monte Carlo Simulation (n={total_points})')
ax.set_xlabel('x')
ax.set_ylabel('y')
# 点が多すぎると凡例が見づらくなることがありますが、一旦そのまま表示します
ax.legend(loc="upper right")
ax.axis('equal')

st.pyplot(fig)
