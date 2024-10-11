from flask import Flask, render_template, jsonify

app = Flask(__name__)

def load_words_from_txt():
    words = []
    with open('formatted_words.txt', 'r', encoding='utf-8') as f:
        for line in f:
            word_data = line.strip().split(',')
            if len(word_data) == 4:
                examples = word_data[3].split('|')  # 예문을 |로 분리
                words.append({
                    "word": word_data[0],
                    "pronunciation": word_data[1],
                    "meaning": word_data[2],
                    "examples": examples
                })
    return words

@app.route('/')
def index():
    words = load_words_from_txt()  # 단어 데이터 로드
    return render_template('index.html', words=words)  # 단어 데이터를 템플릿에 전달

if __name__ == '__main__':
    app.run(debug=True)
