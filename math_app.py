import streamlit as st
import random

# --- 1. 🎨 폰트 강제 적용 (HTML Link 방식) ---
def apply_custom_style():
    # 1. HTML <link> 태그를 이용해 폰트를 가장 먼저 불러옵니다.
    # 2. 모든 요소(*)에 폰트를 강제로(!important) 적용합니다.
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Gamja+Flower&family=Jua&display=swap" rel="stylesheet">
    
    <style>
    /* 전체 폰트 적용 우선순위: Jua -> Gamja Flower -> 맑은 고딕 -> 시스템 폰트 */
    html, body, [class*="css"], font, div, p, span, h1, h2, h3, h4, h5, h6, button, input, label, li, a {
        font-family: 'Jua', 'Gamja Flower', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif !important;
        color: #333333;
    }

    /* 배경색 */
    .stApp {
        background-color: #F8F9FA;
    }

    /* 카드형 디자인 */
    .main-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        border: 2px solid #E9ECEF; /* 테두리 조금 더 진하게 */
    }

    /* 제목 스타일 (보라색 그라데이션) */
    .title-text {
        font-family: 'Jua', sans-serif !important;
        background: linear-gradient(to right, #6C5CE7, #a29bfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* 강조 박스 */
    .highlight-box {
        background-color: #F3F0FF;
        border-left: 5px solid #6C5CE7;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        line-height: 1.8; /* 줄간격 넓게 */
        font-size: 1.1rem;
    }

    /* 버튼 디자인 */
    .stButton>button {
        background: linear-gradient(135deg, #6C5CE7, #8076EE);
        color: white !important;
        border: none;
        border-radius: 15px;
        padding: 15px 0;
        font-size: 1.3rem; /* 글씨 키움 */
        font-family: 'Jua', sans-serif !important;
        box-shadow: 0 4px 10px rgba(108, 92, 231, 0.2);
        width: 100%;
        margin-top: 10px;
    }
    .stButton>button:hover {
        transform: scale(1.02);
    }
    
    /* 사이드바 */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E5E7EB;
    }
    
    /* 라디오 버튼 선택지 */
    .stRadio label {
        background: white;
        padding: 15px;
        border-radius: 12px;
        border: 2px solid #F1F3F5;
        margin-bottom: 8px;
        font-size: 1.1rem !important;
    }
    .stRadio label:hover {
        border-color: #6C5CE7;
        background-color: #F8F7FF;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 📚 데이터 ---
UNITS = {
    1: "1. 분수의 나눗셈",
    2: "2. 각기둥과 각뿔",
    3: "3. 소수의 나눗셈",
    4: "4. 비와 비율"
}

CONCEPTS = {
    1: """
    <div class="main-card">
        <h3 style="color:#6C5CE7;">🍰 분수의 나눗셈 핵심 정리</h3>
        <p><b>1. (자연수) ÷ (자연수)</b></p>
        <p>"피자 1판을 3명이 나눠 먹으면?"<br>
        1개를 3명이 나누니 <b>1/3</b>이 됩니다.</p>
        <div class="highlight-box">
            <b>💡 공식 암기:</b><br>
            뒤에 있는 수(나누는 수)가 <b>분모(아래)</b>로 내려갑니다.<br>
            $$ 1 \\div 3 = \\frac{1}{3} $$
        </div>
        <br>
        <p><b>2. (분수) ÷ (자연수)</b></p>
        <p>나누기는 <b>'곱하기 분의 1'</b>로 바꿀 수 있어요.</p>
        <div class="highlight-box">
            <b>📝 예시 문제:</b><br>
            $$ \\frac{4}{5} \\div 2 $$ <br>
            ① 곱하기로 변신! ➡ $$ \\frac{4}{5} \\times \\frac{1}{2} $$ <br>
            ② 계산하면 ➡ $$ \\frac{4}{10} $$ ➡ 약분해서 <b>$$ \\frac{2}{5} $$</b>
        </div>
    </div>
    """,
    2: """
    <div class="main-card">
        <h3 style="color:#6C5CE7;">📦 각기둥과 각뿔</h3>
        <p><b>🏢 각기둥 (아파트)</b></p>
        <ul>
            <li>위아래가 똑같고 평행해요.</li>
            <li>옆면은 <b>직사각형</b>입니다.</li>
        </ul>
        <p><b>⛺ 각뿔 (텐트)</b></p>
        <ul>
            <li>위가 뾰족해요.</li>
            <li>옆면은 <b>삼각형</b>입니다.</li>
        </ul>
        <div class="highlight-box">
            <b>⚡ 공식 (N = 밑면의 변의 수)</b><br>
            각기둥 모서리: N × 3 <br>
            각뿔 모서리: N × 2
        </div>
    </div>
    """,
    3: """
    <div class="main-card">
        <h3 style="color:#6C5CE7;">💧 소수의 나눗셈</h3>
        <p><b>"점은 나중에 찍자!"</b></p>
        <div class="highlight-box">
            <b>🔎 예시: $$ 3.66 \\div 3 $$</b><br>
            1. 점 빼고 계산: $$ 366 \\div 3 = 122 $$ <br>
            2. 점 다시 찍기: 원래대로 두 칸 앞에 콕! ➡ <b>1.22</b>
        </div>
    </div>
    """,
    4: """
    <div class="main-card">
        <h3 style="color:#6C5CE7;">🍎 비와 비율</h3>
        <p><b>비 (Ratio)</b>: 3 : 2 (3 대 2)</p>
        <div class="highlight-box">
            <b>비율 (Rate)</b><br>
            $$ \\text{비율} = \\frac{\\text{비교하는 양(앞)}}{\\text{기준량(뒤)}} $$
        </div>
    </div>
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
            problem['exp'] = f"{a} ÷ {b} = {a}/{b}"
        else:
            ja, mo, nat = random.randint(1, 9), random.randint(2, 9), random.randint(2, 5)
            problem['q'] = f"계산하시오: $$\\frac{{{ja}}}{{{mo}}} \\div {nat}$$"
            problem['a'] = f"{ja}/{mo*nat}"
            problem['exp'] = f"곱하기 1/{nat}로 바꿔서 계산해요."
            
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
        unit_labels = list(UNITS.values())
        cur_label = UNITS[st.session_state.current_unit]
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
        st.markdown(f"<div class='title-text'>오늘의 학습: {unit_name.split('. ')[1]}</div>", unsafe_allow_html=True)
        st.markdown(CONCEPTS[st.session_state.current_unit], unsafe_allow_html=True)
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
        
        st.markdown(f"""
        <div class="main-card">
            <h4 style="color:#888;">Q{st.session_state.q_idx + 1}.</h4>
            <h3 style="color:#333;">{prob['q']}</h3>
        </div>
        """, unsafe_allow_html=True)

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
                        st.markdown(f"""
                        <div class="highlight-box" style="background:#FFF0F0; border-color:#FF6B6B;">
                            <b>정답: {prob['a']}</b><br>
                            해설: {prob['exp']}
                        </div>
                        """, unsafe_allow_html=True)
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
        st.markdown(f"""
        <div class="main-card" style="text-align:center;">
            <h1 style="color:#6C5CE7; font-size:3rem;">{sc}점</h1>
            <p style="font-size:1.5rem;">{'참 잘했어요! 🏆' if sc==100 else '수고했어요! 복습해볼까요? 💪'}</p>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        if c1.button("다시 풀기 🔄", use_container_width=True):
            st.session_state.step = 'intro'
            st.rerun()
        if len(st.session_state.wrong_notes) > 0:
            if c2.button("오답 노트 확인 📝", use_container_width=True):
                st.session_state.step = 'wrong_note_view'
                st.rerun()

    elif st.session_state.step == 'wrong_note_view':
        st.markdown("<div class='title-text'>📝 오답 노트</div>", unsafe_allow_html=True)
        if not st.session_state.wrong_notes:
            st.info("오답 노트가 비어있어요.")
        
        for i, n in enumerate(st.session_state.wrong_notes):
            with st.expander(f"🔍 {i+1}번 문제 보기"):
                st.markdown(f"""
                <div class="main-card" style="padding:15px; border-left: 5px solid #FF7675;">
                    <p><b>문제:</b> {n['q']}</p>
                    <p style="color:red;"><b>내가 쓴 답:</b> {n.get('user_wrong','?')}</p>
                    <p style="color:green;"><b>정답: {n['a']}</b></p>
                    <p style="background:#eee; padding:5px;"><b>해설:</b> {n['exp']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        if st.button("🔙 돌아가기", use_container_width=True):
            st.session_state.step = 'intro'
            st.rerun()

if __name__ == "__main__":
    main()
