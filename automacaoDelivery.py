from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Processar a mensagem do WhatsApp
    print(data)
    return "Mensagem recebida!", 200

if __name__ == "__main__":
    app.run(debug=True)
