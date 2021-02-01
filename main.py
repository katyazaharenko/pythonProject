import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('lenta-ru-news.csv', dtype={"url": str, "title": str,
                                                   "text": str, "topic": str,
                                                   "tags": str})
    print('hello')
    data.groupby(['topic', 'tags']).size()
