import os
import pickle

filename = 'score.bin'

def save_scores(scores):
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

def load_scores():
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return None

def print_scores(scores):
    print("\n[점수 출력]")
    print("개인점수:", *scores)
    avg = sum(scores) / len(scores)
    print("평균:", avg)

def main():
    scores = load_scores()
    
    if scores is not None:
        print("[파일 읽기]")
        print_scores(scores)
    else:
        scores = []
        print("[점수 입력]")
        i = 1
        while True:
            try:
                score = int(input(f"#{i}? "))
                if score < 0:
                    break
                scores.append(score)
                i += 1
            except ValueError:
                print("숫자를 입력해주세요.")
        print_scores(scores)
        save_scores(scores)

if __name__ == '__main__':
    main()
