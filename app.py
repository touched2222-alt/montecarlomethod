import streamlit as st
import random
import matplotlib.pyplot as plt

# ページの設定（タイトルやレイアウト）
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

# --- 2. 実験のやり方（見やすいように青いボックスに入れる） ---
st.info("""
### 🧪 実験のやり方
下のスライダーを動かして、**「試行回数（点の数）」**を変えてみてください。
* **数が少ない時：** 形がボロボロで、計算結果も 3.14 から遠いことが多いです。
* **数を増やした時：** きれいな円になり、結果が 3.1415... に近づいていきます。
""")

st.divider() # 区切り線

# --- 3. シミュレーション設定 ---
st.subheader("🛠️ シミュレーション開始")

# スライダーで回数を決定
total_points = st.slider("点の数を選んでください", min_value=100, max_value=10000, value=3000, step=100)

# --- 4. 計算処理 ---
inside_circle = 0
x_inside, y_inside = [], []
x_outside, y_outside = [], []

# プログレスバーの準備
progress_text = "計算中..."
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
    
    # 負荷軽減のため、100回に1回だけバーを更新
    if i % 100 == 0:
        my_bar.progress((i + 1) / total_points, text=progress_text)

my_bar.empty() # バーを消す

# 円周率の計算
pi_estimate = 4 * inside_circle / total_points

# --- 5. 結果の表示 ---
# カラムを使って横並びにする
col1, col2 = st.columns(2)

with col1:
    st.metric(label="シミュレーション結果", value=f"{pi_estimate:.5f}")

with col2:
    st.metric(label="実際の円周率", value="3.14159...")

# 誤差を表示
diff = abs(pi_estimate - 3.1415926535)
st.write(f"誤差: {diff:.5f}")

# --- 6. グラフの描画 ---
fig, ax = plt.subplots(figsize=(6, 6))
# 点をプロット（点が多すぎると重くなるのでサイズを調整）
point_size = 10 if total_points < 500 else 1
ax.scatter(x_inside, y_inside, color='red', s=point_size, label='円の内側')
ax.scatter(x_outside, y_outside, color='blue', s=point_size, label='外側')

ax.set_title(f'Monte Carlo Simulation (n={total_points})')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc="upper right")
ax.axis('equal') # 縦横比を固定

st.pyplot(fig)
