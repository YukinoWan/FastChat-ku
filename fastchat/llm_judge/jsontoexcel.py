import json
import sys
from tqdm import tqdm
import pandas as pd

def convert(q_data, a_data, model_id):
    output_data = ["question_id, question, {}".format(model_id)]
    length = len(q_data)
    out_dict = []
    new_q = {}
    new_a = {}
    for i in tqdm(range(length)):
        q_dict = json.loads(q_data[i])
        a_dict = json.loads(a_data[i])

        #new_q = {}
        new_q[q_dict["question_id"]] = q_dict["turns"][0]

        #new_a = {}
        new_a[a_dict["question_id"]] = a_dict["choices"][0]["turns"][0]
    for i in tqdm(range(length)):
        q_id = i + 1
        new_line = "\"" + str(q_id) + "\",\"" + new_q[q_id] + "\",\"" + new_a[q_id] + "\""
        output_data.append(new_line)
        new_dict = {}
        new_dict["question_id"] = q_id
        new_dict["question"] = new_q[q_id]
        new_dict["{}".format(model_id)] = new_a[q_id]
        out_dict.append(new_dict)
        
    return output_data, out_dict

       

if __name__ == "__main__":
    question_file = sys.argv[1]
    model_id = sys.argv[2]
    output_file = sys.argv[3]

    answer_file = "/home/zhen/FastChat-ku/fastchat/llm_judge/data/vicuna_bench/model_answer/{}.jsonl".format(model_id)
    with open(question_file, "r") as f:
        q_data = f.read().splitlines()

    with open(answer_file, "r") as f:
        a_data = f.read().splitlines()

    output_data, out_dict = convert(q_data, a_data,model_id)
    print(len(output_data))
    print(out_dict[1])

    df = pd.DataFrame(out_dict)
    df.to_excel(output_file)
    #with open(output_file, "w") as f:
    #    for line in tqdm(out_dict):
    #        json.dump(line, f)
    #        f.write("\n")



