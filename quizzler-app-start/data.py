import requests

question_results = {'amount':10,
                     'type': 'boolean'
                    }

results = requests.get('https://opentdb.com/api.php', params=question_results)
results = results.json()
question_data = results['results']

