import json

from flask import Flask, render_template, request

from closeio_api_client.api import CloseIO_API as Client

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/webhook", methods=['POST'])
def webhook():
    data = json.loads(request.form['data'])
    note = '---------------------------------\n'
    note += '\n'.join(['%s:\n%s\n---------------------------------' % (item['nickname'], item['body']) for item in data['items']])
    print note

    # TODO depending on what info you have in data (i.e. what you provide via
    # the JS API), figure out which lead to assign a note to. For the sake of
    # this example, a new lead is posted with the user's nickname as the company name

    api = Client('YOUR API KEY')
    resp = api.post('lead', { 'name': data['items'][0]['nickname'] })
    lead_id = resp['id']
    api.post('activity/note', { 'lead_id': lead_id, 'note': note })

    return 'ok'


if __name__ == "__main__":
    app.run(port=5000)

