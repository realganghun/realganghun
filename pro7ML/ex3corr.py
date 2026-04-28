# 외국인(미국, 일본, 중국) 국내 관광지(5개) 방문 관련자료 사용
# 나라별 관광지 상관관계 확인하기

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 산점도 그리기
def setScatterGraph(tour_table, all_table, tourpoint):
    # 1. 해당 관광지의 데이터만 추출
    target_tour = tour_table[tour_table['resNm'] == tourpoint]
    
    # 2. 국가별 테이블(all_table)과 관광지 테이블 병합
    merged_table = pd.merge(target_tour, all_table, left_index=True, right_index=True)
    
    # 3. 상관계수 계산 (ForNum과 국가별 데이터 사이)
    # 필요한 컬럼만 추출해서 상관계수 행렬을 만듭니다.
    corr_matrix = merged_table[['ForNum', 'china', 'japan', 'usa']].corr()
    
    # 우리가 궁금한 건 '관광지 입장객(ForNum)'과 '국가별 방문객' 사이의 관계입니다.
    r_china = corr_matrix.loc['ForNum', 'china']
    r_japan = corr_matrix.loc['ForNum', 'japan']
    r_usa = corr_matrix.loc['ForNum', 'usa']
    
    print(f"\n[{tourpoint}] 상관계수")
    print(f"중국: {r_china:.3f}, 일본: {r_japan:.3f}, 미국: {r_usa:.3f}")

    # 4. 시각화 (산점도 그리기)
    plt.figure(figsize=(12, 4))
    
    countries = [('china', 'red'), ('japan', 'blue'), ('usa', 'green')]
    for i, (country, color) in enumerate(countries, 1):
        plt.subplot(1, 3, i)
        plt.scatter(merged_table[country], merged_table['ForNum'], alpha=0.5, c=color)
        plt.title(f"{country} (r={corr_matrix.loc['ForNum', country]:.2f})")
        plt.xlabel(f"{country} 전체 입국자")
        plt.ylabel("관광지 입장객 수")

    plt.suptitle(f"<{tourpoint}> 국가별 방문객 상관관계 분석")
    plt.tight_layout()
    plt.show()
    
    # 나중에 리스트로 관리하기 위해 결과 반환
    return {'tourpoint': tourpoint, 'china': r_china, 'japan': r_japan, 'usa': r_usa}

def processFunc():
    # 서울시 관광지 정보 파일
    fname = "서울특별시_관광지입장정보_2011_2016.json"
    jsonTP = json.loads(open(fname, 'r', encoding='utf-8').read())
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm', 'resNm', 'ForNum')) # 년월, 관광지명, 관광객수
    tour_table = tour_table.set_index('yyyymm')
    print(tour_table)
            #   resNm  ForNum
# yyyymm
# 201101        창덕궁   14137
# 201101        운현궁       0
# 201101        경복궁   40224
    resNm = tour_table.resNm.unique()
    # print('resNm : ', resNm[:5])

    # 중국인 관광지 정보 파일 DataFrame에 저장
    cdf = '중국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding='utf-8').read())
    china_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    print(china_table[:2])

    # 일본인 관광지 정보 파일 DataFrame에 저장
    jdf = '일본인방문객.json'
    jdata = json.loads(open(jdf, 'r', encoding='utf-8').read())
    japan_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns={'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    print(japan_table[:2])

    # 미국 관광지 정보 파일 DataFrame에 저장
    udf = '미국인방문객.json'
    jdata = json.loads(open(udf, 'r', encoding='utf-8').read())
    usa_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    print(usa_table[:2])

    all_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    all_table = pd.merge(all_table, usa_table, left_index=True, right_index=True)
    print(all_table)

    r_list = []
    for tourpoint in resNm[:5]:
        r_list.append(setScatterGraph(tour_table, all_table, tourpoint))

    # r_list를 데이터프레임으로 변환
    result_df = pd.DataFrame(r_list)
    result_df.set_index('tourpoint', inplace=True)
    
    print("\n--- 전체 관광지별 상관계수 결과 ---")
    print(result_df)

    # Heatmap 시각화
    import seaborn as sns
    plt.figure(figsize=(8, 6))
    sns.heatmap(result_df, annot=True, cmap='RdYlBu_r', center=0)
    plt.title("관광지별 국가 관광객 상관계수 히트맵")
    plt.show()

if __name__ == "__main__":
    processFunc()