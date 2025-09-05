import json
import pandas as pd
class few_short():
    def __init__(self,file_path="data/processed_data.json"):
        self.df = None
        self.unique_tags = None
        self.load_post(file_path)
    def load_post(self,file_path):
        with open(file_path,encoding="utf8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df['length']=self.df['line_count'].apply(self.categorize_length)
            all_tags = self.df["tags"].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))
    def get_filtered_post(self,length,language,tag):
        df_filtered = self.df[
           (self.df["tags"].apply(lambda tags: tag in tags))&
            (self.df["length"] == length)&
            (self.df["language"] == language)
        ]
        return df_filtered.to_dict(orient='records')


    def categorize_length(self,line_count):
        if line_count<5:
            return "short"
        elif 5<=line_count <=10:
            return "medium"
        else:
            return "long"

    def get_tags(self):
        return self.unique_tags
if __name__ == "__main__":
    fs = few_short()
    tags = fs.get_tags()
    print(tags)