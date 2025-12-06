import streamlit as st
import random

# --- 1. 🎨 디자인 & CSS 설정 ---
def apply_custom_style():
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
    
    <style>
    /* 1. 기본 폰트 설정 */
    html, body, [class*="css"], div, p, span, h1, h2, h3, h4, button, input {
        font-family: 'Jua', 'Noto Sans KR', sans-serif !important;
        color: #333333;
    }

    /* 2. 배경색 */
    .stApp {
        background-color: #F8F9FA;
    }

    /* 3. st.info 박스 스타일 변경 (보라색 테마로 커스텀) */
    /* 기본 파란색 알림창을 우리가 원하는 보라색 개념 박스로 바꿉니다 */
    div[data-baseweb="notification"] {
        background-color: #F3F0FF !important; /* 연한 보라 배경 */
        border-left: 5px solid #6C5CE7 !important; /* 진한 보라 선 */
        border-radius: 10px;
        padding: 20px;
    }
    
    /* 4. 제목 스타일 */
    h1, h2, h3 {
        color: #6C5CE7 !important;
    }

    /* 5. 버튼 스타일 */
    .stButton>button {
        background: linear-gradient(135deg, #6C5CE7, #8076EE);
        color: white !important;
        border: none;
        border-radius: 15px;
        padding: 15px 0;
        font-size: 1.2rem;
        font-weight: bold;
        width: 100%;
        margin-top: 10px;
    }
    .stButton>button:hover {
        transform: scale(1.02);
    }
    
    /* 6. 라디오 버튼 스타일 */
    .stRadio label {
        background: white;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #EEE;
    }
    .stRadio label:hover {
        border-color: #6C5CE7;
        background-color: #F8F7FF;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 📚 데이터 (수학 공식이 깨지지 않도록 r"..." 사용) ---
UNITS = {
    1: "1. 분수의 나눗셈",
    2: "2. 각기둥과 각뿔",
    3: "3. 소수의 나눗셈",
    4: "4. 비와 비율"
}

# 중요: 여기서 HTML 태그를 쓰지 않고 마크다운만 씁니다.
# 디자인은 위에서 설정한 CSS가 st.info 박스에 자동으로 적용됩니다.
CONCEPTS = {
    1: r"""
### 🍰 분수의 나눗셈 핵심 정리

**1. (자연수) ÷ (자연수)**

"피자 1판을 3명이 나눠 먹으면?"
1개를 3명이 나누니 **1/3**이 됩니다.

> **💡 공식 암기**
>
> 뒤에 있는 수(나누는 수)가 **분모(아래)**로 슝! 내려갑니다.
>
> $$ 1 \div 3 = \frac{1}{3} $$

**2. (분수) ÷ (자연수)**

나누기는 **'곱하기 분의 1'**로 변신할 수 있어요.
"4로 나눈다"는 말은 "4등분 한 것 중의 하나(1/4)를 가진다"는 뜻이니까요.

> **📝 예시 문제**
>
> $$ \frac{4}{5} \div 2 $$
>
> ① 나누기를 곱하기로 변신! 👉 $$ \frac{4}{5} \times \frac{1}{2} $$
>
> ② 분모는 분모끼리! 👉 $$ \frac{4}{10} $$
>
> ③ 약분하면 끝! 👉 $$ \frac{2}{5} $$
""",
    2: r"""
### 📦 각기둥과 각뿔 구분하기

**🏢 각기둥 (아파트 모양)**

* 위 뚜껑과 아래 바닥이 **똑같이 생겼고 평행**해요.
* 옆에서 보면 반듯한 **직사각형** 모양이에요.

**⛺ 각뿔 (텐트 모양)**

* 바닥은 평평하지만 위는 **뾰족한 점**으로 모여요.
* 옆에서 보면 **삼각형** 모양이에요.

> **⚡ 구성 요소 공식 (N = 밑면의 변의 수)**
>
> * **각기둥 모서리**: $ N \times 3 $
> * **각기둥 꼭짓점**: $ N \times 2 $
> * **각뿔 모서리**: $ N \times 2 $
> * **각뿔 꼭짓점**: $ N + 1 $
""",
    3: r"""
### 💧 소수의 나눗셈 비법

**"점은 나중에 찍자!"**

소수점이 있으면 어렵죠? 잠시 점을 없애고 **자연수처럼** 계산하세요.

> **🔎 예시: $$ 3.66 \div 3 $$**
>
> 1.  점 숨기기: $$ 366 \div 3 = 122 $$
> 2.  점 다시 찍기: 원래 점이 두 칸 앞에 있었죠?
>     정답도 똑같이 두 칸 앞에 점을 콕!
>
>     👉 **1.22**
""",
    4: r"""
### 🍎 비와 비율

**1. 비 (Ratio)**

사과 3개와 배 2개를 비교할 때 **3 : 2** 라고 씁니다.
왼쪽(3)이 **비교하는 양**, 오른쪽(2)이 **기준량**입니다.

> **2. 비율 (Rate)**
>
> 비를 분수나 소수로 나타낸 값이에요.
>
> $$ \text{비율} = \frac{\text{비교하는 양(앞)}}{\text{기준량(뒤)}} $$
"""
}

# --- 3. 로직 함수 ---
def check_answer(user_input, correct_val):
    try:
        user_str = str(user_input).strip().replace(" ", "")
        correct_str = str(correct_val).strip().replace(" ", "")
        if user_str == correct_str: return True
        
        def parse(v):
            if '/' in str(v):
                n, d = map(float, str(v).split('/'))
                return n/d
            return float(v)
        return abs(parse(user_str) - parse(correct_str)) < 0.001
    except:
        return False

def generate_problem(unit_num, difficulty):
    problem = {'unit': unit_num}
    q_type = 'obj' if (random.random() > 0.5 or unit_num == 2) else 'subj'
    problem['type'] = q_type
    
    if unit_num == 1:
        if difficulty == '하':
            a, b = random.randint(1, 8), random.randint(2, 9)
            if a >= b: b = a + 1
            problem['q'] = f"피자 {a}판을 {b}명이 나누어 먹습니다. 한 사람의 양은?"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = f"전체({a}) ÷ 사람수({b}) = {a}/{b}"
        else:
            ja, mo, nat = random.randint(1, 9), random.randint(2, 9), random.randint(2, 5)
            problem['q'] = f"계산하시오: $$\\frac{{{ja}}}{{{mo}}} \\div {nat}$$"
            problem['a'] = f"{ja}/{mo*nat}"
            problem['exp'] = f"나누기를 곱하기 1/{nat}로 바꿔서 계산해요."
            
        if q_type == 'obj':
            opts = [problem['a'], f"{mo}/{ja}", f"{ja}/{nat}", f"{nat}/{ja}"]
            random.shuffle(opts)
            problem['options'] = opts

    elif unit_num == 2:
        shapes = [('삼각기둥',3,'기둥'), ('사각기둥',4,'기둥'), ('오각기둥',5,'기둥'), ('삼각뿔',3,'뿔'), ('사각뿔',4,'뿔')]
        name, n, kind = random.choice(shapes)
        target = random.choice(['모서리', '꼭짓점', '면'])
        problem['q'] = f"**{name}**의 **{target}** 수는?"
        
        if kind == '기둥':
            ans = n*3 if target=='모서리' else (n*2 if target=='꼭짓점' else n+2)
        else:
            ans = n*2 if target=='모서리' else n+1
        problem['a'] = str(ans)
        problem['exp'] = f"{name}의 밑면 변은 {n}개입니다."
        
        if q_type == 'obj':
            opts = list(set([str(ans), str(ans+1), str(ans-1), str(n*2), str(n*3)]))[:4]
            while len(opts) < 4: opts.append(str(random.randint(5,20)))
            random.shuffle(opts)
            problem['options'] = opts

    elif unit_num == 3:
        d = random.randint(2, 5)
        q = random.randint(12, 88)
        dividend = q * d 
        problem['q'] = f"계산하시오: $${dividend/100} \\div {d}$$"
        problem['a'] = str(q/100)
        problem['exp'] = f"{dividend}÷{d}={q} 이므로 점을 찍으면 {q/100}"
        if q_type == 'obj':
            opts = [str(q/100), str(q/10), str(q), str(q/1000)]
            random.shuffle(opts)
            problem['options'] = opts

    elif unit_num == 4:
        a, b = random.randint(2, 9), random.randint(3, 9)
        if random.random() > 0.5:
            problem['q'] = f"비 {a}:{b}의 비율(분수)은?"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = f"앞({a}) 나누기 뒤({b}) = {a}/{b}"
            if q_type == 'obj': problem['options'] = [f"{a}/{b}", f"{b}/{a}", f"1/{b}", f"{a+b}"]
        else:
            problem['q'] = f"비 {a}:{b}에서 **기준량**은?"
            problem['a'] = str(b)
            problem['exp'] = "뒤에 있는 수가 기준량입니다."
            if q_type == 'obj': problem['options'] = [str(a), str(b), str(a+b), "1"]
        if q_type == 'obj': random.shuffle(problem['options'])

    return problem

# --- 4. 메인 실행 ---
def main():
    st.set_page_config(page_title="초등 수학 짱", page_icon="💯", layout="wide")
    apply_custom_style()

    # NameError 방지: 변수 초기화를 가장 먼저 수행
    unit_labels = list(UNITS.values())

    if 'step' not in st.session_state: st.session_state.step = 'intro'
    if 'current_unit' not in st.session_state: st.session_state.current_unit = 1
    if 'wrong_notes' not in st.session_state: st.session_state.wrong_notes = []
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
    if 'current_prob' not in st.session_state: st.session_state.current_prob = None
    if 'solved' not in st.session_state: st.session_state.solved = False

    # --- 사이드바 ---
    with st.sidebar:
        st.markdown("<h2 style='font-family:Jua; color:#6C5CE7;'>🎒 나의 학습실</h2>", unsafe_allow_html=True)
        st.write("---")
        
        # 단원 선택
        cur_label = UNITS[st.session_state.current_unit]
        # index 에러 방지를 위한 안전장치
        if cur_label not in unit_labels:
            cur_label = unit_labels[0]
            
        sel = st.radio("학습 단원", unit_labels, index=unit_labels.index(cur_label), label_visibility="collapsed")
        
        # 변경 감지
        new_u = [k for k, v in UNITS.items() if v == sel][0]
        if new_u != st.session_state.current_unit:
            st.session_state.current_unit = new_u
            st.session_state.step = 'intro'
            st.session_state.score = 0
            st.rerun()

        st.write("---")
        st.markdown(f"**📝 오답 노트 ({len(st.session_state.wrong_notes)})**")
        if len(st.session_state.wrong_notes) > 0:
            if st.button("오답 문제 풀기"):
                st.session_state.step = 'wrong_note_view'
                st.rerun()
        else:
            st.caption("틀린 문제가 없어요!")

        st.write("---")
        if st.button("🏠 홈으로"):
            st.session_state.step = 'intro'
            st.rerun()

    # --- 메인 화면 ---
    unit_name = UNITS[st.session_state.current_unit]

    if st.session_state.step == 'intro':
        st.markdown(f"<h1 style='color:#6C5CE7; font-family:Jua;'>오늘의 학습: {unit_name.split('. ')[1]}</h1>", unsafe_allow_html=True)
        
        # HTML 태그 대신 st.info 사용 (CSS로 색상 변경됨) -> LaTeX 완벽 지원
        st.info(CONCEPTS[st.session_state.current_unit])
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 공부 시작하기!", use_container_width=True):
                st.session_state.step = 'quiz'
                st.session_state.q_idx = 0
                st.session_state.score = 0
                st.session_state.current_prob = None
                st.session_state.solved = False
                st.rerun()

    elif st.session_state.step == 'quiz':
        total = 5
        st.markdown(f"### ✏️ 문제 풀기 ({st.session_state.q_idx + 1}/{total})")
        st.progress((st.session_state.q_idx) / total)

        if st.session_state.current_prob is None:
            st.session_state.current_prob = generate_problem(st.session_state.current_unit, '중')
            st.session_state.solved = False
        
        prob = st.session_state.current_prob
        
        # 문제 표시 (컨테이너 사용)
        with st.container(border=True):
            st.markdown(f"<h4 style='color:#888;'>Q{st.session_state.q_idx + 1}.</h4>", unsafe_allow_html=True)
            st.markdown(f"### {prob['q']}")

        with st.form(key=f"f_{st.session_state.q_idx}"):
            if prob['type'] == 'obj':
                ans = st.radio("정답:", prob['options'], index=None, disabled=st.session_state.solved)
            else:
                ans = st.text_input("정답:", disabled=st.session_state.solved)
            
            btn_label = "다음 문제 ➡️" if st.session_state.solved else "채점하기 ✨"
            sub = st.form_submit_button(btn_label, use_container_width=True)

        if sub:
            if not st.session_state.solved:
                if not ans:
                    st.warning("정답을 입력하세요!")
                else:
                    if check_answer(ans, prob['a']):
                        st.balloons()
                        st.success("정답입니다! 🎉")
                        st.session_state.score += 1
                    else:
                        st.error("틀렸습니다 😢")
                        # 오답 해설도 st.info(또는 warning) 사용해서 수식 깨짐 방지
                        st.warning(f"**정답: {prob['a']}**\n\n해설: {prob['exp']}")
                        
                        if prob not in st.session_state.wrong_notes:
                            prob['user_wrong'] = ans
                            st.session_state.wrong_notes.append(prob)
                    st.session_state.solved = True
                    st.rerun()
            else:
                st.session_state.q_idx += 1
                st.session_state.current_prob = None
                st.session_state.solved = False
                if st.session_state.q_idx >= total: st.session_state.step = 'result'
                st.rerun()

    elif st.session_state.step == 'result':
        sc = st.session_state.score * 20
        with st.container(border=True):
            st.markdown(f"<h1 style='text-align:center; color:#6C5CE7; font-size:3rem;'>{sc}점</h1>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center; font-size:1.5rem;'>{'참 잘했어요! 🏆' if sc==100 else '수고했어요! 복습해볼까요? 💪'}</p>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        if c1.button("다시 풀기 🔄", use_container_width=True):
            st.session_state.step = 'intro'
            st.rerun()
        if len(st.session_state.wrong_notes) > 0:
            if c2.button("오답 노트 확인 📝", use_container_width=True):
                st.session_state.step = 'wrong_note_view'
                st.rerun()

    elif st.session_state.step == 'wrong_note_view':
        st.markdown("<h2 style='color:#6C5CE7; font-family:Jua;'>📝 오답 노트</h2>", unsafe_allow_html=True)
        if not st.session_state.wrong_notes:
            st.info("오답 노트가 비어있어요.")
        
        for i, n in enumerate(st.session_state.wrong_notes):
            with st.expander(f"🔍 {i+1}번 문제 보기"):
                st.markdown(f"**문제:** {n['q']}")
                st.markdown(f"**내가 쓴 답:** :red[{n.get('user_wrong','?')}]")
                st.markdown(f"**정답:** :green[{n['a']}]")
                # 해설 박스
                st.info(f"**해설:** {n['exp']}")
        
        if st.button("🔙 돌아가기", use_container_width=True):
            st.session_state.step = 'intro'
            st.rerun()

if __name__ == "__main__":
    main()
