def transformation_based_tagging(sentence):
    tagged_sentence = []
    
    words = sentence.split()

    for i, word in enumerate(words):
        # Rule: Words ending with "-ing" are tagged as verbs
        if word.endswith("ing"):
            tagged_sentence.append((word, 'VERB'))
        else:
            tagged_sentence.append((word, 'UNKNOWN'))

    return tagged_sentence

# Example usage:
input_sentence = "The cat is jumping on the table."
tagged_result = transformation_based_tagging(input_sentence)

print("Tagged Sentence:")
for word, pos_tag in tagged_result:
    print(f"{word}: {pos_tag}")
