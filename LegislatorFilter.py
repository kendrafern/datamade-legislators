import csv
from datetime import datetime
from datetime import timedelta

def main():
    inputfilename = "legislators.csv"
    outputfilename1 = "legislators1.csv"
    outputfilename2 = "legislators2.csv"
    header = ("title", "firstname", "middlename", "lastname", "name_suffix", "nickname", "party", "state", "district", "in_office", "gender", "phone", "fax", "website", "webform", "congress_office", "bioguide_id", "votesmart_id", "fec_id", "govtrack_id", "crp_id", "twitter_id", "congresspedia_url", "youtube_url", "facebook_id", "official_rss", "senate_class", "birthdate", "oc_email")

    inputdata = reader(inputfilename)

    youngdems = []
    today = datetime.today()
    yearsago45 = today - timedelta(days=(45*365.25))
    for i, x in enumerate(inputdata):
        bdateparts = x["birthdate"].split("-")
        birthdate = datetime(int(bdateparts[0]), int(bdateparts[1]), int(bdateparts[2]))
        if x["party"] == "D" and birthdate > yearsago45:
            youngdems.append(x)

    writer(header, youngdems, outputfilename1)

    socialreps = []
    for i, x in enumerate(inputdata):
        if x["party"] == "R" and x["twitter_id"] != "" and x["youtube_url"] != "":
            socialreps.append(x)

    writer(header, socialreps, outputfilename2)

def writer(header, data, filename):
    with open (filename, "w", newline = "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = header)
        writer.writeheader()
        writer.writerows(data)

def reader(filename):
    with open(filename, newline = "") as file:
        return [row for row in csv.DictReader(file)]

main()
