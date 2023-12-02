from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer
model = SBertSummarizer('paraphrase-MiniLM-L6-v2')


def getSummary(body):
    result = model(body, num_sentences=10)
    return result

if __name__=="__main__":
    #body="With SBERT, BERT got the additional capability to compare massive sets for semantic similarities, groups, and retrieve information via semantic search."
    print(getSummary(body))
