import requests

def commitCounter(content):
	names = {'sungho park': 0, 'saideep vollala': 0, 'jingqi cheng': 0, 'brendan panici': 0, 'kevin le': 0, "brendan56": 0}

	for i in range(len(content)):
		names[content[i].get("committer_name").lower()] += 1

	names["brendan panici"] = names["brendan panici"] + names["brendan56"]
	del names["brendan56"]

	return names

def api():
	parameters = {"private_token": "JYFjjVSCXU6sxbsGrDb_", "per_page" : 100}
	project_id = str("16868890")
	url = 'https://gitlab.com/api/v4/projects/'+ project_id + '/repository/commits'

	reponse = requests.get(url, params = parameters)
	content= reponse.json()

	return (commitCounter(content))


if __name__ == '__main__':
	api()
