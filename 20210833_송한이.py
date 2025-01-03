import random
import string

class StudentManager:
    def __init__(self):
        self.students = []

    # 학생 정보 무작위 생성
    def generate_random_students(self, count=5):
        students = []
        for _ in range(count):
            name = ''.join(random.choices(string.ascii_uppercase, k=2))  # 이름: 알파벳 대문자 두 글자
            age = random.randint(18, 22)  # 나이: 18 ~ 22 사이의 정수
            score = random.randint(0, 100)  # 성적: 0 ~ 100 사이의 정수
            students.append({"name": name, "age": age, "score": score})
        self.students = students

    # 파일에 학생 정보 저장
    def write_students_to_file(self, filename):
        with open(filename, 'w') as file:
            for student in self.students:
                file.write(f"{student['name']} {student['age']} {student['score']}\n")

    # 파일에서 학생 정보 읽기
    def read_students_from_file(self, filename):
        students = []
        with open(filename, 'r') as file:
            for line in file:
                name, age, score = line.strip().split()
                students.append({"name": name, "age": int(age), "score": int(score)})
        self.students = students

    # 정렬 알고리즘 구현
    def selection_sort(self, field, reverse=False):
        """선택 정렬"""
        students = self.students
        n = len(students)
        for i in range(n - 1):
            selected = i
            for j in range(i + 1, n):
                if (students[j][field] < students[selected][field]) != reverse:
                    selected = j
            students[i], students[selected] = students[selected], students[i]
        return students

    def insertion_sort(self, field, reverse=False):
        """삽입 정렬"""
        students = self.students
        for i in range(1, len(students)):
            key = students[i]
            j = i - 1
            while j >= 0 and (students[j][field] > key[field]) != reverse:
                students[j + 1] = students[j]
                j -= 1
            students[j + 1] = key
        return students

    def quick_sort(self, field, left, right, reverse=False):
        """퀵 정렬"""
        if left < right:
            q = self.partition(field, left, right, reverse)  # 분할
            self.quick_sort(field, left, q - 1, reverse)  # 왼쪽 부분리스트를 퀵 정렬
            self.quick_sort(field, q + 1, right, reverse)  # 오른쪽 부분리스트를 퀵 정렬

        return self.students
        
    def partition(self, field, left, right, reverse):
        """분할 알고리즘"""
        low = left + 1
        high = right
        pivot = self.students[left][field]  # pivot은 선택한 field에 해당하는 값으로 설정
        
        while low <= high:
            # 피벗보다 큰 요소를 찾음 (reverse에 따라 조건 변경)
            while low <= right and ((self.students[low][field] <= pivot) if not reverse else (self.students[low][field] >= pivot)):
                low += 1
            # 피벗보다 작은 요소를 찾음 (reverse에 따라 조건 변경)
            while high >= left and ((self.students[high][field] > pivot) if not reverse else (self.students[high][field] < pivot)):
                high -= 1

            # 요소를 교환
            if low < high:
                self.students[low], self.students[high] = self.students[high], self.students[low]

        # 피벗 교환
        self.students[left], self.students[high] = self.students[high], self.students[left]
        return high


    def radix_sort(self, field, reverse=False):
        """기수 정렬"""
        max_num = max(x[field] for x in self.students)
        exp = 1
        while max_num // exp > 0:
            self.students = self.counting_sort(field, exp, reverse)
            exp *= 10
        return self.students

    def counting_sort(self, field, exp, reverse):
        """계수 정렬 알고리즘"""
        output = [None] * len(self.students)
        count = [0] * 30

        for student in self.students:
            index = (student[field] // exp) % 10
            count[index] += 1

        # 내림차순으로 처리
        if reverse:
            for i in range(28, -1, -1):
                count[i] += count[i + 1]
        else:
            for i in range(1, 30):
                count[i] += count[i - 1] 

        for student in reversed(self.students):
            index = (student[field] // exp) % 10
            output[count[index] - 1] = student
            count[index] -= 1

        return output


def main():
    manager = StudentManager()
    input_filename = 'C://Users//soldesk//Desktop//hani//students.txt'

    print('안녕하세요 20210833 송한이입니다')

    while True:
        print('''=== 성적 관리 프로그램 ===
메뉴:
1. 이름을 기준으로 정렬
2. 나이를 기준으로 정렬
3. 성적을 기준으로 정렬
4. 프로그램 종료
        ''')

        choice = input("정렬기준을 선택하세요. (1, 2, 3, 4): ")

        if choice == "1":
            field = "name"
            field_name = "이름"
        elif choice == "2":
            field = "age"
            field_name = "나이"
        elif choice == "3":
            field = "score"
            field_name = "성적"
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")
            continue

        # 정렬 순서 선택
        while True:
            order = input("정렬 순서를 선택하세요. (1: 오름차순, 2: 내림차순): ")
    
            if order == "1": # 오름차순
                reverse = False 
                break 
            elif order == "2": # 내림차순
                reverse = True
                break 
            else:
                print("잘못된 입력입니다. 다시 시도해주세요.") 

        # 학생 정보 저장 방식 선택
        while True:
            save = input("학생 정보를 파일로 저장하시겠습니까? (Y: 파일로 저장, N: 리스트로만 저장): ")
            if save == 'Y' or save =='y':
                manager.generate_random_students(30)
                manager.write_students_to_file(input_filename)
                print(f"학생 정보가 '{input_filename}' 에 저장되었습니다.")
                break
            elif save =='N' or save == 'n':
                manager.generate_random_students(30)
                print("학생 정보가 리스트로만 저장되었습니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 시도해주세요.") 
              
        # 파일에서 학생 정보 읽기
        manager.read_students_from_file(input_filename)
        print(f"-----------------------------------------\n* 정렬 기준: {field_name}, {'내림차순' if reverse else '오름차순'}")  
        
        # 생성된 학생 리스트 출력
        print("* 생성된 학생 정보:")
        for student in manager.students:
            print(f"이름: {student['name']}, 나이: {student['age']}, 성적: {student['score']}")
        print("-----------------------------------------")

        # 각 정렬 방식 출력
        print("\n정렬 결과 (선택 정렬):")
        selection_sorted = manager.selection_sort(field, reverse)
        for student in selection_sorted:
            print(f"이름: {student['name']}, 나이: {student['age']}, 성적: {student['score']}")

        print("\n정렬 결과 (삽입 정렬):")
        insertion_sorted = manager.insertion_sort(field, reverse)
        for student in insertion_sorted:
            print(f"이름: {student['name']}, 나이: {student['age']}, 성적: {student['score']}")

        print("\n정렬 결과 (퀵 정렬):")
        quick_sorted = manager.quick_sort(field, 0, len(manager.students) - 1, reverse)
        for student in quick_sorted:
            print(f"이름: {student['name']}, 나이: {student['age']}, 성적: {student['score']}")

        # 기수 정렬 - 성적 기준으로 정렬할 때만 사용 가능
        if field == "score":
            print("\n정렬 결과 (기수 정렬):")
            radix_sorted = manager.radix_sort(field, reverse)
            for student in radix_sorted:
                print(f"이름: {student['name']}, 나이: {student['age']}, 성적: {student['score']}")


        print("==========================================")

if __name__ == "__main__":
    main()
