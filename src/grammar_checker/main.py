from flask import Flask, render_template, request
from app.rules import check_subject_verb_agreement
from app.nlp_model import check_grammar_with_transformer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_grammar():
    text = request.form["text"]
    rule_based_result = check_subject_verb_agreement(text)
    transformer_result = check_grammar_with_transformer(text)
    return {
        "rule_based": rule_based_result,
        "transformer_based": transformer_result,
    }

if __name__ == "__main__":
    app.run(debug=True)
