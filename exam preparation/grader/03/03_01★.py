f = {
    "01": "The Sirindhorn Thai Language Institute",
    "02": "General Education Center",
    "20": "Graduate School",
    "21": "Faculty of Engineering",
    "22": "Faculty of Arts",
    "23": "Faculty of Science",
    "24": "Faculty of Political Science",
    "25": "Faculty of Architecture",
    "26": "Faculty of Commerce and Accountancy",
    "27": "Faculty of Education",
    "28": "Faculty of Communication Arts",
    "29": "Faculty of Economics",
    "30": "Faculty of Medicine",
    "31": "Faculty of Veterinary Science",
    "32": "Faculty of Dentistry",
    "33": "Faculty of Pharmaceutical Sciences",
    "34": "Faculty of Law",
    "35": "Faculty of Fine and Applied Arts",
    "36": "Faculty of Nursing",
    "37": "Faculty of Allied Health Sciences",
    "38": "Faculty of Psychology",
    "39": "Faculty of Sports Science",
    "40": "School of Agricultural",
    "51": "College of Population Studies",
    "53": "College of Public Health Sciences",
    "55": "Language Institute",
    "58": "Sasin Graduate Institute of Business Administration of Chulalongkorn University"
}


a = str(input())
if a in list(f.keys()) or a in list(f.values()):
    print("OK")
else:
    print("Error")
