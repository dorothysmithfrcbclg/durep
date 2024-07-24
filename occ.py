from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from keybert import KeyBERT

# Initialize KeyBERT
kw_model = KeyBERT(model)

# Helper function to calculate cTF-IDF
def calculate_ctfidf(docs, m, cluster):
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(docs)
    tfidf_feature_names = tfidf.get_feature_names_out()
    
    # Get the terms and their cTF-IDF scores
    scores = defaultdict(lambda: 0.0)
    for doc_id, doc in enumerate(docs):
        if m.labels_[doc_id] == cluster:
            feature_index = tfidf_matrix[doc_id, :].nonzero()[1]
            for i in feature_index:
                scores[tfidf_feature_names[i]] += tfidf_matrix[doc_id, i]
    
    return dict(scores)

# Organize documents by clusters
clustered_docs = defaultdict(list)
for idx, label in enumerate(cluster_labels):
    clustered_docs[label].append(sentences[idx])

# Compute cTF-IDF for each cluster
for cluster, docs in clustered_docs.items():
    ctfidf_scores = calculate_ctfidf(docs, cluster_model, cluster)
    keywords = kw_model.extract_keywords(" ".join(docs), keyphrase_ngram_range=(1, 2), stop_words='english')
    print(f"Cluster {cluster} Keywords:", keywords)
