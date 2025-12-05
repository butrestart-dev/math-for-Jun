import streamlit as st
import random

# --- 🎨 디자인 & CSS (가독성 최적화 테마) ---
def apply_custom_style():
    st.markdown("""
    <style>
    /* 따뜻한 크림색 배경 */
    .stApp { background-color: #FFF9C4; }
    
    /* 가독성 좋은 진한 글씨 (다크모드 강제 해제 효과) */
    h1, h2, h3, h4, p, div, span, label, li {
        color: #3E2723 !important;
        font-family: 'Jua', 'Nanum Gothic', sans-serif;
        line-height: 1.6;
    }
    
    /* 강조 박스 스타일 */
    .concept-box {
        background-color: #FFFFFF;
        border: 2px solid #FF9800;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    
    /* 버튼 스타일 */
    .stButton>button {
        background-color: #FF9800;
        color: white !important;
        border-radius: 15px;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); background-color: #F57C00; }
    
    /* 라디오 버튼 폰트 키우기 */
    .stRadio label { font-size: 18px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 📚 데이터: 단원 목록 ---
UNITS = {
    1: "1. 분수의 나눗셈",
    2: "2. 각기둥과 각뿔",
    3: "3. 소수의 나눗셈",
    4: "4. 비와 비율"
}

# --- 📖 데이터: 단원별 상세 개념 설명 (대폭 보강) ---
CONCEPTS = {
    1: """
    <div class='concept-box'>
        <h3>🍰 1. 분수의 나눗셈, 완벽 정복!</h3>
        <p><b>핵심 1: (자연수) ÷ (자연수)</b></p>
        <ul>
            <li>나눗셈의 몫을 분수로 나타낼 수 있어요.</li>
            <li>$$ 1 \\div 3 = \\frac{1}{3} $$ (뒤에 있는 수가 분모로 가요!)</li>
            <li>$$ 5 \\div 4 = \\frac{5}{4} = 1\\frac{1}{4} $$ (가분수는 대분수로!)</li>
        </ul>
        <br>
        <p><b>핵심 2: (분수) ÷ (자연수)</b></p>
        <ul>
            <li>나누기를 <b>곱하기</b>로 바꾸면 쉬워요.</li>
            <li>$$ \\div \\text{네모} $$ 는 $$ \\times \\frac{1}{\\text{네모}} $$ 로 변신!</li>
            <li>예시: $$ \\frac{4}{5} \\div 2 = \\frac{4}{5} \\times \\frac{1}{2} = \\frac{4}{10} = \\frac{2}{5} $$</li>
        </ul>
    </div>
    """,
    
    2: """
    <div class='concept-box'>
        <h3>📦 2. 각기둥과 각뿔의 세계</h3>
        <p><b>[각기둥] 위아래가 똑같은 기둥 모양</b></p>
        <ul>
            <li><b>밑면</b>: 서로 평행하고 합동인 두 면 (모양의 이름이 돼요)</li>
            <li><b>옆면</b>: 두 밑면을 연결하는 면 (모두 <b>직사각형</b> 모양!)</li>
        </ul>
        <p><b>[각뿔] 위가 뾰족한 뿔 모양</b></p>
        <ul>
            <li><b>밑면</b>: 바닥에 있는 면</li>
            <li><b>옆면</b>: 뿔의 꼭짓점으로 모이는 면 (모두 <b>삼각형</b> 모양!)</li>
        </ul>
        <hr>
        <p><b>💡 도형의 구성 요소 공식 (밑면의 변의 수 = N)</b></p>
        <table style="width:100%; text-align:center; color:#3E2723;">
            <tr><td>구분</td><td>모서리</td><td>꼭짓점</td><td>면</td></tr>
            <tr><td><b>각기둥</b></td><td>$$ N \\times 3 $$</td><td>$$ N \\times 2 $$</td><td>$$ N + 2 $$</td></tr>
            <tr><td><b>각뿔</b></td><td>$$ N \\times 2 $$</td><td>$$ N + 1 $$</td><td>$$ N + 1 $$</td></tr>
        </table>
    </div>
    """,
    
    3: """
    <div class='concept-box'>
        <h3>💧 3. 소수의 나눗셈</h3>
        <p><b>방법 1: 자연수처럼 계산하기</b></p>
        <ul>
            <li>$$ 36.6 \\div 3 $$ 을 계산할 때,</li>
            <li>먼저 점이 없다고 생각하고 $$ 366 \\div 3 = 122 $$ 를 계산해요.</li>
            <li>그 다음, 원래 소수점 위치에 맞춰 점을 콕! 찍으면 $$ 12.2 $$ 가 됩니다.</li>
        </ul>
        <br>
        <p><b>방법 2: 분수로 고쳐서 계산하기</b></p>
        <ul>
            <li>$$ 1.2 \\div 2 = \\frac{12}{10} \\div 2 = \\frac{12}{10} \\times \\frac{1}{2} = \\frac{6}{10} = 0.6 $$</li>
        </ul>
        <p>⚠️ <b>주의할 점:</b> 몫의 소수점은 나뉠 수의 소수점 자리에 맞춰서 찍어야 해요!</p>
    </div>
    """,
    
    4: """
    <div class='concept-box'>
        <h3>🍎 4. 비와 비율</h3>
        <p><b>1. 비 (Ratio)</b></p>
        <ul>
            <li>두 수를 나눗셈으로 비교할 때 <b>:</b> 기호를 사용해요.</li>
            <li><b>3 : 2</b> $\\rightarrow$ 3 대 2</li>
            <li>왼쪽(3)이 <b>전항</b>(비교하는 양), 오른쪽(2)이 <b>후항</b>(기준량)입니다.</li>
        </ul>
        <br>
        <p><b>2. 비율 (Rate)</b></p>
        <ul>
            <li>비의 값을 분수나 소수로 나타낸 것입니다.</li>
            <li>$$ \\text{비율} = \\frac{\\text{비교하는 양}}{\\text{기준량}} $$</li>
            <li>예: 3 : 2 의 비율은 $$ \\frac{3}{2} $$ 또는 1.5</li>
        </ul>
        <br>
        <p><b>3. 백분율 (%)</b></p>
        <ul>
            <li>비율에 100을 곱한 값입니다.</li>
            <li>$$ \\frac{1}{2} \\times 100 = 50\\% $$</li>
        </ul>
    </div>
    """
}

# --- ⚙️ 기능 함수: 채점 및 문제 생성 ---

def check_answer(user_input, correct_val):
    """정답 확인 로직 (유연한 비교)"""
    try:
        user_str = str(user_input).replace(" ", "") # 공백 제거
        correct_str = str(correct_val).replace(" ", "")
        
        # 1. 텍스트 완전 일치 확인
        if user_str == correct_str: return True
        
        # 2. 수치 비교 (소수/분수)
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
    """
    단원별 문제 출제 로직
    - 상/중/하 난이도 반영
    - 객관식(obj)/주관식(subj) 랜덤 배정
    """
    problem = {}
    problem['unit'] = unit_num
    
    # 문제 유형 랜덤 결정 (객관식 50%, 주관식 50%)
    q_type = random.choice(['obj', 'subj'])
    # 2단원은 객관식이 더 적합하므로 확률 높임
    if unit_num == 2: q_type = 'obj'
    
    problem['type'] = q_type
    
    # ---------------- [1단원: 분수의 나눗셈] ----------------
    if unit_num == 1:
        if difficulty == '하': # (자연수)÷(자연수)
            a, b = random.randint(1, 9), random.randint(2, 9)
            if a == b: b += 1
            problem['q'] = f"나눗셈의 몫을 분수로 나타내면? $${a} \\div {b}$$"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = f"뒤에 있는 수({b})가 분모가 됩니다."
            
        elif difficulty == '중': # (분수)÷(자연수)
            ja, mo = random.randint(1, 9), random.randint(2, 9)
            nat = random.randint(2, 5)
            problem['q'] = f"계산하시오: $$\\frac{{{ja}}}{{{mo}}} \\div {nat}$$"
            problem['a'] = f"{ja}/{mo*nat}"
            problem['exp'] = f"곱하기로 바꾸면: {ja}/{mo} × 1/{nat} = {ja}/{mo*nat}"
            
        else: # (대분수 포함 or 약분 필요)
            a = random.randint(10, 20)
            b = random.randint(2, 5)
            problem['q'] = f"계산하시오 (가분수 가능): $$\\frac{{{a}}}{{{b}}} \\div 2$$"
            problem['a'] = f"{a}/{b*2}"
            problem['exp'] = f"분모에 2를 곱해줍니다. {a}/{b*2}"

        # 객관식 보기 생성
        if q_type == 'obj':
            opts = [problem['a']]
            while len(opts) < 4:
                # 임의의 오답 생성
                fake = f"{random.randint(1,20)}/{random.randint(2,20)}"
                if fake not in opts: opts.append(fake)
            random.shuffle(opts)
            problem['options'] = opts

    # ---------------- [2단원: 각기둥과 각뿔] ----------------
    elif unit_num == 2:
        shapes = [
            ('삼각기둥', 3, '기둥'), ('사각기둥', 4, '기둥'), ('오각기둥', 5, '기둥'),
            ('삼각뿔', 3, '뿔'), ('사각뿔', 4, '뿔'), ('오각뿔', 5, '뿔')
        ]
        s_name, n, s_class = random.choice(shapes)
        target = random.choice(['모서리', '꼭짓점', '면'])
        
        problem['q'] = f"**{s_name}**의 **{target}**의 수는 몇 개일까요?"
        
        if s_class == '기둥':
            if target == '모서리': ans = n * 3
            elif target == '꼭짓점': ans = n * 2
            else: ans = n + 2
        else: # 뿔
            if target == '모서리': ans = n * 2
            elif target == '꼭짓점': ans = n + 1
            else: ans = n + 1
            
        problem['a'] = str(ans)
        problem['exp'] = f"{s_name}의 밑면 변의 수는 {n}개입니다. 공식을 떠올려보세요!"
        
        if q_type == 'obj':
            # 정답 주변의 숫자로 오답 생성
            opts = set([str(ans)])
            while len(opts) < 4:
                opts.add(str(int(ans) + random.randint(-3, 3)))
            problem['options'] = list(opts)
            random.shuffle(problem['options'])

    # ---------------- [3단원: 소수의 나눗셈] ----------------
    elif unit_num == 3:
        # 나누어 떨어지는 수 생성 로직
        divisor = random.randint(2, 9) # 나누는 수
        quotient = random.randint(11, 99) # 몫 (자연수 부분)
        dividend = quotient * divisor
        
        # 소수점 만들기 (예: 366 -> 36.6)
        dividend_f = dividend / 10
        quotient_f = quotient / 10
        
        problem['q'] = f"다음 나눗셈을 계산하세요: $${dividend_f} \\div {divisor}$$"
        problem['a'] = str(quotient_f)
        problem['exp'] = f"자연수 {dividend} ÷ {divisor} = {quotient} 입니다. 소수점을 한 칸 앞으로 옮기세요."
        
        if q_type == 'obj':
            opts = [str(quotient_f), str(quotient_f*10), str(quotient_f/10), str(quotient_f + 1)]
            random.shuffle(opts)
            problem['options'] = opts

    # ---------------- [4단원: 비와 비율] ----------------
    elif unit_num == 4:
        sub_type = random.choice(['ratio', 'term', 'percent'])
        
        if sub_type == 'ratio':
            a, b = random.randint(1, 10), random.randint(1, 10)
            problem['q'] = f"사과 {a}개와 배 {b}개가 있습니다. 배에 대한 사과의 비는?"
            problem['a'] = f"{a}:{b}"
            problem['exp'] = f"'~에 대한'이 붙은 {b}가 기준(뒤)이 됩니다. 답은 {a}:{b}"
            if q_type == 'obj':
                problem['options'] = [f"{a}:{b}", f"{b}:{a}", f"{a}/{b}", f"{a+b}"]
                random.shuffle(problem['options'])
                
        elif sub_type == 'term':
            a, b = random.randint(2, 9), random.randint(2, 9)
            problem['q'] = f"비 {a}:{b} 에서 **후항**(기준량)은 무엇입니까?"
            problem['a'] = str(b)
            problem['exp'] = f"기호 : 의 오른쪽에 있는 수가 후항입니다."
            if q_type == 'obj':
                problem['options'] = [str(a), str(b), str(a+b), "없음"]
                random.shuffle(problem['options'])
                
        else: # percent
            num = random.choice([1, 2, 3, 4])
            problem['q'] = f"비율 $$\\frac{{{num}}}{{5}}$$ 를 백분율(%)로 나타내면?"
            problem['a'] = str(num * 20)
            problem['exp'] = f"분모를 100으로 만들거나, 100을 곱해보세요. {num}/5 × 100 = {num*20}"
            if q_type == 'obj':
                ans = num*20
                problem['options'] = [f"{ans}%", f"{ans+10}%", f"{ans/2}%", f"{ans*2}%"]
                random.shuffle(problem['options'])

    return problem

# --- 🚀 메인 앱 실행 ---
def main():
    st.set_page_config(page_title="초등 수학 완전정복", page_icon="💯", layout="centered")
    apply_custom_style()

    # --- 세션 상태 관리 (새로고침 되어도 데이터 유지) ---
    if 'step' not in st.session_state: st.session_state.step = 'intro'
    if 'current_unit' not in st.session_state: st.session_state.current_unit = 1
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
    if 'current_prob' not in st.session_state: st.session_state.current_prob = None
    if 'solved' not in st.session_state: st.session_state.solved = False
    if 'wrong_notes' not in st.session_state: st.session_state.wrong_notes = [] 

    # --- 사이드바 메뉴 ---
    st.sidebar.markdown("## 🚩 메뉴")
    
    # 1. 처음으로 버튼
    if st.sidebar.button("🏠 홈으로 이동"):
        st.session_state.step = 'intro'
        st.session_state.score = 0
        st.session_state.q_idx = 0
        st.session_state.current_prob = None
        st.rerun()

    # 2. 오답 노트 버튼
    if len(st.session_state.wrong_notes) > 0:
        st.sidebar.markdown("---")
        st.sidebar.warning(f"오답 노트에 **{len(st.session_state.wrong_notes)}문제**가 있어요!")
        if st.sidebar.button("📝 오답 노트 복습하기"):
            st.session_state.step = 'wrong_note_view'
            st.rerun()

    # --- [STEP 1] 개념 학습 화면 ---
    if st.session_state.step == 'intro' or st.session_state.step == 'study':
        st.title("초등 수학 6-1 🏫")
        st.markdown("공부할 단원을 선택해주세요.")
        
        # 단원 선택 UI
        unit_options = list(UNITS.values())
        selected_name = st.selectbox("단원 목록", unit_options, index=st.session_state.current_unit-1)
        
        # 선택된 단원 ID 찾기
        for k, v in UNITS.items():
            if v == selected_name:
                st.session_state.current_unit = k
                break
        
        # 상세 개념 설명 출력 (HTML Box 활용)
        st.markdown(CONCEPTS[st.session_state.current_unit], unsafe_allow_html=True)
        
        # 학습 시작 버튼
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 학습 내용을 이해했어요! 문제 풀기", use_container_width=True):
            st.session_state.step = 'quiz'
            st.session_state.score = 0
            st.session_state.q_idx = 0
            st.session_state.current_prob = None
            st.session_state.solved = False
            # 오답노트는 누적하거나, 여기서 초기화할 수 있음 (현재는 누적)
            st.rerun()

    # --- [STEP 2] 퀴즈 화면 ---
    elif st.session_state.step == 'quiz':
        total_q = 5
        
        # 상단 정보
        st.markdown(f"**{UNITS[st.session_state.current_unit]}** 푸는 중...")
        st.progress(st.session_state.q_idx / total_q, text=f"문제 {st.session_state.q_idx + 1} / {total_q}")

        # 문제 생성 (없으면 생성)
        if st.session_state.current_prob is None:
            # 난이도 랜덤 섞기
            diff = random.choice(['하', '중', '중', '상'])
            st.session_state.current_prob = generate_problem(st.session_state.current_unit, diff)
            st.session_state.solved = False
        
        prob = st.session_state.current_prob
        
        # 문제 출력
        st.markdown(f"### Q{st.session_state.q_idx + 1}.")
        st.markdown(f"<h5>{prob['q']}</h5>", unsafe_allow_html=True)
        
        # 정답 입력 폼
        with st.form(key='quiz_form'):
            user_val = ""
            
            # 객관식/주관식 분기
            if prob['type'] == 'obj':
                # key에 idx를 넣어 문제 바뀔 때마다 초기화
                user_val = st.radio(
                    "정답을 선택하세요:", 
                    prob['options'], 
                    key=f"radio_{st.session_state.q_idx}",
                    index=None,
                    disabled=st.session_state.solved
                )
            else:
                # key에 idx를 넣어 문제 바뀔 때마다 비움
                user_val = st.text_input(
                    "정답을 입력하세요:", 
                    key=f"text_{st.session_state.q_idx}",
                    disabled=st.session_state.solved
                )
            
            # 버튼 텍스트 변경
            btn_text = "다음 문제 ➡️" if st.session_state.solved else "채점하기 ✨"
            submit_btn = st.form_submit_button(btn_text)
        
        # 제출 처리
        if submit_btn:
            if not st.session_state.solved:
                # [채점 하기]
                if not user_val:
                    st.warning("답을 입력해주세요!")
                else:
                    is_correct = check_answer(user_val, prob['a'])
                    if is_correct:
                        st.success("정답입니다! 🎉")
                        st.session_state.score += 1
                        st.balloons()
                    else:
                        st.error("틀렸습니다. 😢")
                        st.markdown(f"**정답: {prob['a']}**")
                        st.info(f"💡 해설: {prob['exp']}")
                        # 오답노트 저장 (이미 있는지 확인 후)
                        if prob not in st.session_state.wrong_notes:
                            prob['user_wrong_answer'] = user_val # 내가 쓴 오답도 기록
                            st.session_state.wrong_notes.append(prob)
                    
                    st.session_state.solved = True
                    st.rerun()
            else:
                # [다음 문제로]
                st.session_state.q_idx += 1
                st.session_state.current_prob = None
                st.session_state.solved = False
                
                # 끝났으면 결과 화면으로
                if st.session_state.q_idx >= total_q:
                    st.session_state.step = 'result'
                st.rerun()

    # --- [STEP 3] 결과 화면 ---
    elif st.session_state.step == 'result':
        total_q = 5
        final_score = st.session_state.score * (100 // total_q)
        
        st.title("수고했어요! 👏")
        st.metric("최종 점수", f"{final_score}점")
        
        if final_score >= 80:
            st.success("와우! 실력이 대단해요! 🏆")
        elif final_score >= 60:
            st.info("참 잘했어요! 조금만 더 하면 백점! 💪")
        else:
            st.warning("아쉬워요. 개념을 다시 읽어볼까요? 🌱")

        col1, col2 = st.columns(2)
        if col1.button("다시 풀기 🔄"):
            st.session_state.step = 'study' # 개념부터 다시
            st.rerun()
        if len(st.session_state.wrong_notes) > 0:
            if col2.button("오답 노트 확인 📝"):
                st.session_state.step = 'wrong_note_view'
                st.rerun()

    # --- [STEP 4] 오답 노트 모아보기 ---
    elif st.session_state.step == 'wrong_note_view':
        st.title("📝 내 오답 노트")
        st.markdown("틀린 문제를 다시 한번 읽어보세요.")
        
        if not st.session_state.wrong_notes:
            st.success("오답 노트가 비어있어요! 완벽합니다.")
        
        for i, note in enumerate(st.session_state.wrong_notes):
            with st.expander(f"{i+1}번 문제 (클릭해서 보기)"):
                st.markdown(f"**문제:** {note['q']}")
                st.markdown(f"**내가 쓴 답:** {note.get('user_wrong_answer', '없음')}")
                st.markdown(f"**정답:** {note['a']}")
                st.info(f"**해설:** {note['exp']}")
        
        if st.button("🏠 메인으로 돌아가기"):
            st.session_state.step = 'intro'
            st.rerun()

if __name__ == "__main__":
    main()
