# Import necessary modules
from config import H2O_GPT_E_API_KEY, REMOTE_ADDRESS
from h2ogpte import H2OGPTE
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer

# Initialize H2O GPT client
client = H2OGPTE(address=REMOTE_ADDRESS, api_key=H2O_GPT_E_API_KEY)

# Define the translation function
def translate_text(question, target_language="Spanish", llm="gpt-4o-mini", llm_args=None):
    """
    Uses H2OGPTE client to translate a given text to a target language.
    """
    if llm_args is None:
        llm_args = dict(temperature=0.5, max_new_tokens=100,response_format="text")
    prompt = f"""You are a professional translation assistant. 
    Your task is to translate ```{question}``` from English to a specified ```{target_language}``` language while 
    maintaining the original meaning, tone, and context. Just provide translation in the final output and nothing else."""
    response = client.answer_question(question=prompt, llm=llm, llm_args=llm_args,)
    return response.content.strip()

# Define function to calculate BLEU and ROUGE scores
def evaluate_translation(reference, candidate):
    """
    Evaluates the translation quality using BLEU and ROUGE metrics.
    """
    # BLEU score
    smoothie = SmoothingFunction().method4
    bleu_score = sentence_bleu([reference.split()], candidate.split(), weights=(1.0, 0, 0, 0), smoothing_function=smoothie)
    
    # ROUGE scores
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(reference, candidate)
    
    return {
        "BLEU": bleu_score,
        "ROUGE-1": rouge_scores['rouge1'].fmeasure,
        "ROUGE-2": rouge_scores['rouge2'].fmeasure,
        "ROUGE-L": rouge_scores['rougeL'].fmeasure
    }

# Load WMT data (or use a simplified dataset for this example)
# Example reference and test sentences
wmt_data = [
    {"source": "How are you?", "reference": "¿Cómo estás?"},
    {"source": "Good morning", "reference": "Buenos días"},
    {"source": "What is your name?", "reference": "¿Cómo te llamas?"},
]

# Translate and evaluate
results = []
for data in wmt_data:
    source = data["source"]
    reference = data["reference"]
    
    # Perform translation
    candidate = translate_text(source)
    # print(f"Source: {source}")
    # print(f"Reference: {reference}")
    # print(f"Candidate: {candidate}")
    
    # Evaluate translation
    metrics = evaluate_translation(reference, candidate)
    results.append({"source": source, "reference": reference, "candidate": candidate, "metrics": metrics})

# Display results
for result in results:
    print(f"\nSource: {result['source']}")
    print(f"Reference: {result['reference']}")
    print(f"Candidate: {result['candidate']}")
    print(f"Metrics: {result['metrics']}")