import pprint
import requests
import sys

sample_chain = {
    'chain': [
        {
            'index': 1,
            'previous_hash': 1,
            'proof': 100,
            'timestamp': 1571852367.484206,
            'transactions': [ ]
        },
        {
            'index': 2,
            'previous_hash': "ddf1adddad9af96695fda647492897f058aa702f806d7eaa21dfd46ecab0fcd1",
            'proof': 24368051,
            'timestamp': 1571852436.924649,
            'transactions': [
                {
                    'amount': 1,
                    'recipient': "Brian",
                    'sender': "0"
                }
            ]
        },
        {
            'index': 3,
            'previous_hash': "2fa2bcc7b423d5d74d621835b098842cf9dd34591bfc0e68800a41cf20b2ec90",
            'proof': 8132268,
            'timestamp': 1571852467.247827,
            'transactions': [
                {
                    'amount': 1,
                    'recipient': "Brian",
                    'sender': "0"
                }
            ]
        },
        {
            'index': 4,
            'previous_hash': "3f4b18d04371d8ce3129643ccf5ad46bb9943a87adf8c5addded0d3612128f59",
            'proof': 1301845,
            'timestamp': 1571852472.199991,
            'transactions': [
                {
                    'amount': 1,
                    'recipient': "Brian",
                    'sender': "0"
                }
            ]
        },
        {
            'index': 5,
            'previous_hash': "9177932144818f9c3072d11849251bdd31096621162f0e081016fa59e25010d2",
            'proof': 13176802,
            'timestamp': 1571852599.8256152,
            'transactions': [
                {
                    'amount': "3",
                    'recipient': "Beej",
                    'sender': "Brian"
                },
                {
                    'amount': 1,
                    'recipient': "Brian",
                    'sender': "0"
                }
            ]
        },
        {
            'index': 6,
            'previous_hash': "1e110e46bd7a6a86cd39c3adae667439a40e31b20db3b314bed5b1fa56c746ea",
            'proof': 41571496,
            'timestamp': 1571852940.9420102,
            'transactions': [
                {
                    'amount': ".5",
                    'recipient': "Brady",
                    'sender': "Beej"
                },
                {
                    'amount': ".5",
                    'recipient': "Elissa",
                    'sender': "Beej"
                },
                {
                    'amount': ".5",
                    'recipient': "Tom",
                    'sender': "Beej"
                },
                {
                    'amount': 1,
                    'recipient': "Brian",
                    'sender': "0"
                }
            ]
        }
    ],
    'length': 6
}

if __name__ == '__main__':
    # What is the server address? IE `python3 miner.py https://server.com/api/`
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"\

    # Run forever until interrupted
    while True:
        choice = input('enter test or live\n')
        if choice == 'test':
            data = sample_chain
        else:
            r = requests.get(url=node + "/chain")
            # Handle non-json response
            try:
                data = r.json()
            except ValueError:
                print("Error:  Non-json response")
                print("Response returned:")
                print(r)
                break

        user = input('enter user id, please:\n')

        ledger = [transaction for entry in data['chain'] for
                  transaction in entry['transactions'] if
                  transaction['recipient'] == user or
                  transaction['sender'] == user]

        balance = 0
        for transaction in ledger:
            transaction['amount'] = float(transaction['amount'])
            if transaction['recipient'] == user:
                balance += transaction['amount']
            elif transaction['sender'] == user:
                balance -= transaction['amount']
            else:
                print("Error in ledger")
                sys.exit()

        pprint.pprint(ledger)
        print(f'\nThe current balance for {user} is {balance} lambda coins.\n')

        another = input('Would you like another balance, y or n?\n')
        if another.lower() == 'n':
            sys.exit()
