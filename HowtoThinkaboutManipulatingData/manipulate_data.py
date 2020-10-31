import pandas as pd

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

url = "https://en.wikipedia.org/wiki/NBA_All-Star_Game"


def main():
    df = pd.read_html(url)
    all_star_game_result_df = df[2]
    all_star_game_result_df = all_star_game_result_df.dropna().drop(["Game MVP","Host arena"],axis=1)[all_star_game_result_df.Year!='1999']
    all_star_game_result_df['East']=None
    all_star_game_result_df['West'] = None
    all_star_game_result_df['difference'] = None
    for index,row in all_star_game_result_df.iterrows():
        row['Year']=row['Year'][:4]
        for split_result in row['Result'].split(","):
            if 'East' in split_result:
                row['East']=int(split_result.split()[1])
            elif 'West' in split_result:
                row['West']=int(split_result.split()[1])
            elif 'East' not in split_result and 'West' not in split_result:
                row['East'] =None
                row['West'] =None
        row["Host city"]=row["Host city"].split(',')[0]
        row['difference'] = abs(int(row['East']) - int(row['West'])) if (row['East'] is not None and row['West'] is not None) else 0
    all_star_game_result_df=all_star_game_result_df.drop(["Result"],axis=1).dropna()
    all_star_game_result_df.set_index("Year",inplace=True)
    max_difference = all_star_game_result_df["difference"].max()
    min_difference = all_star_game_result_df["difference"].min()
    # print(all_star_game_result_df)

    all_star_game_result_difference_df = all_star_game_result_df[["Host city","difference"]].groupby("difference").agg(['count'])
    all_star_game_result_difference_df.columns=['difference count']
    all_star_game_result_difference_df.sort_values("difference count",inplace=True)
    # print(all_star_game_result_difference_df)
    all_star_game_result_df_city_count = all_star_game_result_df.groupby(["Host city"]).agg(['count'])
    all_star_game_result_df_city_count.columns=['East count','West count','difference count']
    all_star_game_result_df_city_count = all_star_game_result_df_city_count[['East count']]
    all_star_game_result_df_city_count.columns=['count']
    all_star_game_result_df_city_count.sort_values("count",inplace=True)
    all_star_game_result_df_city_count=all_star_game_result_df_city_count[all_star_game_result_df_city_count['count'] > 1]
    # print(all_star_game_result_df_city_count)
    all_star_game_result_df_city_count['average_score']=0
    for index,row in all_star_game_result_df_city_count.iterrows():
        city_record=all_star_game_result_df[all_star_game_result_df['Host city']==index].to_dict(orient='records')[0]
        east_score =int(city_record['East'])
        west_score = int(city_record['West'])
        average_score=(east_score+west_score)/2
        row['average_score']=average_score

    print("Maximum score difference between all games is {} and Minimum score difference between all games is {}".format(max_difference,min_difference))
    print("Average score between Eastern conference and Western conference in a city that hosted a game more than once is below")
    print(all_star_game_result_df_city_count)


if __name__ == '__main__':
    main()