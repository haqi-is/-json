
import json
import os
def unite_json_words(root_path):
    words={}
    des_path=os.path.join(root_path,"unitl.json")
    for file in os.listdir(root_path):
        if os.path.isfile(os.path.join(root_path,file)):
            json_path = os.path.join(root_path, file)
            with open(json_path, "r", encoding="utf-8") as f:
                src_words = json.load(f)
                words=dict(list(words.items())+list(src_words.items()))
    if is_save==True:
        with open(des_path,"w",encoding="utf-8") as f:
            f.seek(0,2)
            words=json.dumps(words,indent=4)
            f.write(words)
        print("save succeed")
    return words