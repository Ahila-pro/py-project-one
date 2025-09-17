from flask import Flask, request, jsonify

app = Flask(__name__)

def number_to_words(num):
    units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five',
             'Six', 'Seven', 'Eight', 'Nine']
    return ' '.join(units[int(digit)] for digit in str(num))

@app.route("/")
def home():
    return """
        <h2>Number to Words Converter</h2>
        <form action="/convert" method="get">
            <input type="text" name="number" placeholder="Enter number">
            <input type="submit" value="Convert">
        </form>
    """

@app.route("/convert", methods=["GET"])
def convert():
    number = request.args.get("number")
    if not number:
        return jsonify({"error": "Please provide a number ?number=123"}), 400
    
    try:
        result = number_to_words(number)
        return jsonify({"number": number, "words": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
