





def read_from_json():
  import json

  with open(r"files/newsafr.json", encoding='utf-8') as f:
    json_data = json.load(f)

  description_list = []
  for i in json_data["rss"]["channel"]["items"]:
    ad = i["description"].split()
    description_list.extend(ad)

  def sortByLength(inputStr):
    return len(inputStr)

  description_list.sort(key=sortByLength, reverse=True)
  new_list = description_list
  print()

  new2_list = []
  for d in new_list:
    if len(d) > 6:
      new2_list.append(d)

  from collections import Counter

  c = Counter(new2_list)

  print(c.most_common(10))
  print()

# read_from_json()

def read_from_xml():
  import xml.etree.ElementTree as ET

  parser = ET.XMLParser(encoding="utf-8")
  tree = ET.parse(f"files/newsafr.xml", parser)
  root = tree.getroot()
  channel = root.find("channel")
  items = channel.findall("item")

  description_list = []

  for item in items:
    a = item.find("description").text
    ad = a.split()
    description_list.extend(ad)

  def sortByLength(inputStr):
      return len(inputStr)

  description_list.sort(key=sortByLength, reverse=True)
  new_list = description_list
  print()

  new2_list = []
  for d in new_list:
    if len(d) > 6:
      new2_list.append(d)

  from collections import Counter

  c = Counter(new2_list)

  print(c.most_common(10))


# read_from_xml()




