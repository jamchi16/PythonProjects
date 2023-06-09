from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

@app.route('/')
def home():
    posts = []
    for file in os.listdir('posts'):
        if file.endswith('.md'):
            title = file[:-3]
            posts.append(title)
    return render_template('index.html', posts=posts)

@app.route('/posts/<path:path>')
def post(path):
    with open(f'posts/{path}.md', 'r') as file:
        content = file.read()
        html = markdown.markdown(content)
        return render_template('post.html', content=html)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)