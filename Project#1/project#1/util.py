from pathlib import Path
import os
import pandas as pd
import numpy as np


class Util:
    """
    ! "city" or "cities" 데이터는 예를 들어 "TSP.csv"를 의미함
    ! "solution" 데이터는 예를 들어 "example_solution.csv"를 의미함

    * CSV 데이터 R/W 관련 Method
        * checkPath(path: Path) -> None
            * path 경로가 있는지 확인 후, 없는 경우 디렉토리 생성

        * getData(path: Path, name: str) -> DataFrame
            * path 경로에 있는 'name' 도시 데이터 파일을 읽어서 pandas DataFrame 타입으로 반환 (COL - x, y)

        * getSolution(path: Path, name: str) -> DataFrame
            * path 경로에 있는 'name' 솔루션 파일을 읽어서 pandas DataFrame 타입으로 변환 (COL - city)

        * saveData(data: DataFrame, path: Path, name: str) -> None
            * path 경로에 'name' 파일 이름으로 data 파일 csv 형식으로 저장

    ========================================================================

    * 데이터 처리 관련 Method
        * distance(x: list[float, float], y: list[float, float]) -> float
            * x와 y 좌표 사이의 유클리드 거리 값 반환

        * cost(sol_with_loc: DataFrame) -> float
            * city 데이터와 solution 데이터가 병합된 sol_with_loc DataFrame 인자로 받아 전체 경로 계산하여 반환
            * city 데이터와 solution 데이터 병합은 mergeData(cities, solution) 이용

        * mergeData(cities: DataFrame, solution: DataFrame) -> DataFrame
            * 도시 좌표 정보를 가진 cities 데이터와 경로를 가지고 있는 solution 데이터를 병합하여 반환
            * 반환된 데이터는 cost(sol_with_loc)을 통해서 총 경로 비용 계산 가능

        * randomize(data: DataFrame) -> DataFrame
            * 입력된 데이터 랜덤하게 셔플한 후 반환

        * concatStartLoc(body: DataFrame, item: DataFrame) -> DataFrame
            * body 앞 부분에 item 추가하여 DataFrame 형태로 반환
            * 시작점을 제외하고 가공한 데이터에 시작점을 붙이고 싶을 때 이용
    """

    @staticmethod
    def checkPath(path: Path) -> None:
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def getData(path: Path, name: str) -> pd.DataFrame:
        data = pd.read_csv(path / name, header=None, names=["x", "y"])

        return data

    @staticmethod
    def getSolution(path: Path, name: str) -> pd.DataFrame:
        data = pd.read_csv(path / name, header=None, names=["city"])

        return data

    @staticmethod
    def saveData(data: pd.DataFrame, path: Path, name: str) -> None:
        Util.checkPath(path)
        data.to_csv(path / name, sep=",", header=False, index=False, encoding="UTF-8", line_terminator="\n")

    @staticmethod
    def distance(x, y) -> float:
        return np.linalg.norm(np.array(x)-np.array(y))

    @staticmethod
    def cost(sol_with_loc: pd.DataFrame) -> float:
        total_cost = 0.0
        sol_ = sol_with_loc.values.tolist()

        for idx in range(len(sol_)-1):
            total_cost += Util.distance(sol_[idx], sol_[idx+1])

        return total_cost

    @staticmethod
    def mergeData(cities: pd.DataFrame, solution: pd.DataFrame) -> pd.DataFrame:
        data = pd.concat([solution, cities], axis=1)

        return data.drop(data.columns[[0]], axis=1)

    @staticmethod
    def randomize(data: pd.DataFrame) -> pd.DataFrame:
        return data.sample(frac=1)

    @staticmethod
    def concatStartLoc(body: pd.DataFrame, item: pd.DataFrame) -> pd.DataFrame:
        temp_ = pd.concat([item, body])
        return pd.concat([temp_, item])
