import streamlit as st
import random

# --- 1. 🎨 디자인 & 폰트 절대 사수 (3중 안전장치) ---
def apply_custom_style():
    st.markdown("""
    <style>
    /* 1. 웹 폰트 로딩 (Jua: 제목용, Noto Sans: 본문용) */
    @import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;700&display=swap');

    /* 2. 폰트 강제 적용 순서 (웹폰트 실패 시 -> 기기 기본 폰트 사용) */
    html, body, [class*="css"], font, div, p, span, h1, h2, h3, h4, h5, h6 {
        font-family: 'Jua', 'Noto Sans KR', 'Apple SD Gothic Neo', 'Malgun Gothic', 'Nanum Gothic', sans-serif !important;
        color: #333333;
    }

    /* 배경: 아주 연한 보라빛 회색 (눈 편안함) */
    .stApp {
        background-color: #F3F4F6;
    }

    /* ----------------- 카드 UI (상용 앱 스타일) ----------------- */
    .main-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #E5E7EB;
    }

    /* 제목 스타일 */
    .title-text {
        font-family: 'Jua', sans-serif !important;
        color: #6C5CE7; /* 예쁜 보라색 */
        font-size: 2.2rem;
        text-shadow: 2px 2px 0px #E0E0E0;
        margin-bottom: 10px;
    }

    /* 강조 박스 */
    .highlight-box {
        background-color: #F5F3FF; /* 연한 보라 배경 */
        border-left: 5px solid #6C5CE7;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }

    /* 버튼 스타일 (그라데이션 젤리 버튼) */
    .stButton>button {
        background: linear-gradient(90deg, #6C5CE7, #8076EE);
        color: white !important;
        border: none;
        border-radius: 15px;
        padding: 12px 0;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(108, 92, 231, 0.3);
        transition: transform 0.2s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 15px rgba(108, 92, 231, 0.4);
    }
    
    /* 사이드바 스타일 개선 */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E5E7EB;
    }

    /* 라디오 버튼 (선택지) 스타일 */
    .stRadio label {
        background: white;
        padding: 12px;
        border-radius: 10px;
        border: 2px solid #F3F4F6;
        margin-bottom: 5px;
        transition: 0.3s;
        font-size: 1.05rem !important;
    }
    .stRadio label:hover {
        border-color: #6C5CE7;
        background-color: #F5F3FF;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 📚 데이터: 상세한 개념 설명 & 문제 ---
UNITS = {
    1: "1. 분수의 나눗셈",
    2: "2. 각기둥과 각뿔",
    3: "3. 소수의 나눗셈",
    4: "4. 비와 비율"
}

# HTML을 활용해 예쁘게 꾸민 개념 설명
CONCEPTS = {
    1: """
    <div class="main-card">
        <h3 style="color:#6C5CE7;">🍰 분수의 나눗셈, 이렇게 이해해요!</h3>
        <p><b>1. (자연수) ÷ (자연수)</b></p>
        <p>"피자 1판을 3명이 똑같이 나누어 먹는 상황을 상상해봐요."<br>
        한 사람이 먹는 양은 3조각 중의 1조각이죠? 그래서 <b>1/3</b>입니다.</p>
        <div class="highlight-box">
            <b>💡 공식 암기:</b><br>
            뒤에 있는 수(나누는 수)가 <b>분모(아래)</b>로 슝! 내려가요.<br>
            $$ 1 \div 3 = \\frac{1}{3} $$
        </div>
        <br>
        <p><b>2. (분수) ÷ (자연수)</b></p>
        <p>나누기는 <b>'곱하기 분의 1'</b>로 변신할 수 있어요.<br>
        "4로 나눈다"는 말은 "4등분 한 것 중의 하나(1/4)를 가진다"는 뜻이니까요.</p>
        <div class="highlight-box">
            <b>📝 예시 문제:</b><br>
            $$ \\frac{4}{5} \div 2 $$ <br>
            ① 나누기를 곱하기로 변신! ➡ $$ \\frac{4}{5} \\times \\frac{1}{2} $$ <br>
            ② 분모는 분모끼리, 분자는 분자끼리! ➡ $$ \\frac{4}{10} $$ <br>
            ③ 약분하면 끝! ➡ $$ \\frac{2}{5} $$
        </div>
    </div>
    """,
    2: """
    <div class="main-card">
        <h3 style="color:#6C5CE7;">📦 각기둥과 각뿔 구분하기</h3>
        <p><b>🏢 각기둥 (아파트 모양)</b></p>
        <ul>
            <li>위 뚜껑과 아래 바닥이 <b>똑같이 생겼고 평행</b>해요.</li>
            <li>옆에서 보면 반듯한 <b>직사각형</b> 모양이에요.</li>
        </ul>
        <p><b>⛺ 각뿔 (텐트 모양)</b></p>
        <ul>
            <li>바닥은 평평하지만 위는 <b>뾰족한 점</b>으로 모여요.</li>
            <li>옆에서 보면 <b>삼각형</b> 모양이에요.</li>
        </ul>
        <div class="highlight-box">
            <b>⚡ 구성 요소 공식 (N = 밑면의 변의 수)</b><br>
            <table style="width:100%; text-align:center;">
                <tr><td>구분</td><td>모서리</td><td>꼭짓점</td></tr>
                <tr><td><b>각기둥</b></td><td>N × 3</td><td>N × 2</td></tr>
                <tr><td><b>각뿔</b></td><td>N × 2</td><td>N + 1</td></tr>
            </table>
            <br>Tip: 기둥이 뿔보다 재료(모서리, 꼭짓점)가 더 많이 필요해요!
        </div>
    </div>
    """,
    3: """
    <div class="main-card">
        <h3 style="color:#6C5CE7;">💧 소수의 나눗셈 비법</h3>
        <p><b>"점은 나중에 찍자!"</b></p>
        <p>소수점이 있으면 어렵죠? 잠시 점을 없애고 <b>자연수처럼</b> 계산하세요.</p>
        <div class="highlight-box">
            <b>🔎 예시: $$ 3.66 \div 3 $$</b><br>
            1. 점 숨기기: $$ 366 \div 3 = 122 $$ <br>
            2. 점 다시 찍기: 원래 점이 두 칸 앞에 있었죠?<br>
            정답도 똑같이 두 칸 앞에 점을 콕! ➡ <b>1.22</b>
        </div>
    </div>
    """,
    4: """
    <div class="main-card">
        <h3 style="color:#6C5CE7;">🍎 비와 비율</h3>
        <p><b>1. 비 (Ratio)</b></p>
        <p>사과 3개와 배 2개를 비교할 때 <b>3 : 2</b> 라고 씁니다.<br>
        왼쪽(3)이 <b>비교하는 양</b>, 오른쪽(2)이 <b>기준량</b>입니다.</p>
        <div class="highlight-box">
            <b>2. 비율 (Rate)</b><br>
            비를 분수나 소수로 나타낸 값이에요.<br>
            $$ \\text{비율} = \\frac{\\text{비교하는 양(앞)}}{\\text{기준량(뒤)}} $$
        </div>
    </div>
    """
}

# --- 3. 핵심 로직 (정답 체크 & 문제 생성) ---
def check_answer(user_input, correct_val):
    try:
        user_str = str(user_input).strip().replace(" ", "")
        correct_str = str(correct_val).strip().replace(" ", "")
        
        # 텍스트 일치
        if user_str == correct_str: return True
        
        # 수치 일치 (분수/소수)
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
    # 2단원은 객관식이 더 적합, 나머지는 반반
    q_type = 'obj' if (random.random() > 0.5 or unit_num == 2) else 'subj'
    problem['type'] = q_type
    
    # [1단원]
    if unit_num == 1:
        if difficulty == '하':
            a, b = random.randint(1, 8), random.randint(2, 9)
            if a >= b: b = a + 1
            problem['q'] = f"피자 {a}판을 {b}명이 나누어 먹습니다. 한 사람의 양은?"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = f"전체({a}) ÷ 사람수({b}) = {a}/{b}"
        else:
            ja, mo, nat = random.randint(1, 9), random.randint(2, 9), random.randint(2, 5)
            problem['q'] = f"계산하시오: $$\\frac{{{ja}}}{{{mo}}} \div {nat}$$"
            problem['a'] = f"{ja}/{mo*nat}"
            problem['exp'] = f"나누기를 곱하기 1/{nat}로 바꿔서 분모끼리 곱해요."
            
        if q_type == 'obj':
            opts = [problem['a'], f"{mo}/{ja}", f"{ja}/{nat}", f"{nat}/{ja}"]
            random.shuffle(opts)
            problem['options'] = opts

    # [2단원]
    elif unit_num == 2:
        shapes = [('삼각기둥',3,'기둥'),('사각기둥',4,'기둥'),('오각기둥',5,'기둥'),('삼각뿔',3,'뿔'),('사각뿔',4,'뿔')]
        name, n, kind = random.choice(shapes)
        target = random.choice(['모서리', '꼭짓점', '면'])
        problem['q'] = f"**{name}**의 **{target}** 수는 몇 개일까요?"
        
        if kind == '기둥':
            ans = n*3 if target=='모서리' else (n*2 if target=='꼭짓점' else n+2)
        else:
            ans = n*2 if target=='모서리' else n+1
        
        problem['a'] = str(ans)
        problem['exp'] = f"{name}의 밑면 변은 {n}개입니다. 공식을 적용해보세요!"
        
        if q_type == 'obj':
            opts = list(set([str(ans), str(ans+1), str(ans-1), str(n*2), str(n*3)]))[:4]
            while len(opts) < 4: opts.append(str(random.randint(5,20)))
            random.shuffle(opts)
            problem['options'] = opts

    # [3단원]
    elif unit_num == 3:
        d = random.randint(2, 5)
        q = random.randint(12, 88)
        dividend = q * d 
        problem['q'] = f"계산하시오: $${dividend/100} \div {d}$$"
        problem['a'] = str(q/100)
        problem['exp'] = f"자연수 {dividend}÷{d}={q} 계산 후 소수점을 2칸 앞으로!"
        if q_type == 'obj':
            opts = [str(q/100), str(q/10), str(q), str(q/1000)]
            random.shuffle(opts)
            problem['options'] = opts

    # [4단원]
    elif unit_num == 4:
        a, b = random.randint(2, 9), random.randint(3, 9)
        if random.random() > 0.5:
            problem['q'] = f"비 {a}:{b}를 비율(분수)로 나타내면?"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = "비율 = 비교하는 양(앞) / 기준량(뒤)"
            if q_type == 'obj': problem['options'] = [f"{a}/{b}", f"{b}/{a}", f"1/{b}", f"{a+b}"]
        else:
            problem['q'] = f"비 {a}:{b}에서 **기준량**은?"
            problem['a'] = str(b)
            problem['exp'] = "비 기호 뒤에 있는 수가 기준량입니다."
            if q_type == 'obj': problem['options'] = [str(a), str(b), str(a+b), "1"]
        
        if q_type == 'obj' and 'options' in problem: random.shuffle(problem['options'])

    return problem

# --- 4. 메인 앱 실행 ---
def main():
    st.set_page_config(page_title="스마트 수학 학습", page_icon="✏️", layout="wide")
    apply_custom_style() # 스타일 적용

    # 세션 상태 초기화 (새로고침 해도 데이터 유지)
    if 'step' not in st.session_state: st.session_state.step = 'intro'
    if 'current_unit' not in st.session_state: st.session_state.current_unit = 1
    if 'wrong_notes' not in st.session_state: st.session_state.wrong_notes = []
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
    if 'current_prob' not in st.session_state: st.session_state.current_prob = None
    if 'solved' not in st.session_state: st.session_state.solved = False

    # ================= 사이드바 (Nav) =================
    with st.sidebar:
        st.markdown("<h2 style='color:#6C5CE7; font-family:Jua;'>🏫 나의 학습실</h2>", unsafe_allow_html=True)
        
        # 1. 단원 선택
        st.write("---")
        st.markdown("**📘 단원 선택**")
        unit_labels = list(UNITS.values())
        current_label = UNITS[st.session_state.current_unit]
        
        selected = st.radio(
            "단원 목록",
            unit_labels,
            index=unit_labels.index(current_label),
            label_visibility="collapsed"
        )
        
        # 단원 변경 감지
        new_unit = [k for k, v in UNITS.items() if v == selected][0]
        if new_unit != st.session_state.current_unit:
            st.session_state.current_unit = new_unit
            st.session_state.step = 'intro'
            st.session_state.score = 0
            st.rerun()

        # 2. 오답 노트 (항상 표시)
        st.write("---")
        st.markdown(f"**📝 오답 노트 ({len(st.session_state.wrong_notes)})**")
        if len(st.session_state.wrong_notes) > 0:
            if st.button("오답 문제 풀기"):
                st.session_state.step = 'wrong_note_view'
                st.rerun()
        else:
            st.caption("틀린 문제가 없습니다. 👍")

        st.write("---")
        if st.button("🏠 홈으로"):
            st.session_state.step = 'intro'
            st.rerun()

    # ================= 메인 콘텐츠 =================
    unit_name = UNITS[st.session_state.current_unit]

    # [1] 개념 학습 화면
    if st.session_state.step == 'intro':
        st.markdown(f"<div class='title-text'>오늘의 학습: {unit_name.split('. ')[1]}</div>", unsafe_allow_html=True)
        
        # 개념 카드 표시
        st.markdown(CONCEPTS[st.session_state.current_unit], unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 개념 완료! 문제 풀기 Start", use_container_width=True):
                st.session_state.step = 'quiz'
                st.session_state.q_idx = 0
                st.session_state.score = 0
                st.session_state.current_prob = None
                st.session_state.solved = False
                st.rerun()

    # [2] 퀴즈 화면
    elif st.session_state.step == 'quiz':
        total_q = 5
        st.markdown(f"### ✏️ 실력 점검 ({st.session_state.q_idx + 1}/{total_q})")
        st.progress((st.session_state.q_idx) / total_q)

        # 문제 생성
        if st.session_state.current_prob is None:
            st.session_state.current_prob = generate_problem(st.session_state.current_unit, '중')
            st.session_state.solved = False
        
        prob = st.session_state.current_prob
        
        # 문제 카드
        st.markdown(f"""
        <div class="main-card">
            <h4 style="color:#666;">Q{st.session_state.q_idx + 1}.</h4>
            <h3 style="margin-top:5px; color:#333;">{prob['q']}</h3>
        </div>
        """, unsafe_allow_html=True)

        with st.form(key=f"q_form_{st.session_state.q_idx}"):
            if prob['type'] == 'obj':
                user_val = st.radio("정답 선택:", prob['options'], index=None, disabled=st.session_state.solved)
            else:
                user_val = st.text_input("정답 입력:", disabled=st.session_state.solved)
            
            btn_text = "다음 문제 ➡️" if st.session_state.solved else "채점하기 ✨"
            submit = st.form_submit_button(btn_text, use_container_width=True)

        if submit:
            if not st.session_state.solved:
                if not user_val:
                    st.warning("정답을 입력해주세요!")
                else:
                    if check_answer(user_val, prob['a']):
                        st.balloons()
                        st.success("정답입니다! 🎉")
                        st.session_state.score += 1
                    else:
                        st.error("틀렸습니다. 😢")
                        st.markdown(f"""
                        <div class="highlight-box" style="background-color:#FFF5F5; border-color:#FF6B6B;">
                            <b>정답: {prob['a']}</b><br>
                            해설: {prob['exp']}
                        </div>
                        """, unsafe_allow_html=True)
                        # 오답노트 저장
                        if prob not in st.session_state.wrong_notes:
                            prob['user_wrong'] = user_val
                            st.session_state.wrong_notes.append(prob)
                    
                    st.session_state.solved = True
                    st.rerun()
            else:
                st.session_state.q_idx += 1
                st.session_state.current_prob = None
                st.session_state.solved = False
                if st.session_state.q_idx >= total_q:
                    st.session_state.step = 'result'
                st.rerun()

    # [3] 결과 화면
    elif st.session_state.step == 'result':
        final_score = st.session_state.score * 20
        st.markdown("<div class='title-text'>🏆 학습 결과</div>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="main-card" style="text-align:center;">
            <h1 style="color:#6C5CE7; font-size:4rem; margin:0;">{final_score}점</h1>
            <p style="font-size:1.5rem; margin-top:10px;">
                {'완벽해요! 참 잘했어요! 🎓' if final_score == 100 else '수고했어요! 오답 노트로 복습해봐요 💪'}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        if col1.button("다시 풀기 🔄", use_container_width=True):
            st.session_state.step = 'intro'
            st.rerun()
        if len(st.session_state.wrong_notes) > 0:
            if col2.button("오답 노트 확인 📝", use_container_width=True):
                st.session_state.step = 'wrong_note_view'
                st.rerun()

    # [4] 오답 노트 화면
    elif st.session_state.step == 'wrong_note_view':
        st.markdown("<div class='title-text'>📝 내 오답 노트</div>", unsafe_allow_html=True)
        
        if not st.session_state.wrong_notes:
            st.info("오답 노트가 비어있어요. 모두 맞혔군요! 👍")
        
        for i, note in enumerate(st.session_state.wrong_notes):
            with st.expander(f"🔍 {i+1}번 문제 다시보기"):
                st.markdown(f"""
                <div class="main-card" style="padding:15px; border-left: 5px solid #FF7675;">
                    <p><b>문제:</b> {note['q']}</p>
                    <p style="color:#E03131;"><b>내가 쓴 답:</b> {note.get('user_wrong','?')}</p>
                    <p style="color:#2F9E44;"><b>정답: {note['a']}</b></p>
                    <p style="background:#F1F3F5; padding:10px; border-radius:5px;"><b>💡 해설:</b> {note['exp']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        if st.button("🔙 돌아가기", use_container_width=True):
            st.session_state.step = 'intro'
            st.rerun()

if __name__ == "__main__":
    main()
