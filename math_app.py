import streamlit as st
import random

# --- 1. 🎨 스타일 설정 (폰트 깨짐 방지 & UI) ---
def apply_custom_style():
    st.markdown("""
    <style>
    /* 1. 폰트 로드: Noto Sans KR (웹폰트) */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Jua&display=swap');
    
    /* 2. 폰트 적용 순서 (안전장치 강화) */
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', 'Dotum', sans-serif !important;
        background-color: #F0F2F5 !important;
        color: #333333 !important;
    }
    
    /* 제목 스타일 (주아체 포인트) */
    h1, h2, h3 {
        font-family: 'Jua', 'Noto Sans KR', sans-serif !important;
    }

    /* 카드형 UI 스타일 */
    .card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        border: 1px solid #E1E4E8;
    }
    
    /* 개념 설명 카드 스타일 */
    .concept-card {
        border-left: 6px solid #6C5CE7;
        background: linear-gradient(to right, #FFFFFF, #F8F7FF);
    }
    
    /* 퀴즈 카드 스타일 */
    .quiz-card {
        border-top: 6px solid #FF7675;
    }

    /* 버튼 스타일 */
    .stButton>button {
        background: linear-gradient(90deg, #6C5CE7, #8176EE);
        color: white !important;
        border-radius: 12px;
        border: none;
        padding: 12px;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(108, 92, 231, 0.2);
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(108, 92, 231, 0.3);
    }

    /* 사이드바 스타일 */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E0E0E0;
    }
    
    /* 선택지(라디오 버튼) 디자인 */
    .stRadio label {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #DDD;
        margin-bottom: 8px;
        font-size: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .stRadio label:hover {
        border-color: #6C5CE7;
        background-color: #F4F1FF;
    }

    /* 경고/알림창 */
    .stAlert {
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 📚 데이터: 친절한 개념 설명 (예시 포함) ---
UNITS = {
    1: "1. 분수의 나눗셈",
    2: "2. 각기둥과 각뿔",
    3: "3. 소수의 나눗셈",
    4: "4. 비와 비율"
}

CONCEPTS = {
    1: """
    <div class="card concept-card">
        <h3>🍰 1. 분수의 나눗셈, 이렇게 이해해요!</h3>
        <p><b>① 자연수 ÷ 자연수</b></p>
        <p style="color:#555; font-size:0.95rem;">
            "피자 1판을 3명이 똑같이 나누어 먹으려면?"<br>
            한 사람이 먹는 양은 <b>3조각 중의 1조각</b>이죠? 그래서 1/3입니다.
        </p>
        <div style="background:#EFEFFF; padding:10px; border-radius:10px;">
            <b>💡 공식:</b> 나누는 수(뒤에 있는 수)가 <b>분모</b>로 슝! 내려가요.<br>
            $$ 1 \div 3 = \\frac{1}{3} $$ <br>
            $$ 5 \div 4 = \\frac{5}{4} = 1\\frac{1}{4} $$
        </div>
        <br>
        <p><b>② 분수 ÷ 자연수</b></p>
        <p style="color:#555; font-size:0.95rem;">
            나누기는 <b>'곱하기 분의 1'</b>로 변신할 수 있어요.<br>
            "4로 나눈다"는 말은 "4등분 한 것 중의 하나(1/4)를 곱한다"는 뜻과 같아요.
        </p>
        <div style="background:#FFF0F0; padding:10px; border-radius:10px;">
            <b>💡 예시 문제:</b><br>
            $$ \\frac{4}{5} \div 2 $$ <br>
            = $$ \\frac{4}{5} \\times \\frac{1}{2} $$ (나누기를 곱하기로 변신!)<br>
            = $$ \\frac{4 \\times 1}{5 \\times 2} = \\frac{4}{10} $$ <br>
            = $$ \\frac{2}{5} $$ (약분까지 깔끔하게!)
        </div>
    </div>
    """,
    2: """
    <div class="card concept-card">
        <h3>📦 2. 각기둥과 각뿔 구별하기</h3>
        <p><b>🏢 각기둥 (아파트 같은 모양)</b></p>
        <ul>
            <li>위 뚜껑과 아래 바닥이 <b>똑같은 모양</b>이고 <b>평행</b>해요.</li>
            <li>옆에서 보면 <b>직사각형</b> 모양이에요.</li>
            <li>이름 짓기: 밑면이 삼각형이면 삼각기둥, 사각형이면 사각기둥!</li>
        </ul>
        <br>
        <p><b>⛺ 각뿔 (텐트 같은 모양)</b></p>
        <ul>
            <li>바닥은 평평하지만 위는 <b>뾰족한 점</b>으로 모여요.</li>
            <li>옆에서 보면 <b>삼각형</b> 모양이에요.</li>
        </ul>
        <div style="background:#FFF9DB; padding:10px; border-radius:10px; margin-top:10px;">
            <b>⚡ 마법 공식 (N = 밑면의 변의 수)</b><br>
            <table style="width:100%; border-collapse: collapse;">
                <tr><td style="border-bottom:1px solid #ddd;">구분</td><td style="border-bottom:1px solid #ddd;">모서리</td><td style="border-bottom:1px solid #ddd;">꼭짓점</td></tr>
                <tr><td><b>각기둥</b></td><td>N × 3</td><td>N × 2</td></tr>
                <tr><td><b>각뿔</b></td><td>N × 2</td><td>N + 1</td></tr>
            </table>
            <p style="font-size:0.8rem; margin-top:5px;">팁: 기둥이 뿔보다 재료(모서리, 꼭짓점)가 더 많이 필요해요!</p>
        </div>
    </div>
    """,
    3: """
    <div class="card concept-card">
        <h3>💧 3. 소수의 나눗셈 비법</h3>
        <p><b>"점은 나중에 생각하자!"</b></p>
        <p>소수점이 있으면 계산하기 복잡해 보이죠? <br>
        잠깐 점을 없애고 <b>자연수처럼</b> 계산한 뒤, 마지막에 제자리에 찍어주면 돼요.</p>
        <div style="background:#E3FAFC; padding:15px; border-radius:10px;">
            <b>🔎 예시: $$ 3.66 \div 3 $$</b><br>
            <ol style="margin-left:20px; padding-left:0;">
                <li><b>점을 숨겨요:</b> $$ 366 \div 3 $$ 을 계산합니다.<br>
                $$ \Rightarrow 122 $$ </li>
                <li><b>점을 다시 찍어요:</b> 원래 소수점이 두 칸 앞에 있었죠? (3.<b>66</b>)<br>
                정답도 뒤에서 두 칸 앞에 점을 콕!<br>
                $$ \Rightarrow 1.22 $$</li>
            </ol>
        </div>
        <p style="margin-top:10px;"><b>주의할 점:</b> 몫의 소수점은 <b>나뉠 수의 소수점 자리</b> 그대로 위로 올라가서 찍혀요.</p>
    </div>
    """,
    4: """
    <div class="card concept-card">
        <h3>🍎 4. 비와 비율이 뭐예요?</h3>
        <p><b>① 비 (Ratio) - "누가 더 많나?"</b></p>
        <p>사과 3개와 배 2개를 비교하고 싶을 때,<br>
        <b>3 : 2</b> 라고 쓰고 <b>"3 대 2"</b>라고 읽어요.</p>
        <ul>
            <li>기호 왼쪽(3): <b>비교하는 양</b> (주인공)</li>
            <li>기호 오른쪽(2): <b>기준량</b> (기준이 되는 친구)</li>
        </ul>
        <br>
        <p><b>② 비율 (Rate) - "얼마나 차지하나?"</b></p>
        <p>비를 분수나 소수로 계산한 값이에요.</p>
        <div style="background:#FFF0F6; padding:10px; border-radius:10px;">
            $$ \\text{비율} = \\frac{\\text{비교하는 양(앞)}}{\\text{기준량(뒤)}} $$ <br><br>
            예) 3 : 2 의 비율은? $$ \\frac{3}{2} = 1.5 $$ <br>
            예) 1 : 2 의 비율은? $$ \\frac{1}{2} = 0.5 = 50\\% $$
        </div>
    </div>
    """
}

# --- 3. 핵심 로직 함수 ---
def check_answer(user_input, correct_val):
    try:
        user_str = str(user_input).strip().replace(" ", "")
        correct_str = str(correct_val).strip().replace(" ", "")
        
        # 1. 문자열 완전 일치 확인
        if user_str == correct_str: return True
        
        # 2. 수치 변환 비교 (분수/소수 유연하게)
        def parse_val(v):
            if '/' in str(v):
                n, d = map(float, str(v).split('/'))
                return n / d
            return float(v)

        return abs(parse_val(correct_val) - parse_val(user_str)) < 0.001
    except:
        return False

def generate_problem(unit_num, difficulty):
    problem = {'unit': unit_num}
    # 문제 유형 랜덤 (객관식 50%, 주관식 50%)
    # 단, 2단원(도형)은 객관식이 풀기 편하므로 확률 높임
    q_type = 'obj' if (random.random() > 0.4 or unit_num == 2) else 'subj'
    problem['type'] = q_type
    
    if unit_num == 1:
        if difficulty == '하':
            a, b = random.randint(1, 8), random.randint(2, 9)
            if a >= b: b = a + 1 # 진분수 유도
            problem['q'] = f"피자 {a}판을 {b}명이 나누어 먹습니다. 한 사람이 먹게 되는 양은?"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = f"전체({a})를 사람 수({b})로 나누면 분모가 {b}가 됩니다."
        else:
            ja, mo, nat = random.randint(1, 9), random.randint(2, 9), random.randint(2, 5)
            problem['q'] = f"계산해 보세요: $$\\frac{{{ja}}}{{{mo}}} \div {nat}$$"
            problem['a'] = f"{ja}/{mo*nat}"
            problem['exp'] = f"나누기 {nat} ➡ 곱하기 1/{nat}로 바꿔보세요. 분모끼리 곱하면 됩니다."
            
        if q_type == 'obj':
            opts = [problem['a'], f"{mo}/{ja}", f"{ja}/{nat}", f"{nat}/{mo}"]
            random.shuffle(opts)
            problem['options'] = opts

    elif unit_num == 2:
        shapes = [
            ('삼각기둥',3,'기둥'), ('사각기둥',4,'기둥'), ('오각기둥',5,'기둥'),
            ('삼각뿔',3,'뿔'), ('사각뿔',4,'뿔'), ('오각뿔',5,'뿔')
        ]
        name, n, s_type = random.choice(shapes)
        target = random.choice(['모서리', '꼭짓점', '면'])
        
        problem['q'] = f"**{name}**의 **{target}** 개수는 몇 개일까요?"
        
        if s_type == '기둥':
            ans = n*3 if target=='모서리' else (n*2 if target=='꼭짓점' else n+2)
        else: # 뿔
            ans = n*2 if target=='모서리' else n+1
            
        problem['a'] = str(ans)
        problem['exp'] = f"{name}의 밑면 변의 수는 {n}개입니다. {target} 구하는 공식을 적용해 보세요!"
        
        if q_type == 'obj':
            opts = list(set([str(ans), str(ans+1), str(ans-1), str(n*2), str(n*3)]))[:4]
            while len(opts) < 4: opts.append(str(random.randint(5, 20)))
            random.shuffle(opts)
            problem['options'] = opts

    elif unit_num == 3:
        d = random.randint(2, 5)
        q = random.randint(12, 88)
        dividend = q * d 
        problem['q'] = f"계산하시오: $${dividend/100} \div {d}$$" # 예: 1.44 / 2
        problem['a'] = str(q/100)
        problem['exp'] = f"먼저 {dividend} ÷ {d} = {q} 를 계산하고, 소수점을 두 칸 앞으로 옮기세요."
        
        if q_type == 'obj':
            opts = [str(q/100), str(q/10), str(q), str(q/1000)]
            random.shuffle(opts)
            problem['options'] = opts

    elif unit_num == 4:
        a, b = random.randint(2, 9), random.randint(3, 10)
        if random.random() > 0.5:
            problem['q'] = f"비 {a}:{b} 를 비율(분수)로 나타내면?"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = "비율 = (비교하는 양) / (기준량) 입니다."
            if q_type == 'obj': problem['options'] = [f"{a}/{b}", f"{b}/{a}", f"1/{b}", f"{a+b}"]
        else:
            problem['q'] = f"비 7:10 에서 **비교하는 양**(전항)은 무엇입니까?"
            problem['a'] = "7"
            problem['exp'] = "비 기호(:)의 앞에 있는 수가 비교하는 양입니다."
            if q_type == 'obj': problem['options'] = ["7", "10", "17", "3"]
            
        if q_type == 'obj' and 'options' in problem: 
            random.shuffle(problem['options'])

    return problem

# --- 4. 메인 앱 ---
def main():
    st.set_page_config(page_title="스마트 초등 수학", page_icon="🏫", layout="wide")
    apply_custom_style()

    # 세션 초기화
    if 'step' not in st.session_state: st.session_state.step = 'intro'
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
    if 'current_prob' not in st.session_state: st.session_state.current_prob = None
    if 'solved' not in st.session_state: st.session_state.solved = False
    if 'wrong_notes' not in st.session_state: st.session_state.wrong_notes = []
    if 'current_unit' not in st.session_state: st.session_state.current_unit = 1

    # ================= 사이드바 =================
    with st.sidebar:
        st.markdown("<h2 style='color:#6C5CE7;'>🏫 나의 학습실</h2>", unsafe_allow_html=True)
        
        # 1. 단원 선택
        st.markdown("### 📘 단원 선택")
        selected_label = st.radio(
            "학습할 단원:",
            list(UNITS.values()),
            index=st.session_state.current_unit - 1,
            label_visibility="collapsed"
        )
        
        # 단원 변경 로직
        new_unit = [k for k, v in UNITS.items() if v == selected_label][0]
        if new_unit != st.session_state.current_unit:
            st.session_state.current_unit = new_unit
            st.session_state.step = 'intro'
            st.session_state.score = 0
            st.rerun()

        st.markdown("---")
        
        # 2. 오답 노트 (항상 표시, 없으면 비활성 메시지)
        st.markdown("### 📝 오답 노트")
        wrong_cnt = len(st.session_state.wrong_notes)
        
        if wrong_cnt > 0:
            st.warning(f"틀린 문제: {wrong_cnt}개")
            if st.button("오답 다시 풀기"):
                st.session_state.step = 'wrong_note_view'
                st.rerun()
        else:
            st.info("현재 오답이 없어요! 👍")
            # 버튼은 보여주되 비활성화 느낌을 주거나, 그냥 텍스트만 유지

        st.markdown("---")
        if st.button("🏠 홈으로 가기"):
            st.session_state.step = 'intro'
            st.rerun()

    # ================= 메인 화면 =================
    u_name = UNITS[st.session_state.current_unit]

    # [1] 개념 설명 화면
    if st.session_state.step == 'intro':
        st.markdown(f"<h1>오늘의 학습: {u_name.split('. ')[1]}</h1>", unsafe_allow_html=True)
        
        # 개념 카드 출력
        st.markdown(CONCEPTS[st.session_state.current_unit], unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 개념 이해 완료! 문제 풀기", use_container_width=True):
                st.session_state.step = 'quiz'
                st.session_state.q_idx = 0
                st.session_state.score = 0
                st.session_state.current_prob = None
                st.session_state.solved = False
                st.rerun()

    # [2] 퀴즈 화면
    elif st.session_state.step == 'quiz':
        total_q = 5
        st.markdown(f"<h3>✏️ {u_name} 실력 확인</h3>", unsafe_allow_html=True)
        st.progress((st.session_state.q_idx) / total_q, text=f"문제 {st.session_state.q_idx + 1} / {total_q}")

        if st.session_state.current_prob is None:
            st.session_state.current_prob = generate_problem(st.session_state.current_unit, '중')
            st.session_state.solved = False
        
        prob = st.session_state.current_prob
        
        # 문제 카드
        st.markdown(f"""
        <div class="card quiz-card">
            <h4 style="color:#666;">Q{st.session_state.q_idx + 1}.</h4>
            <h3 style="margin-top:0;">{prob['q']}</h3>
        </div>
        """, unsafe_allow_html=True)

        with st.form(key=f"q_{st.session_state.q_idx}"):
            if prob['type'] == 'obj':
                user_val = st.radio("정답 선택:", prob['options'], index=None, disabled=st.session_state.solved)
            else:
                user_val = st.text_input("정답 입력:", disabled=st.session_state.solved)
            
            btn_txt = "다음 문제 ➡️" if st.session_state.solved else "채점하기 ✨"
            submit = st.form_submit_button(btn_txt, use_container_width=True)

        if submit:
            if not st.session_state.solved:
                if not user_val:
                    st.warning("정답을 입력해주세요!")
                else:
                    if check_answer(user_val, prob['a']):
                        st.balloons()
                        st.success("정답입니다! 참 잘했어요! 🎉")
                        st.session_state.score += 1
                    else:
                        st.error("틀렸습니다. 😢")
                        st.markdown(f"""
                        <div class="card" style="background:#FFF5F5; border-color:#FFAAAA;">
                            <b>정답:</b> {prob['a']}<br>
                            <b>해설:</b> {prob['exp']}
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # 오답노트 추가
                        if prob not in st.session_state.wrong_notes:
                            prob['user_wrong'] = user_val
                            st.session_state.wrong_notes.append(prob)
                    
                    st.session_state.solved = True
                    st.rerun()
            else:
                # 다음 문제로
                st.session_state.q_idx += 1
                st.session_state.current_prob = None
                st.session_state.solved = False
                if st.session_state.q_idx >= total_q:
                    st.session_state.step = 'result'
                st.rerun()

    # [3] 결과 화면
    elif st.session_state.step == 'result':
        final_score = st.session_state.score * 20
        st.markdown("<h1>🏆 학습 완료!</h1>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <h2 style="font-size:3rem; color:#6C5CE7; margin-bottom:10px;">{final_score}점</h2>
            <p style="font-size:1.2rem;">{'완벽해요! 천재인가봐요! 🎓' if final_score==100 else '수고했어요! 오답 노트로 복습해볼까요? 💪'}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        if col1.button("다시 풀기 🔄", use_container_width=True):
            st.session_state.step = 'intro'
            st.rerun()
        if len(st.session_state.wrong_notes) > 0:
            if col2.button("오답 노트 보러가기 📝", use_container_width=True):
                st.session_state.step = 'wrong_note_view'
                st.rerun()

    # [4] 오답 노트 화면
    elif st.session_state.step == 'wrong_note_view':
        st.markdown("<h1>📝 내 오답 노트</h1>", unsafe_allow_html=True)
        
        if not st.session_state.wrong_notes:
            st.info("오답 노트가 비어있어요. 모두 맞혔나봐요! 👏")
        
        for i, note in enumerate(st.session_state.wrong_notes):
            with st.expander(f"🔍 {i+1}번 문제 다시보기 (클릭)"):
                st.markdown(f"""
                <div class="card" style="padding:15px; border-left: 5px solid #FF7675;">
                    <p><b>문제:</b> {note['q']}</p>
                    <p style="color:#D63031;"><b>내가 쓴 답:</b> {note.get('user_wrong','?')}</p>
                    <p style="color:#0984E3;"><b>정답: {note['a']}</b></p>
                    <p style="background:#F0F2F5; padding:10px; border-radius:5px;"><b>💡 해설:</b> {note['exp']}</p>
                </div>
                """, unsafe_allow_html=True)
                
        if st.button("🔙 돌아가기", use_container_width=True):
            st.session_state.step = 'intro'
            st.rerun()

if __name__ == "__main__":
    main()
