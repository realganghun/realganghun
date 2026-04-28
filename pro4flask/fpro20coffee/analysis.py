from pathlib import Path
import pandas as pd
import scipy.stats as stats
import matplotlib
matplotlib.use('Agg') #Anti Grain Geometry : matplotlib의 렌더링 엔진 中 하나, 이미지 저장 시 오류 방지 - 차트 출력 없이 저장할 때 사용
import matplotlib.pyplot as plt
import koreanize_matplotlib

BRAND_ORDER = ['스타벅스', '이디야', '탐앤탐스', '폴바셋']

def analysis_func(rdata:list[dict]):
    df = pd.DataFrame(rdata)

    if df.empty:
        return pd.DataFrame(), "데이터가 없습니다.", pd.DataFrame() # 빈 데이터프레임 반환
    
    df = df.dropna(subset=['gender', 'co_survey']) # co_survey 열에서 결측값 제거

    # 성별 브랜드별 선호 빈도수
    crossTable = pd.crosstab(index=df['gender'], columns=df['co_survey'])

    if crossTable.size == 0 or crossTable.shape[0] < 2 or crossTable.shape[1] < 2:
        return crossTable, "충분한 데이터가 없습니다.", pd.DataFrame() # 카이제곱 검정 불가 메시지 반환
    
    # 유의수준 : 0.05
    alpha = 0.05
    chi2, p, dof, expected = stats.chi2_contingency(crossTable)

    min_expected = expected.min()
    note = ""
    if min_expected < 5:
        note = f"<br><small>기대 빈도수가 5 미만인 셀이 있습니다 -> {min_expected:.2f}</small>"
    
    if p < alpha:
        result = f"귀무가설 기각({p:.5f} < {alpha}): 성별과 브랜드 선호도는 관련성이 있습니다.(대립가설)"
    else:
        result = f"귀무가설 채택({p:.5f} >= {alpha}): 성별과 브랜드 선호도는 관련성이 없습니다.(귀무가설)"

    return crossTable, result, df

def save_barchart_func(df:pd.DataFrame, out_path:Path) -> bool:
    if df is None or df.empty or 'co_survey' not in df.columns:
        return False
    
    counts = df['co_survey'].value_counts().reindex(BRAND_ORDER, fill_value=0)
    out_path.parent.mkdir(parents=True, exist_ok=True) # 디렉토리 생성
    fig = plt.figure()
    ax = counts.plot(kind='bar', width=0.6, edgecolor='black')
    ax.set_xlabel('커피 브랜드')
    ax.set_ylabel('선호도 수')
    ax.set_title('커피 브랜드별 선호도')
    ax.set_xticklabels(BRAND_ORDER, rotation=0)
    fig.tight_layout()
    fig.savefig(str(out_path), dpi=130, bbox_inches='tight')
    plt.close(fig)
    return True