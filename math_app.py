import streamlit as st
import random

# --- 1. 🎨 세련된 스타일 적용 (벤치마킹 UI) ---
def apply_custom_style():
    st.markdown("""
    <style>
    /* Noto Sans KR 폰트 임포트 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
    
    /* 전체 테마 적용 */
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif !important;
        background-color: #F5F7FA !important; /* 밝은 회색 배경 */
        color: #333333 !important;
    }
    
    /* 메인 컨테이너 스타일 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
    }

    /* ----------------- 카드 UI ----------------- */
    .card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        border: 1px solid #ECEFF5;
    }
    .concept-card {
        border-left: 5px solid #6C5CE7; /* 포인트 컬러 */
    }
    .quiz-card {
        border-top: 5px solid #A29BFE;
    }

    /* ----------------- 타이포그래피 ----------------- */
    h1 {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(to right, #6C5CE7, #A29BFE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
    }
    h2 { color: #4a4a4a; font-weight: 700; }
    h3 { color: #6C5CE7; font-weight: 700; margin-bottom: 1rem;}
    p, li { line-height: 1.7; font-size: 1.1rem; color: #555;}
    
    /* ----------------- 버튼 스타일 ----------------- */
    .stButton>button {
        background: linear-gradient(135deg, #6C5CE7, #8176EE);
        color: white !important;
        border: none;
        border-radius: 15px;
        padding: 12px 24px;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(108, 92, 231, 0.3);
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(108, 92, 231, 0.4);
    }

    /* ----------------- 사이드바 스타일 ----------------- */
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #F0F2F5, #FFFFFF);
        border-right: 1px solid #E0E5EC;
    }
    [data-testid="stSidebar"] h1 {
        background: none;
        -webkit-text-fill-color: #6C5CE7;
        font-size: 2rem;
    }

    /* 라디오 버튼 스타일 커스텀 (카드처럼 보이게) */
    .stRadio > div {
        gap: 10px;
    }
    .stRadio label {
        background-color: #FFFFFF;
        padding: 15px 20px;
        border-radius: 12px;
        border: 1px solid #E0E5EC;
        font-size: 1.1rem !important;
        font-weight: 500;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
        transition: 0.2s;
    }
    .stRadio label:hover {
        border-color: #6C5CE7;
        background-color: #F8F7FF;
    }
    /* 선택된 라디오 버튼 강조 */
    .stRadio div[role="radiogroup"] > label[data-checked="true"] {
        background-color: #6C5CE7 !important;
        color: white !important;
        border: none;
    }
    .stRadio div[role="radiogroup"] > label[data-checked="true"] p {
        color: white !important;
    }

    /* 입력창 스타일 */
    .stTextInput input {
        border-radius: 12px;
        border: 2px solid #E0E5EC;
        padding: 12px;
        font-size: 1.1rem;
    }
    .stTextInput input:focus {
        border-color: #6C5CE7;
    }

    /* 알림창 스타일 */
    .stAlert {
        border-radius: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* 진행바 색상 */
    .stProgress > div > div > div > div {
        background-color: #6C5CE7;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 데이터 ---
UNITS = {
    1: "1. 분수의 나눗셈",
    2: "2. 각기둥과 각뿔",
    3: "3. 소수의 나눗셈",
    4: "4. 비와 비율"
}

# 개념 설명 (HTML 태그로 카드 스타일 적용)
CONCEPTS = {
    1: """
    <div class="card concept-card">
        <h3>🍰 분수의 나눗셈 핵심 정리</h3>
        <p><b>1. (자연수) ÷ (자연수)</b></p>
        <ul><li>나눗셈의 몫을 분수로! 뒤에 있는 수가 분모가 돼요.<br>예: $ 1 \\div 3 = \\frac{1}{3} $</li></ul>
        <p><b>2. (분수) ÷ (자연수)</b></p>
        <ul><li>나누기를 <b>곱하기 분의 1</b>로 바꿔서 계산해요.<br>예: $ \\frac{2}{3} \\div 4 = \\frac{2}{3} \\times \\frac{1}{4} = \\frac{2}{12} = \\frac{1}{6} $</li></ul>
    </div>
    """,
    2: """
    <div class="card concept-card">
        <h3>📦 각기둥과 각뿔 친구들</h3>
        <p><b>각기둥 (Prism)</b></p>
        <ul><li>위아래 면이 서로 평행하고 합동인 다각형</li><li>옆면은 모두 <b>직사각형</b> 모양!</li></ul>
        <p><b>각뿔 (Pyramid)</b></p>
        <ul><li>밑면은 다각형, 위는 뾰족한 점(각뿔의 꼭짓점)</li><li>옆면은 모두 <b>삼각형</b> 모양!</li></ul>
        <hr style="border-top: 1px dashed #ddd;">
        <p><b>💡 구성 요소 공식 (N = 밑면의 변의 수)</b></p>
        <ul>
            <li><b>각기둥</b>: 모서리(3×N), 꼭짓점(2×N), 면(N+2)</li>
            <li><b>각뿔</b>: 모서리(2×N), 꼭짓점(N+1), 면(N+1)</li>
        </ul>
    </div>
    """,
    3: """
    <div class="card concept-card">
        <h3>💧 소수의 나눗셈 비법</h3>
        <p><b>자연수처럼 계산하고 점 찍기!</b></p>
        <ol>
            <li>소수점이 없다고 생각하고 자연수의 나눗셈을 해요.</li>
            <li>나뉠 수의 원래 소수점 위치에 맞춰 몫에 점을 콕! 찍어요.</li>
        </ol>
        <p style="background-color:#F8F7FF; padding:10px; border-radius:10px;">
            <b>예시: $ 3.66 \\div 3 $</b><br>
            ① $ 366 \\div 3 = 122 $<br>
            ② 원래 위치에 점 찍기 ➡ <b>$ 1.22 $</b>
        </p>
    </div>
    """,
    4: """
    <div class="card concept-card">
        <h3>🍎 비와 비율 알아보기</h3>
        <p><b>1. 비 (Ratio)</b></p>
        <ul>
            <li>두 수를 나눗셈으로 비교할 때 <b>:</b> 기호 사용 (예: 3 : 2)</li>
            <li><b>전항</b>(앞, 비교하는 양) : <b>후항</b>(뒤, 기준량)</li>
        </ul>
        <p><b>2. 비율 (Rate)</b></p>
        <ul>
            <li>비를 분수나 소수로 나타낸 값 ($ \\frac{\\text{비교하는 양}}{\\text{기준량}} $)</li>
            <li>3 : 2 의 비율 ➡ $ \\frac{3}{2} $ 또는 $ 1.5 $</li>
        </ul>
    </div>
    """
}

# --- 3. 함수 ---
def check_answer(user_input, correct_val):
    try:
        user_str = str(user_input).strip().replace(" ", "")
        correct_str = str(correct_val).strip().replace(" ", "")
        if user_str == correct_str: return True
        
        if '/' in str(correct_val):
            n, d = map(float, str(correct_val).split('/'))
            ans_val = n / d
        else:
            ans_val = float(correct_val)

        if '/' in user_str:
            n, d = map(float, user_str.split('/'))
            user_val = n / d
        else:
            user_val = float(user_str)
            
        return abs(ans_val - user_val) < 0.001
    except:
        return False

def generate_problem(unit_num, difficulty):
    problem = {'unit': unit_num}
    q_type = 'obj' if (random.random() > 0.5 or unit_num == 2) else 'subj'
    problem['type'] = q_type
    
    if unit_num == 1:
        if difficulty == '하':
            a, b = random.randint(1, 9), random.randint(2, 9)
            if a == b: b += 1
            problem['q'] = f"몫을 분수로 나타내면? $${a} \div {b}$$"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = f"뒤에 있는 수 {b}가 분모가 됩니다."
        else:
            ja, mo, nat = random.randint(1, 9), random.randint(2, 9), random.randint(2, 5)
            problem['q'] = f"계산하시오: $$\\frac{{{ja}}}{{{mo}}} \div {nat}$$"
            problem['a'] = f"{ja}/{mo*nat}"
            problem['exp'] = f"곱하기 분의 1로 바꾸세요: {ja}/{mo} × 1/{nat}"
        if q_type == 'obj':
            opts = [problem['a'], f"{b}/{a}", f"{a+1}/{b}", f"{a}/{b+1}"]
            random.shuffle(opts)
            problem['options'] = opts
            
    elif unit_num == 2:
        shapes = [('삼각기둥',3),('사각기둥',4),('오각기둥',5),('삼각뿔',3),('사각뿔',4)]
        name, n = random.choice(shapes)
        target = random.choice(['모서리', '꼭짓점', '면'])
        is_prism = '기둥' in name
        problem['q'] = f"**{name}**의 **{target}**의 수는?"
        if is_prism: ans = n*3 if target=='모서리' else (n*2 if target=='꼭짓점' else n+2)
        else: ans = n*2 if target=='모서리' else n+1
        problem['a'] = str(ans)
        problem['exp'] = f"{name}의 밑면 변의 수는 {n}개입니다."
        if q_type == 'obj':
            opts = list(set([str(ans), str(ans+1), str(ans-1), str(ans*2), str(n)]))
            random.shuffle(opts)
            problem['options'] = opts[:4]

    elif unit_num == 3:
        d, q = random.randint(2, 5), random.randint(11, 99)
        problem['q'] = f"계산하시오: $${q*d/10} \div {d}$$"
        problem['a'] = str(q/10)
        problem['exp'] = f"자연수 계산 {q*d}÷{d}={q} 후, 소수점을 찍으세요."
        if q_type == 'obj':
            opts = [str(q/10), str(q), str(q/100), str((q+1)/10)]
            random.shuffle(opts)
            problem['options'] = opts

    elif unit_num == 4:
        a, b = random.randint(2, 9), random.randint(3, 9)
        if random.random() > 0.5:
            problem['q'] = f"비 {a}:{b}의 **비율**을 분수로 나타내면?"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = "비율 = 비교하는 양(앞) / 기준량(뒤)"
            if q_type == 'obj': problem['options'] = [f"{a}/{b}", f"{b}/{a}", f"1/{a}", f"1/{b}"]
        else:
            problem['q'] = f"비 5:8에서 **기준량**(후항)은?"
            problem['a'] = "8"
            problem['exp'] = "비 기호(:) 뒤에 있는 수가 기준량입니다."
            if q_type == 'obj': problem['options'] = ["5", "8", "13", "3"]
        if q_type == 'obj': random.shuffle(problem['options'])

    return problem

# --- 4. 메인 앱 ---
def main():
    st.set_page_config(page_title="스마트 초등 수학", page_icon="📘", layout="wide")
    apply_custom_style()

    if 'step' not in st.session_state: st.session_state.step = 'intro'
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
    if 'current_prob' not in st.session_state: st.session_state.current_prob = None
    if 'solved' not in st.session_state: st.session_state.solved = False
    if 'wrong_notes' not in st.session_state: st.session_state.wrong_notes = []
    if 'current_unit' not in st.session_state: st.session_state.current_unit = 1

    # ================= 사이드바 =================
    with st.sidebar:
        st.title("나의 학습실 🎒")
        st.markdown("### 📘 단원 선택")
        # 커스텀 스타일이 적용된 라디오 버튼
        selected_label = st.radio(
            "학습할 단원을 골라보세요:",
            list(UNITS.values()),
            index=st.session_state.current_unit - 1,
            label_visibility="collapsed"
        )
        new_unit = [k for k, v in UNITS.items() if v == selected_label][0]
        if new_unit != st.session_state.current_unit:
            st.session_state.current_unit = new_unit
            st.session_state.step = 'intro'
            st.session_state.score = 0
            st.rerun()

        st.markdown("---")
        wrong_cnt = len(st.session_state.wrong_notes)
        if wrong_cnt > 0:
            st.markdown(f"""
            <div class="card" style="padding: 15px; background-color: #F8F7FF; border:1px solid #6C5CE7;">
                <h4 style="margin:0; color:#6C5CE7;">❌ 오답 노트 ({wrong_cnt})</h4>
                <p style="font-size:0.9rem;">틀린 문제를 복습해보세요!</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("📝 오답 확인하기"):
                st.session_state.step = 'wrong_note_view'
                st.rerun()
        
        st.markdown("---")
        if st.button("🏠 홈으로 가기"):
            st.session_state.step = 'intro'
            st.rerun()

    # ================= 메인 콘텐츠 =================
    u_name = UNITS[st.session_state.current_unit]

    # [Intro] 개념 학습
    if st.session_state.step == 'intro':
        st.markdown(f"<h1>오늘의 학습: {u_name.split('. ')[1]}</h1>", unsafe_allow_html=True)
        st.markdown(CONCEPTS[st.session_state.current_unit], unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 개념 탑재 완료! 문제 풀기 Start", use_container_width=True):
            st.session_state.step = 'quiz'
            st.session_state.q_idx = 0
            st.session_state.score = 0
            st.session_state.current_prob = None
            st.session_state.solved = False
            st.rerun()

    # [Quiz] 문제 풀이
    elif st.session_state.step == 'quiz':
        total_q = 5
        st.markdown(f"<h3>📘 {u_name} 실력 점검</h3>", unsafe_allow_html=True)
        st.progress((st.session_state.q_idx) / total_q, text=f"진행률: {st.session_state.q_idx+1}/{total_q}")

        if st.session_state.current_prob is None:
            st.session_state.current_prob = generate_problem(st.session_state.current_unit, random.choice(['중','상']))
            st.session_state.solved = False
        prob = st.session_state.current_prob
        
        # 문제 카드
        st.markdown(f"""
        <div class="card quiz-card">
            <h4 style="color:#555;">Q{st.session_state.q_idx + 1}. 다음 문제를 풀어보세요.</h4>
            <h3 style="color:#333; font-size:1.5rem;">{prob['q']}</h3>
        </div>
        """, unsafe_allow_html=True)

        with st.form(key=f"q_form_{st.session_state.q_idx}"):
            if prob['type'] == 'obj':
                user_val = st.radio("정답 선택:", prob['options'], index=None, disabled=st.session_state.solved, label_visibility="collapsed")
            else:
                user_val = st.text_input("정답을 입력하세요:", disabled=st.session_state.solved)
            
            btn_txt = "다음 문제로 넘어가기 ➡️" if st.session_state.solved else "채점하기 ✨"
            submit = st.form_submit_button(btn_txt, use_container_width=True)

        if submit:
            if not st.session_state.solved:
                if not user_val: st.warning("정답을 입력해주세요!")
                else:
                    if check_answer(user_val, prob['a']):
                        st.balloons()
                        st.success("정답입니다! 훌륭해요! 🎉")
                        st.session_state.score += 1
                    else:
                        st.error("아쉽게도 틀렸습니다. 😢")
                        st.markdown(f"""<div class="card" style="background-color:#FFF5F5; border-color:#FF6B6B;">
                            <b>정답: {prob['a']}</b><br>💡 해설: {prob['exp']}</div>""", unsafe_allow_html=True)
                        if prob not in st.session_state.wrong_notes:
                            prob['user_wrong'] = user_val
                            st.session_state.wrong_notes.append(prob)
                    st.session_state.solved = True
                    st.rerun()
            else:
                st.session_state.q_idx += 1
                st.session_state.current_prob = None
                st.session_state.solved = False
                if st.session_state.q_idx >= total_q: st.session_state.step = 'result'
                st.rerun()

    # [Result] 결과 화면
    elif st.session_state.step == 'result':
        final_score = st.session_state.score * 20
        st.markdown("""<h1>🏆 학습 결과 리포트</h1>""", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <h2 style="font-size:3rem; color:#6C5CE7;">{final_score}점</h2>
            <p>{'와우! 완벽하게 이해했네요! 👏' if final_score==100 else '참 잘했어요! 조금만 더 힘내봐요! 💪'}</p>
        </div>
        """, unsafe_allow_html=True)

        if final_score < 100:
            st.info("💡 Tip: 오답 노트를 확인하면 실력이 더 쑥쑥 오를 거예요!")

    # [Wrong Note] 오답 노트
    elif st.session_state.step == 'wrong_note_view':
        st.markdown("<h1>📝 내 오답 노트</h1>", unsafe_allow_html=True)
        for i, note in enumerate(st.session_state.wrong_notes):
            with st.expander(f"🔍 {i+1}번 문제 다시보기 (클릭)"):
                st.markdown(f"""
                <div class="card quiz-card">
                    <p><b>문제:</b> {note['q']}</p>
                    <p style="color:#FF6B6B;"><b>내가 쓴 답:</b> {note.get('user_wrong','?')}</p>
                    <p style="color:#6C5CE7;"><b>정답: {note['a']}</b></p>
                    <p style="background-color:#F8F7FF; padding:10px; border-radius:10px;"><b>💡 해설:</b> {note['exp']}</p>
                </div>
                """, unsafe_allow_html=True)
        if st.button("🔙 학습 화면으로 돌아가기", use_container_width=True):
            st.session_state.step = 'intro'
            st.rerun()

if __name__ == "__main__":
    main()
