from flask import Flask,request,jsonify
import re
app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def hello_bot():
    return "hello james"


# qa={
#     "ukimwi ni nini": "Ukimwi upungufu wa kinga mwilini",
#     "vvu ni nini": "Ni virusi vinavyosambaza Ukimwi"
# }


@app.route("/ask", methods=["POST","GET"])
def ask():
    qn=request.get_json()["question"].lower().replace("?","").strip()
    
    #dealing with meaning
    # use root words 
    if(re.search("nini", qn) or re.search("maan", qn)):
        if( ( re.search("pat",qn) or re.search("sabab",qn) ) and ( re.search("ukimwi",qn) or re.search("vvu",qn) )):
            ans="Ukimwi unaambukizwa kwa kuchangia vitu vya ncha kali na kwa kujamiiana"
        elif(re.search("ukimwi",qn)):
            ans="Ukimwi upungufu wa kinga mwilini"
        elif(re.search("vvu",qn)):
            ans="VVU ni virusi vinavyosababisha Ukimwi"
        
        else:
            ans="Tafadhali uliza kwa namna nyingine"
    #sababu za ukimwi
    elif( ( re.search("pat",qn) or re.search("sabab",qn) ) and ( re.search("ukimwi",qn) or re.search("vvu",qn) )): 
        ans="Ukimwi unaambukizwa kwa kuchangia vitu vya ncha kali na kwa kujamiiana"

    elif(re.search("king",qn) or re.search("zui",qn) or re.search("epuk",qn) ):
        ans="Kujikinga na Ukimwi tumia sheria ya ABC"
    #

    # ans=qa[qn]
    return ans
    # question=request.get_json()["question"].lower().replace("?","").strip()
    # return qa[question]