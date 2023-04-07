from util import Util
import paths


class RandomSearch:
    """
    ! RandomSearch 초기 인자로 csv 파일 경로와 csv 파일 명을 필요 (default)
    ! cities -> "cities" 데이터 - 예를 들어 "TSP.csv"를 의미함
    ! solution -> "solution" 데이터 - 예를 들어 "example_solution.csv"를 의미함
    ! sol_with_loc -> "cities"와 "solution"이 병합된 데이터
    ! cost -> 총 경로 비용(거리)

    * randomize()
        "cities" 데이터의 시작점을 제외한 나머지를 random 하게 재배열 한 후, 시작점을 맨 앞에 추가하여 반환

    * run()
        초기 load 된 "cities" 데이터를 가지고 랜덤화 및 총 비용 계산하여 csv 파일로 저장하는 모든 과정 수행
    """
    def __init__(self, path=paths.CSV, csv="TSP.csv"):
        self.cities = Util.getData(path, csv)
        self.solution = None
        self.sol_list = []
        self.sol_with_loc = None
        self.startLoc = self.cities.head(1)
        self.cost = 0.0

    def randomize(self):
        random_ = Util.randomize(self.cities.loc[1:])                   # 시작점을 제외한 나머지 randomize 진행
        return Util.concatStartLoc(body=random_, item=self.startLoc)    # 앞 뒤로 시작점 추가

    def save(self):
        Util.saveData(data=self.solution.head(self.solution.shape[0]-1), path=paths.RESULT,
                      name="result_{cost}_.csv".format(cost=self.cost))

    def run(self):
        self.sol_list = []
        self.sol_with_loc = self.randomize()
        self.solution = self.sol_with_loc.index.to_frame()

        for item in self.solution.to_numpy():
            self.sol_list.append(item[0])

        self.sol_list = self.sol_list[:len(self.sol_list)-1]

        self.cost = Util.cost(self.sol_with_loc)


"""
[USAGE EXAMPLE]

randomSearch = RandomSearch()

for i in range(10):
    randomSearch.run()
    # Also, If you want use solution as "list type", using 'randomSearch.sol_list'
    print(randomSearch.sol_list)
    print("COST - ", randomSearch.cost)
    
"""