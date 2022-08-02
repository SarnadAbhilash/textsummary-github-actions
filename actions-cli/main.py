from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def main():

    parser = ArgumentParser(
        description="Generate a summary of any article",
        formatter_class=ArgumentDefaultsHelpFormatter,
        conflict_handler="resolve",
    )
    parser.add_argument(
        "article",
        help="Path to article file",
        type=str,
    )
    args = parser.parse_args()

    with open(args.article, 'r') as article_file:
        article = article_file.read()

    model = AutoModelForSeq2SeqLM.from_pretrained('google/pegasus-xsum')
    tokenizer = AutoTokenizer.from_pretrained('google/pegasus-xsum')
    

    tokens_input = tokenizer.encode("summarize: "+ article, return_tensors='pt', max_length=512, truncation=True)
    ids = model.generate(tokens_input, min_length=80, max_length=120)
    summary = tokenizer.decode(ids[0], skip_special_tokens=True)

   
    return  print(summary)


if __name__ == "__main__":
    main()